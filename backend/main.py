from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import asyncio
from datetime import datetime
from advanced_scenario_generator import AdvancedTestScenarioGenerator
from multi_ai_model_interface import MultiAIModelInterface
from response_analyzer import ResponseAnalyzer
from safeguard_evaluator import SafeguardEvaluator
from report_generator import ReportGenerator
from database import save_test_result, get_test_results

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TestResult(BaseModel):
    id: int
    timestamp: str
    scenario: Dict[str, str]
    responses: Dict[str, str]
    issues: Dict[str, List[str]]
    human_verification: str

class SafeguardEffectiveness(BaseModel):
    content_filtering: float
    ethical_reasoning: float
    consistency_checks: float
    uncertainty_handling: float

class TestRequest(BaseModel):
    scenario_type: str
    content: str

@app.get("/api/test-results", response_model=List[TestResult])
async def get_test_results_api():
    results = await asyncio.to_thread(get_test_results)
    # Convert datetime objects to ISO format strings
    for result in results:
        result['timestamp'] = result['timestamp'].isoformat()
    return results

@app.get("/api/safeguard-effectiveness", response_model=SafeguardEffectiveness)
async def get_safeguard_effectiveness():
    effectiveness = await asyncio.to_thread(SafeguardEvaluator().get_latest_effectiveness)
    return effectiveness

@app.post("/api/run-test")
async def run_test(test_request: TestRequest, background_tasks: BackgroundTasks):
    scenario = {
        "type": test_request.scenario_type,
        "content": test_request.content
    }
    
    background_tasks.add_task(process_test, scenario)
    
    return {"status": "Test started", "message": "The test is being processed in the background."}

async def process_test(scenario: Dict[str, str]):
    generator = AdvancedTestScenarioGenerator()
    ai_models = MultiAIModelInterface(["gpt-3.5-turbo", "bert-base-uncased"])
    analyzer = ResponseAnalyzer()
    evaluator = SafeguardEvaluator()
    
    responses = await asyncio.to_thread(ai_models.get_responses, scenario)
    issues = analyzer.analyze_responses(scenario, responses)
    
    test_result = {
        "scenario": scenario,
        "responses": responses,
        "issues": issues,
        "human_verification": "Pending"
    }
    
    await asyncio.to_thread(save_test_result, **test_result)

@app.post("/api/human-verification/{test_id}")
async def submit_human_verification(test_id: int, verification: Dict[str, str]):
    # Implement logic to save human verification
    # This might involve updating the database
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)