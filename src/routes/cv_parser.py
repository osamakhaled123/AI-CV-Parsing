from fastapi import APIRouter, HTTPException
from pathlib import Path
import os

from services.cv_extractor import extract_text
from services.prompt_builder import (
    load_job_description,
    build_prompt
)
from services.llm_service import call_llm

router = APIRouter(
    tags=["CV Parser"]
)

directory_path = os.path.dirname(os.getcwd())
UPLOAD_DIR = Path(directory_path) / "assests" / "CVs"


@router.post("/parse/{filename}")
async def parse_cv():
    
    if len(os.listdir(UPLOAD_DIR)) == 0:
        raise HTTPException(status_code=404, detail="Directory is empty")


    for file in os.listdir(UPLOAD_DIR):
        file_path = UPLOAD_DIR / filename
        cv_text = extract_text(str(file_path))

    job_description = load_job_description()

    prompt = build_prompt(
        cv_text=cv_text,
        job_description=job_description
    )

    llm_response = call_llm(prompt)

    return {
        "success": True,
        "llm_response": llm_response
    }