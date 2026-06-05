from fastapi import APIRouter, UploadFile, Depends, status
from helpers.config import Settings, get_settings
import os
import aiofiles
from fastapi.responses import JSONResponse
from models import ResponseSignal
from controllers import DataController
import logging

logger = logging.getLogger("uvicorn.error")

api_route = APIRouter()


@api_route.post("/upload_file/{job_id}")
async def Upload_file(file: UploadFile,
                      job_id: str,
                      app_settings : Settings = Depends(get_settings)):
    
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
    
    new_file_path, file_id = data_controller.generate_unique_file_path(
        orig_file_name=file.filename,
        job_id=job_id)
    
    
    try:
        async with aiofiles.open(new_file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNCK_SIZE):
                await f.write(chunk)
     
    except Exception as e:
        logger.error(f"Error while uploading file {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
        
        
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id": file_id
        }
    )    