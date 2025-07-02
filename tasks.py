# tasks.py

from crewai import Task
from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import BloodTestReportTool

# Reuse the same instance for tool efficiency
blood_tool = BloodTestReportTool().read_data_tool

# Task 1: Doctor - Analyze blood test report
help_patients = Task(
    description=(
        "Analyze the blood test report and provide comprehensive medical insights for the user's query: {query}. "
        "Read the PDF file carefully and provide accurate, evidence-based analysis. "
        "Identify any abnormal values, explain their significance, and provide actionable recommendations. "
        "Consider the patient's overall health context and provide clear, professional medical advice."
    ),
    expected_output=(
        "Provide a comprehensive blood test analysis including:\n"
        "- Summary of key findings\n"
        "- Identification of abnormal values with explanations\n"
        "- Medical significance of results\n"
        "- Recommendations for follow-up or lifestyle changes\n"
        "- Any concerning values that require medical attention\n"
        "- Professional, evidence-based advice"
    ),
    agent=doctor,
    tools=[blood_tool],
    async_execution=False,
)

# Task 2: Nutritionist - Analyze nutrition recommendations
nutrition_analysis = Task(
    description=(
        "Analyze the blood test results and provide evidence-based nutritional recommendations. "
        "Focus on values that may indicate nutritional deficiencies or dietary needs. "
        "User query: {query} - provide personalized nutrition advice based on the blood test results."
    ),
    expected_output=(
        "Provide detailed nutrition recommendations:\n"
        "- Analysis of blood values related to nutrition\n"
        "- Identification of potential nutritional deficiencies\n"
        "- Dietary recommendations based on results\n"
        "- Supplement suggestions when appropriate\n"
        "- Foods to include or avoid\n"
        "- Evidence-based nutritional advice"
    ),
    agent=nutritionist,
    tools=[blood_tool],
    async_execution=False,
)

# Task 3: Exercise Specialist - Recommend exercise plan
exercise_planning = Task(
    description=(
        "Create a safe and effective exercise plan based on the blood test results and health status. "
        "Consider any medical conditions or limitations indicated by the blood work. "
        "User query: {query} - provide personalized exercise recommendations."
    ),
    expected_output=(
        "Create a comprehensive exercise plan:\n"
        "- Analysis of blood values affecting exercise capacity\n"
        "- Safe exercise recommendations based on health status\n"
        "- Progressive exercise program\n"
        "- Considerations for any medical conditions\n"
        "- Safety guidelines and precautions\n"
        "- Realistic fitness goals and timelines"
    ),
    agent=exercise_specialist,
    tools=[blood_tool],
    async_execution=False,
)

# Task 4: Verifier - Validate blood report
verification = Task(
    description=(
        "Verify the uploaded document is a valid blood test report and check for completeness. "
        "Ensure all necessary information is present and the report is properly formatted."
    ),
    expected_output=(
        "Provide verification results:\n"
        "- Confirmation that the document is a blood test report\n"
        "- Assessment of report completeness\n"
        "- Identification of any missing information\n"
        "- Quality assessment of the report\n"
        "- Recommendations if additional tests are needed"
    ),
    agent=verifier,
    tools=[blood_tool],
    async_execution=False,
)
