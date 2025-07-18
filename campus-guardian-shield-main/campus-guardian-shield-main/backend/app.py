from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
from datetime import datetime

# Initialize Flask and MongoDB client
app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb+srv://workspavan6:8n5tA1NXVaGLFLf4@cluster0.xkiu1hj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Connect to MongoDB
db = client['bus_tracking']  # Use bus_tracking database

# MongoDB collections
bus_collection = db['buses']
gps_log_collection = db['gps_logs']

class BusEntryExitLog(Resource):
    def post(self):
        data = request.get_json()

        # Simulate logging entry or exit event
        log_data = {
            "plate_number": data["plate_number"],
            "timestamp": datetime.utcnow(),
            "log_type": data["log_type"]  # Either "entry" or "exit"
        }

        # Insert into MongoDB
        gps_log_collection.insert_one(log_data)

        # Return a success message
        return jsonify({"message": "Bus entry/exit logged successfully", "data": log_data})

class BusInfo(Resource):
    def get(self):
        # Fetch all bus data from MongoDB
        buses = list(bus_collection.find())
        for bus in buses:
            bus["_id"] = str(bus["_id"])  # Convert ObjectId to string for JSON serialization
        return jsonify(buses)
@app.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong from Flask!"},


# Adding resources to the API
api.add_resource(BusEntryExitLog, '/log_entry_exit')
api.add_resource(BusInfo, '/buses')

if __name__ == '__main__':
    app.run(debug=True)
