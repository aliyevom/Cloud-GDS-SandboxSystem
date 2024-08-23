import unittest
from report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = ReportGenerator()

    def test_generate_report(self):
        simulation_result = {
            "pilot_id": "Pilot1",
            "score": 95,
            "success": True,
            "log": "Simulation complete."
        }
        report = self.generator.generate_report(simulation_result)
        self.assertEqual(report["pilot_id"], "Pilot1")
        self.assertEqual(report["score"], 95)

    def test_save_report(self):
        simulation_result = {
            "pilot_id": "Pilot1",
            "score": 95,
            "success": True,
            "log": "Simulation complete."
        }
        report = self.generator.generate_report(simulation_result)
        self.generator.save_report(report, "report.txt")
        with open("report.txt", "r") as file:
            content = file.read()
        self.assertIn("Pilot ID: Pilot1", content)

if __name__ == '__main__':
    unittest.main()
