from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class TestResult(Base):
    __tablename__ = 'test_results'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    scenario = Column(JSON)
    responses = Column(JSON)
    issues = Column(JSON)
    human_verification = Column(String)

engine = create_engine('sqlite:///ai_stress_test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_test_result(scenario, responses, issues, human_verification):
    session = Session()
    test_result = TestResult(
        scenario=scenario,
        responses=responses,
        issues=issues,
        human_verification=human_verification
    )
    session.add(test_result)
    session.commit()
    session.close()

def get_test_results():
    session = Session()
    results = session.query(TestResult).all()
    session.close()
    return [
        {
            "id": result.id,
            "timestamp": result.timestamp,
            "scenario": result.scenario,
            "responses": result.responses,
            "issues": result.issues,
            "human_verification": result.human_verification
        }
        for result in results
    ]