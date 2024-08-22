class TrainingAssessment:
    def assess(self, performance_data):
        score = 0
        for data_point in performance_data:
            if data_point["altitude"] >= 32000 and data_point["speed"] <= 500:
                score += 10
            else:
                score -= 5

        if score > 70:
            return "Eligible for next flight"
        else:
            return "Requires further training"

if __name__ == "__main__":
    sample_data = [
        {"altitude": 31000, "speed": 505, "heading": 180, "timestamp": 1651234567.0},
        {"altitude": 35000, "speed": 490, "heading": 190, "timestamp": 1651234577.0}
    ]
    assessment = TrainingAssessment()
    result = assessment.assess(sample_data)
    print(f"Assessment result: {result}")
