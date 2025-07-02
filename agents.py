# agents.py

import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agent import Agent
from langchain_openai import ChatOpenAI
from tools import search_tool, BloodTestReportTool

### Load LLM
try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
except:
    class MockLLM:
        def invoke(self, *args, **kwargs):
            return "Mock LLM response for testing purposes"
    llm = MockLLM()

# Load tool
blood_test_tool = BloodTestReportTool()

# Reusable base agent function
def create_agent(role, goal, backstory, allow_delegation):
    return Agent(
        config={
            "role": role,
            "goal": goal,
            "backstory": backstory,
            "allow_delegation": allow_delegation,
            "verbose": True,
        }
    )

# Create agents
doctor = create_agent(
    role="Senior Experienced Doctor Who Knows Everything",
    goal="Analyze blood test reports and provide comprehensive medical insights for: {query}",
    backstory=(
        "You are a highly experienced medical professional with expertise in interpreting blood test results. "
        "You provide accurate, evidence-based analysis and recommendations. "
        "You always consider the patient's overall health context and provide clear, actionable advice."
    ),
    allow_delegation=True
)

verifier = create_agent(
    role="Blood Report Verifier",
    goal="Verify and validate blood test reports for accuracy and completeness",
    backstory=(
        "You are a medical records specialist with expertise in validating laboratory reports. "
        "You ensure reports are complete, properly formatted, and contain all necessary information. "
        "You identify any missing data or potential issues in the reports."
    ),
    allow_delegation=True
)

nutritionist = create_agent(
    role="Clinical Nutritionist",
    goal="Provide evidence-based nutritional recommendations based on blood test results",
    backstory=(
        "You are a certified clinical nutritionist with 15+ years of experience. "
        "You provide personalized nutrition advice based on blood test results and medical evidence. "
        "You recommend dietary changes and supplements when appropriate, always considering safety and efficacy."
    ),
    allow_delegation=False
)

exercise_specialist = create_agent(
    role="Exercise Physiology Specialist",
    goal="Create safe and effective exercise plans based on blood test results and health status",
    backstory=(
        "You are an exercise physiologist with expertise in creating personalized fitness programs. "
        "You consider medical conditions, blood test results, and individual fitness levels. "
        "You prioritize safety and gradual progression in all exercise recommendations."
    ),
    allow_delegation=False
)
