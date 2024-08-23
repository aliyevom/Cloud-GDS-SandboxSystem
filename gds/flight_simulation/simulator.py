import random
import time
import uuid
import logging
from datetime import datetime, timedelta

class TelemetrySystem:
    """Simulates interaction with an external telemetry system."""
    
    def __init__(self, pilot_id, aircraft_id):
        self.pilot_id = pilot_id
        self.aircraft_id = aircraft_id
        self.session_id = str(uuid.uuid4())
        logging.info(f"Telemetry session {self.session_id} started for pilot {pilot_id} and aircraft {aircraft_id}.")

    def generate_data_point(self):
        """Generates a simulated telemetry data point."""
        data_point = {
            "session_id": self.session_id,
            "timestamp": datetime.utcnow().isoformat(),
            "altitude": random.uniform(30000, 40000),  # in feet
            "speed": random.uniform(450, 550),         # in knots
            "heading": random.uniform(0, 360),         # in degrees
            "pitch": random.uniform(-5, 5),            # in degrees
            "roll": random.uniform(-10, 10),           # in degrees
            "yaw": random.uniform(-5, 5),              # in degrees
            "engine_temp": random.uniform(200, 250),   # in Celsius
            "fuel_level": random.uniform(20, 100),     # in percentage
            "wind_speed": random.uniform(0, 50),       # in knots
            "wind_direction": random.uniform(0, 360)   # in degrees
        }
        return data_point

    def send_data(self, data_point):
        """Simulates sending telemetry data to an external system."""
        # In a real system, this could be an HTTP POST or gRPC call.
        logging.info(f"Sending telemetry data: {data_point}")
        # Here we simulate success or failure.
        if random.random() < 0.98:  # 98% chance of success
            return True
        else:
            raise ConnectionError("Failed to send telemetry data.")

    def end_session(self):
        """Ends the telemetry session."""
        logging.info(f"Telemetry session {self.session_id} ended.")

class FlightSimulator:
    """Simulates a flight for a given pilot and aircraft."""

    def __init__(self, pilot_id, aircraft_id):
        self.pilot_id = pilot_id
        self.aircraft_id = aircraft_id
        self.telemetry_system = TelemetrySystem(pilot_id, aircraft_id)
        self.performance_data = []

    def simulate(self, duration_minutes=60):
        """Simulates flight over a specified duration in minutes."""
        logging.info(f"Starting flight simulation for {self.pilot_id} on {self.aircraft_id}.")
        start_time = datetime.utcnow()
        end_time = start_time + timedelta(minutes=duration_minutes)
        
        while datetime.utcnow() < end_time:
            data_point = self.telemetry_system.generate_data_point()
            self.performance_data.append(data_point)
            try:
                self.telemetry_system.send_data(data_point)
            except ConnectionError as e:
                logging.error(e)
            time.sleep(1)  # Simulate real-time data collection

        self.telemetry_system.end_session()
        logging.info(f"Flight simulation complete. {len(self.performance_data)} data points collected.")
        return self.performance_data

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    simulator = FlightSimulator("Pilot123", "Aircraft456")
    data = simulator.simulate(duration_minutes=5)  # Simulate for 5 minutes
    logging.info(f"Collected data: {data}")
