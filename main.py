from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import asyncio

from crewai import Crew, Process

# Importing agents and tasks
from agents import doctor, verifier, nutritionist, exercise_specialist
from tasks import help_patients, nutrition_analysis, exercise_planning, verification

app = FastAPI(
    title="Blood Test Report Analyzer",
    description="An AI-powered API to analyze blood test PDFs and return medical insights",
    version="1.0.0"
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set specific allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze-report/")
async def analyze_blood_report(file: UploadFile = File(...), query: str = Form(...)):
    try:
        # Save uploaded PDF
        os.makedirs("data", exist_ok=True)
        file_path = f"data/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Create Crew with agents and tasks
        medical_crew = Crew(
            agents=[verifier, doctor, nutritionist, exercise_specialist],
            tasks=[verification, help_patients, nutrition_analysis, exercise_planning],
            process=Process.sequential,
            verbose=True
        )

        # Run the workflow with input context
        result = await medical_crew.kickoff(inputs={
            "query": query,
            "file_path": file_path
        })

        return JSONResponse(content={"status": "success", "result": result})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
