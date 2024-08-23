import unittest
from scenario_manager import ScenarioManager

class TestScenarioManager(unittest.TestCase):

    def setUp(self):
        self.manager = ScenarioManager()

    def test_create_scenario(self):
        scenario = self.manager.create_scenario("Pilot1", "Aircraft1", "clear", "reconnaissance")
        self.assertEqual(scenario["pilot_id"], "Pilot1")
        self.assertEqual(scenario["weather_conditions"], "clear")

    def test_get_scenario(self):
        self.manager.create_scenario("Pilot1", "Aircraft1", "clear", "reconnaissance")
        scenario = self.manager.get_scenario("Pilot1")
        self.assertIsNotNone(scenario)

    def test_remove_scenario(self):
        self.manager.create_scenario("Pilot1", "Aircraft1", "clear", "reconnaissance")
        self.manager.remove_scenario("Pilot1")
        with self.assertRaises(ValueError):
            self.manager.get_scenario("Pilot1")

    def test_list_scenarios(self):
        self.manager.create_scenario("Pilot1", "Aircraft1", "clear", "reconnaissance")
        self.manager.create_scenario("Pilot2", "Aircraft2", "stormy", "combat")
        scenarios = self.manager.list_scenarios()
        self.assertEqual(len(scenarios), 2)

if __name__ == '__main__':
    unittest.main()
