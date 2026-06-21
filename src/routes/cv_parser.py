from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import os
from controllers import JobController
from models import ResponseSignal
import json

router = APIRouter(
    tags=["CV Parser"]
)

@router.post("/parse/{job_id}")
def parse_cv(job_id: str):
    
    job_controller = JobController()
    
    parsed_cvs_dir_path = job_controller.get_parsed_cvs_dir_path(job_id=job_id)
    
    json_file = os.path.join(
        parsed_cvs_dir_path,
        "parsed_cvs.json"
    )
    
    if not os.path.exists(json_file):
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump([], f)  # creates an empty JSON array
    
    
    UPLOAD_DIR = job_controller.get_files_path(job_id=job_id)
    if len(os.listdir(UPLOAD_DIR)) == 0:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal":ResponseSignal.NO_CVS_FOUND.value
            }
        )

    return job_controller.parsing_CVs(UPLOAD_DIR=UPLOAD_DIR, 
                               json_file=json_file)
    return {
        "success": True,
        "llm_response": ResponseSignal.CVS_PARSED_SUCCESS.value
    }