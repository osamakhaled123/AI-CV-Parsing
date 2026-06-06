from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import os
from services.cv_extractor import extract_text
from services.prompt_builder import load_job_description, build_prompt
from services.llm_service import call_llm
from controllers import JobController
from models import ResponseSignal

router = APIRouter(
    tags=["CV Parser"]
)

@router.post("/parse/{job_id}")
async def parse_cv(job_id: str):
    
    job_controller = JobController()
    UPLOAD_DIR = job_controller.get_files_path(job_id=job_id)
    if len(os.listdir(UPLOAD_DIR)) == 0:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal":ResponseSignal.NO_CVS_FOUND.value
            }
        )

    CVs_path = os.path.join(
        UPLOAD_DIR,
        job_id
    )
    
    job_description = load_job_description()

    for file in os.listdir(UPLOAD_DIR):
        
        cv_text = extract_text(str(CVs_path))

    prompt = build_prompt(
        cv_text=cv_text,
        job_description=job_description
    )

    llm_response = call_llm(prompt)

    return {
        "success": True,
        "llm_response": llm_response
    }