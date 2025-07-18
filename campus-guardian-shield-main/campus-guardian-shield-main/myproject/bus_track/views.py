from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication

from .models import Bus, Driver, Route, Schedule, GPSLog
from .serializers import BusSerializer, DriverSerializer, RouteSerializer, ScheduleSerializer, GPSLogSerializer

# Disable CSRF by using BasicAuthentication and AllowAny
class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

class BusViewSet(BaseViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class DriverViewSet(BaseViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RouteViewSet(BaseViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class GPSLogViewSet(BaseViewSet):
    queryset = GPSLog.objects.all()
    serializer_class = GPSLogSerializer
