## Importing libraries and environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# ✅ Web search tool (DuckDuckGo is free and requires no API key)
from langchain.tools import DuckDuckGoSearchRun

# ✅ For reading PDF blood reports
from langchain_community.document_loaders import PyPDFLoader

# Instantiate DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

## 🔬 Blood Test Report Reader Tool
class BloodTestReportTool:
    def __init__(self):
        self.read_data_tool = self._create_read_data_tool()
    
    def _create_read_data_tool(self):
        """Creates a callable PDF reading tool."""
        def read_data_tool(path='data/sample.pdf'):
            """Reads and returns content from the provided PDF file path.

            Args:
                path (str): Path to the blood test PDF report.

            Returns:
                str: Cleaned and concatenated text content of the PDF.
            """
            try:
                loader = PyPDFLoader(file_path=path)
                docs = loader.load()

                full_report = ""
                for doc in docs:
                    content = doc.page_content.replace("\n\n", "\n").strip()
                    full_report += content + "\n"

                return full_report.strip()
            except Exception as e:
                return f"Error reading PDF file: {str(e)}"
        
        return read_data_tool


## 🥗 Nutrition Analysis Tool (Placeholder)
class NutritionTool:
    def analyze_nutrition_tool(self, blood_report_data: str) -> str:
        """Analyzes nutrition-related insights from the report."""
        processed_data = blood_report_data.replace("  ", " ")
        # TODO: Implement logic for real analysis
        return "Nutrition analysis functionality to be implemented"


## 🏃 Exercise Planning Tool (Placeholder)
class ExerciseTool:
    def create_exercise_plan_tool(self, blood_report_data: str) -> str:
        """Creates a custom fitness plan based on blood test data."""
        # TODO: Implement logic for real planning
        return "Exercise planning functionality to be implemented"
