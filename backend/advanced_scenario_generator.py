import random
from typing import List, Dict
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class AdvancedTestScenarioGenerator:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.scenario_types = [
            "adversarial_questions",
            "misleading_information",
            "ethical_dilemmas",
            "complex_queries"
        ]

    def generate_scenario(self) -> Dict[str, str]:
        scenario_type = random.choice(self.scenario_types)
        prompt = self._get_prompt(scenario_type)
        
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
        
        scenario = self.tokenizer.decode(output[0], skip_special_tokens=True)
        
        return {
            "type": scenario_type,
            "content": scenario
        }

    def _get_prompt(self, scenario_type: str) -> str:
        prompts = {
            "adversarial_questions": "Generate a challenging question that might confuse an AI:",
            "misleading_information": "Create a statement with subtle misinformation:",
            "ethical_dilemmas": "Describe an ethical dilemma with no clear right answer:",
            "complex_queries": "Formulate a complex query requiring multi-step reasoning:"
        }
        return prompts[scenario_type]

    def generate_test_set(self, num_scenarios: int) -> List[Dict[str, str]]:
        return [self.generate_scenario() for _ in range(num_scenarios)]