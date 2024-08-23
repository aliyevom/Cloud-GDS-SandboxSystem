class ReportGenerator:
    def __init__(self):
        self.reports = []

    def generate_report(self, simulation_result):
        report = {
            "pilot_id": simulation_result["pilot_id"],
            "score": simulation_result["score"],
            "success": simulation_result["success"],
            "details": simulation_result["log"]
        }
        self.reports.append(report)
        return report

    def save_report(self, report, filepath):
        with open(filepath, "w") as file:
            file.write(f"Pilot ID: {report['pilot_id']}\n")
            file.write(f"Score: {report['score']}\n")
            file.write(f"Success: {report['success']}\n")
            file.write(f"Details:\n{report['details']}\n")

    def get_report(self, pilot_id):
        for report in self.reports:
            if report["pilot_id"] == pilot_id:
                return report
        raise ValueError(f"No report found for pilot {pilot_id}")
