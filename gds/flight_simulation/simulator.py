import random
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlightSimulator:
    def __init__(self, pilot_id, aircraft_id):
        self.pilot_id = pilot_id
        self.aircraft_id = aircraft_id

    def simulate_flight(self):
        logger.info(f"Starting flight simulation for pilot {self.pilot_id} on aircraft {self.aircraft_id}.")
        flight_duration = random.randint(1, 6)  # Simulate 1 to 6 hours of flight
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=flight_duration)
        performance_metrics = self.generate_performance_metrics()

        logger.info(f"Flight simulation completed. Duration: {flight_duration} hours.")
        return {
            "pilot_id": self.pilot_id,
            "aircraft_id": self.aircraft_id,
            "start_time": start_time,
            "end_time": end_time,
            "performance_metrics": performance_metrics
        }

    def generate_performance_metrics(self):
        metrics = {
            "landings": random.randint(1, 5),
            "takeoffs": random.randint(1, 5),
            "errors": random.randint(0, 3),
            "fuel_efficiency": random.uniform(0.8, 1.0)  # Ratio
        }
        logger.info(f"Generated performance metrics: {metrics}")
        return metrics

if __name__ == "__main__":
    simulator = FlightSimulator("Pilot123", "A320")
    simulation_data = simulator.simulate_flight
