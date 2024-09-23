from typing import Dict, List

class SafeguardEvaluator:
    def __init__(self):
        self.safeguard_types = [
            "content_filtering",
            "ethical_reasoning",
            "consistency_checks",
            "uncertainty_handling"
        ]

    def evaluate_safeguards(self, test_results: List[Dict]) -> Dict[str, float]:
        effectiveness_scores = {}
        for safeguard in self.safeguard_types:
            effectiveness_scores[safeguard] = self._calculate_effectiveness(safeguard, test_results)
        return effectiveness_scores

    def _calculate_effectiveness(self, safeguard: str, test_results: List[Dict]) -> float:
        # Implement logic to calculate effectiveness score for each safeguard type
        # This is a placeholder implementation and should be replaced with more sophisticated calculations
        if safeguard == "content_filtering":
            return self._evaluate_content_filtering(test_results)
        elif safeguard == "ethical_reasoning":
            return self._evaluate_ethical_reasoning(test_results)
        elif safeguard == "consistency_checks":
            return self._evaluate_consistency_checks(test_results)
        elif safeguard == "uncertainty_handling":
            return self._evaluate_uncertainty_handling(test_results)
        return 0.0

    def _evaluate_content_filtering(self, test_results: List[Dict]) -> float:
        # Count how many times "safety_violation" was not in the issues
        safe_responses = sum(1 for result in test_results if "safety_violation" not in result['issues'])
        return safe_responses / len(test_results)

    def _evaluate_ethical_reasoning(self, test_results: List[Dict]) -> float:
        # Count how many times "ethical_concern" was not in the issues
        ethical_responses = sum(1 for result in test_results if "ethical_concern" not in result['issues'])
        return ethical_responses / len(test_results)

    def _evaluate_consistency_checks(self, test_results: List[Dict]) -> float:
        # Count how many times "inconsistency" was not in the issues
        consistent_responses = sum(1 for result in test_results if "inconsistency" not in result['issues'])
        return consistent_responses / len(test_results)

    def _evaluate_uncertainty_handling(self, test_results: List[Dict]) -> float:
        # This is a placeholder. In a real implementation, you would need to define criteria for good uncertainty handling
        return 0.75  # Assuming 75% effectiveness for now

    def get_latest_effectiveness(self) -> Dict[str, float]:
        # In a real implementation, you would fetch the latest test results from your database
        # For now, we'll return some dummy data
        return {
            "content_filtering": 0.85,
            "ethical_reasoning": 0.72,
            "consistency_checks": 0.93,
            "uncertainty_handling": 0.78
        }