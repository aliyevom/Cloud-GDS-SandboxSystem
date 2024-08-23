class ScenarioManager:
    def __init__(self):
        self.scenarios = []

    def create_scenario(self, pilot_id, aircraft_id, weather_conditions, mission_objectives):
        scenario = {
            "pilot_id": pilot_id,
            "aircraft_id": aircraft_id,
            "weather_conditions": weather_conditions,
            "mission_objectives": mission_objectives
        }
        self.scenarios.append(scenario)
        return scenario

    def get_scenario(self, pilot_id):
        for scenario in self.scenarios:
            if scenario["pilot_id"] == pilot_id:
                return scenario
        raise ValueError(f"No scenario found for pilot {pilot_id}")

    def remove_scenario(self, pilot_id):
        self.scenarios = [s for s in self.scenarios if s["pilot_id"] != pilot_id]

    def list_scenarios(self):
        return self.scenarios
