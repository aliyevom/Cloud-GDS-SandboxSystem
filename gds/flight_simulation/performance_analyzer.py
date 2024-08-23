import logging
from statistics import mean, stdev
from datetime import datetime

class PerformanceAnalyzer:
    """Analyzes performance data collected during a flight simulation."""

    def __init__(self, performance_data):
        self.performance_data = performance_data
        self.analysis_report = {}

    def analyze_altitude(self):
        """Analyzes altitude data for anomalies."""
        altitudes = [dp["altitude"] for dp in self.performance_data]
        mean_altitude = mean(altitudes)
        stddev_altitude = stdev(altitudes)
        self.analysis_report["mean_altitude"] = mean_altitude
        self.analysis_report["stddev_altitude"] = stddev_altitude

        low_altitude_warnings = [dp for dp in self.performance_data if dp["altitude"] < 32000]
        if low_altitude_warnings:
            logging.warning(f"Low altitude warnings: {len(low_altitude_warnings)} occurrences.")
            self.analysis_report["low_altitude_warnings"] = len(low_altitude_warnings)

    def analyze_speed(self):
        """Analyzes speed data for anomalies."""
        speeds = [dp["speed"] for dp in self.performance_data]
        mean_speed = mean(speeds)
        stddev_speed = stdev(speeds)
        self.analysis_report["mean_speed"] = mean_speed
        self.analysis_report["stddev_speed"] = stddev_speed

        high_speed_warnings = [dp for dp in self.performance_data if dp["speed"] > 500]
        if high_speed_warnings:
            logging.warning(f"High speed warnings: {len(high_speed_warnings)} occurrences.")
            self.analysis_report["high_speed_warnings"] = len(high_speed_warnings)

    def analyze_fuel_usage(self):
        """Analyzes fuel usage for inefficiencies."""
        fuel_levels = [dp["fuel_level"] for dp in self.performance_data]
        if fuel_levels:
            initial_fuel = fuel_levels[0]
            final_fuel = fuel_levels[-1]
            fuel_used = initial_fuel - final_fuel
            self.analysis_report["fuel_used"] = fuel_used
            logging.info(f"Fuel used during flight: {fuel_used}%.")

    def generate_report(self):
        """Generates a comprehensive analysis report."""
        logging.info("Generating performance analysis report...")
        self.analyze_altitude()
        self.analyze_speed()
        self.analyze_fuel_usage()
        self.analysis_report["report_generated"] = datetime.utcnow().isoformat()
        logging.info(f"Analysis Report: {self.analysis_report}")
        return self.analysis_report

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sample_data = [
        {"altitude": 31000, "speed": 505, "heading": 180, "pitch": 2.0, "roll": 0.5, "yaw": 0.1, "engine_temp": 210, "fuel_level": 90, "wind_speed": 10, "wind_direction": 270, "timestamp": 1651234567.0},
        {"altitude": 35000, "speed": 490, "heading": 190, "pitch": 1.0, "roll": -0.5, "yaw": -0.1, "engine_temp": 215, "fuel_level": 85, "wind_speed": 15, "wind_direction": 280, "timestamp": 1651234577.0}
    ]
    analyzer = PerformanceAnalyzer(sample_data)
    report = analyzer.generate_report()
    logging.info(f"Final Report: {report}")
