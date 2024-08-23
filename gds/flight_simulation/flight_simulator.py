import random

class FlightSimulator:
    def __init__(self):
        self.simulation_results = []

    def run_simulation(self, scenario):
        result = {
            "pilot_id": scenario["pilot_id"],
            "success": self._evaluate_success(scenario),
            "score": self._calculate_score(scenario),
            "log": self._generate_log(scenario)
        }
        self.simulation_results.append(result)
        return result

    def _evaluate_success(self, scenario):
        weather = scenario["weather_conditions"]
        if weather == "clear":
            return True
        elif weather == "stormy":
            return random.choice([True, False])
        else:
            return False

    def _calculate_score(self, scenario):
        base_score = 100
        if scenario["weather_conditions"] == "stormy":
            base_score -= 30
        if scenario["mission_objectives"] == "reconnaissance":
            base_score += 20
        return base_score

    def _generate_log(self, scenario):
        log = f"Simulation log for pilot {scenario['pilot_id']} in aircraft {scenario['aircraft_id']}:\n"
        log += f"Weather: {scenario['weather_conditions']}\n"
        log += f"Mission: {scenario['mission_objectives']}\n"
        log += "Simulation complete.\n"
        return log
