from rest_framework import serializers
from .models import Bus, Driver, Route, Schedule, GPSLog, StopTime
from django.utils import timezone

# ROUTE
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name', 'start_point', 'end_point', 'stops']

# STOP TIME
class StopTimeSerializer(serializers.ModelSerializer):
    late_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StopTime
        fields = ['id', 'stop_name', 'arrival_time', 'actual_arrival_time', 'stop_status', 'late_by']

    def get_late_by(self, obj):
        if obj.actual_arrival_time:
            diff = obj.actual_arrival_time - obj.arrival_time
            minutes = int(diff.total_seconds() // 60)
            if minutes > 0:
                return f"{minutes} min late"
            elif minutes < 0:
                return f"{abs(minutes)} min early"
            else:
                return "on time"
        return None

# SCHEDULE
class ScheduleSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    route_id = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(), source='route', write_only=True)
    stop_times = StopTimeSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ['id', 'route', 'route_id', 'bus', 'departure_time', 'arrival_time', 'stop_times']

    def create(self, validated_data):
        stop_times_data = validated_data.pop('stop_times')
        schedule = Schedule.objects.create(**validated_data)
        for stop_time_data in stop_times_data:
            StopTime.objects.create(schedule=schedule, **stop_time_data)
        return schedule

    def update(self, instance, validated_data):
        stop_times_data = validated_data.pop('stop_times', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if stop_times_data:
            instance.stop_times.all().delete()
            for stop_time_data in stop_times_data:
                StopTime.objects.create(schedule=instance, **stop_time_data)

        return instance

# SCHEDULE WITH ROUTE (if needed for condensed view)
class ScheduleWithRouteSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'route', 'bus', 'departure_time', 'arrival_time']

# DRIVER
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

# BUS
class BusSerializer(serializers.ModelSerializer):
    last_trip = serializers.SerializerMethodField()
    next_trip = serializers.SerializerMethodField()
    driver = serializers.SerializerMethodField()

    class Meta:
        model = Bus
        fields = '__all__'
        read_only_fields = ['last_trip', 'next_trip', 'driver']

    def get_last_trip(self, obj):
        last_schedule = Schedule.objects.filter(bus=obj, departure_time__lt=timezone.now()).order_by('-departure_time').first()
        return ScheduleSerializer(last_schedule).data if last_schedule else None

    def get_driver(self, obj):
        driver = Driver.objects.filter(assigned_bus=obj).first()
        return DriverSerializer(driver).data if driver else None

    def get_next_trip(self, obj):
        next_schedule = Schedule.objects.filter(bus=obj, departure_time__gte=timezone.now()).order_by('departure_time').first()
        return ScheduleSerializer(next_schedule).data if next_schedule else None

# GPS LOG
class GPSLogSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    bus_id = serializers.PrimaryKeyRelatedField(queryset=Bus.objects.all(), source='bus', write_only=True)

    timestamp = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%SZ",
        required=False,
        input_formats=["%Y-%m-%dT%H:%M:%SZ", "iso-8601"]
    )

    log_type = serializers.ChoiceField(choices=GPSLog.LOG_TYPES, default=GPSLog.ENTRY)

    class Meta:
        model = GPSLog
        fields = ['id', 'bus', 'bus_id', 'latitude', 'longitude', 'timestamp', 'log_type']
        read_only_fields = ['timestamp']

    def validate(self, data):
        if not (-90 <= data.get('latitude', 0) <= 90):
            raise serializers.ValidationError("Latitude must be between -90 and 90")
        if not (-180 <= data.get('longitude', 0) <= 180):
            raise serializers.ValidationError("Longitude must be between -180 and 180")
        return data

    def create(self, validated_data):
        return GPSLog.objects.create(**validated_data)
