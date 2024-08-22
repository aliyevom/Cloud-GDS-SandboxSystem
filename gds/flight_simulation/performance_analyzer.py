import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PerformanceAnalyzer:
    def __init__(self, simulation_data):
        self.simulation_data = simulation_data

    def analyze(self):
        logger.info(f"Analyzing simulation data for pilot {self.simulation_data['pilot_id']} on aircraft {self.simulation_data['aircraft_id']}.")
        score = self.calculate_performance_score(self.simulation_data['performance_metrics'])
        result = {
            "pilot_id": self.simulation_data["pilot_id"],
            "score": score,
            "recommendation": self.get_recommendation(score)
        }
        logger.info(f"Performance analysis completed: {result}")
        return result

    def calculate_performance_score(self, metrics):
        base_score = 100
        penalties = metrics["errors"] * 10
        efficiency_bonus = metrics["fuel_efficiency"] * 20
        final_score = base_score - penalties + efficiency_bonus
        return max(min(final_score, 100), 0)

    def get_recommendation(self, score
