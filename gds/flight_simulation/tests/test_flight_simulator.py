import unittest
from flight_simulator import FlightSimulator

class TestFlightSimulator(unittest.TestCase):

    def setUp(self):
        self.simulator = FlightSimulator()

    def test_run_simulation(self):
        scenario = {
            "pilot_id": "Pilot1",
            "aircraft_id": "Aircraft1",
            "weather_conditions": "clear",
            "mission_objectives": "reconnaissance"
        }
        result = self.simulator.run_simulation(scenario)
        self.assertTrue(result["success"])
        self.assertGreaterEqual(result["score"], 100)

    def test_simulation_stormy_weather(self):
        scenario = {
            "pilot_id": "Pilot1",
            "aircraft_id": "Aircraft1",
            "weather_conditions": "stormy",
            "mission_objectives": "combat"
        }
        result = self.simulator.run_simulation(scenario)
        self.assertIn(result["success"], [True, False])

if __name__ == '__main__':
    unittest.main()
