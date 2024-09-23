from typing import Dict, List
from openai import OpenAI
from transformers import pipeline, AutoTokenizer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MockCompletions:
    def create(self, model, messages, max_tokens):
        # Simulate a response
        prompt = messages[0]['content']
        response = f"This is a mock response to: {prompt}"
        return type('obj', (object,), {
            'choices': [type('obj', (object,), {
                'message': type('obj', (object,), {
                    'content': response
                })
            })]
        })

class MockChat:
    def __init__(self):
        self.completions = MockCompletions()

class MockOpenAIModel:
    def __init__(self):
        self.chat = MockChat()

class MultiAIModelInterface:
    def __init__(self, models: List[str], use_mock=False):
        self.models = {}
        self.use_mock = use_mock
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key and not use_mock:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables")
        self.client = OpenAI(api_key=api_key) if not use_mock else MockOpenAIModel()
        for model in models:
            if model.startswith("gpt"):
                self.models[model] = self._setup_openai_model(model)
            else:
                self.models[model] = self._setup_huggingface_model(model)

    def _setup_openai_model(self, model_name: str):
        return lambda prompt: self.client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )

    def _setup_huggingface_model(self, model_name: str):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = pipeline(
            "text-generation",
            model=model_name,
            tokenizer=tokenizer,
            max_length=512,  # Increase max_length
            max_new_tokens=100,  # Set max_new_tokens
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1
        )
        return model

    def get_responses(self, input_data: Dict[str, str]) -> Dict[str, str]:
        responses = {}
        for model_name, model in self.models.items():
            if model_name.startswith("gpt"):
                response = model(input_data["content"])
                responses[model_name] = response.choices[0].message.content
            else:
                generated_text = model(input_data["content"], max_length=512, max_new_tokens=100)[0]["generated_text"]
                responses[model_name] = generated_text
        return responses

    def reset(self):
        # Reset model states if necessary
        pass