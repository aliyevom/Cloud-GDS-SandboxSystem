import statistics
from datetime import datetime

class TrainingAssessment:
    def __init__(self, performance_data):
        self.performance_data = performance_data

    def assess_flight_protocols(self):
        score = 0
        protocol_violations = []

        for data_point in self.performance_data:
            if data_point["altitude"] < 32000:
                protocol_violations.append(f"Low altitude at {data_point['timestamp']}")
                score -= 10
            if data_point["speed"] > 500:
                protocol_violations.append(f"High speed at {data_point['timestamp']}")
                score -= 10
            if not 0 <= data_point["heading"] <= 360:
                protocol_violations.append(f"Invalid heading at {data_point['timestamp']}")
                score -= 15

        return score, protocol_violations

    def assess_decision_making(self):
        # Simulate decision-making assessment based on response time to simulated events
        response_times = [dp["response_time"] for dp in self.performance_data if "response_time" in dp]
        if not response_times:
            return 0, ["No response data available"]

        avg_response_time = statistics.mean(response_times)
        score = max(0, 100 - avg_response_time)  # Deduct points for slower response

        feedback = []
        if avg_response_time > 30:
            feedback.append(f"Slow response time: {avg_response_time} seconds")

        return score, feedback

    def assess_overall_performance(self):
        protocol_score, protocol_feedback = self.assess_flight_protocols()
        decision_score, decision_feedback = self.assess_decision_making()

        total_score = protocol_score + decision_score
        feedback = protocol_feedback + decision_feedback

        eligibility = "Eligible for next flight" if total_score >= 70 else "Requires further training"

        return {
            "total_score": total_score,
            "eligibility": eligibility,
            "feedback": feedback
        }

if __name__ == "__main__":
    # Simulated performance data
    sample_data = [
        {"altitude": 31000, "speed": 505, "heading": 180, "response_time": 25, "timestamp": datetime.now().timestamp()},
        {"altitude": 35000, "speed": 490, "heading": 190, "response_time": 20, "timestamp": datetime.now().timestamp()},
        {"altitude": 33000, "speed": 470, "heading": 360, "response_time": 35, "timestamp": datetime.now().timestamp()},
    ]

    assessment = TrainingAssessment(sample_data)
    result = assessment.assess_overall_performance()
    print(f"Assessment result: {result['eligibility']}")
    print(f"Total Score: {result['total_score']}")
    for feedback in result['feedback']:
        print(f"Feedback: {feedback}")
