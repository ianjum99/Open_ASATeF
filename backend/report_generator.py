from typing import Dict, List

class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, test_results: List[Dict], safeguard_effectiveness: Dict[str, float]) -> str:
        report = "AI Stress-Testing Framework Report\n\n"
        report += self._summarize_test_results(test_results)
        report += self._summarize_safeguard_effectiveness(safeguard_effectiveness)
        report += self._generate_improvement_suggestions(test_results, safeguard_effectiveness)
        return report

    def _summarize_test_results(self, test_results: List[Dict]) -> str:
        summary = "Test Results Summary:\n"
        summary += f"Total scenarios tested: {len(test_results)}\n"
        
        issue_counts = {}
        for result in test_results:
            for issue in result['issues']:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1
        
        summary += "Issues detected:\n"
        for issue, count in issue_counts.items():
            summary += f"- {issue}: {count} times\n"
        
        return summary + "\n"

    def _summarize_safeguard_effectiveness(self, safeguard_effectiveness: Dict[str, float]) -> str:
        summary = "Safeguard Effectiveness Summary:\n"
        for safeguard, score in safeguard_effectiveness.items():
            summary += f"- {safeguard}: {score:.2%}\n"
        return summary + "\n"

    def _generate_improvement_suggestions(self, test_results: List[Dict], safeguard_effectiveness: Dict[str, float]) -> str:
        suggestions = "Improvement Suggestions:\n"
        
        # Identify the least effective safeguard
        least_effective = min(safeguard_effectiveness, key=safeguard_effectiveness.get)
        suggestions += f"1. Focus on improving the {least_effective} safeguard, as it has the lowest effectiveness score.\n"
        
        # Identify the most common issue
        issue_counts = {}
        for result in test_results:
            for issue in result['issues']:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1
        most_common_issue = max(issue_counts, key=issue_counts.get)
        suggestions += f"2. Address the '{most_common_issue}' issue, as it was the most frequently occurring problem.\n"
        
        # General suggestion
        suggestions += "3. Review and refine the test scenario generation to ensure a diverse and challenging set of inputs.\n"
        
        return suggestions