from fastapi import APIRouter, UploadFile, Depends
from helpers.config import Settings, get_settings
import os
import aiofiles
from fastapi.responses import JSONResponse

api_route = APIRouter()


@api_route.post("/upload_file")
async def Upload_file(file: UploadFile, app_settings : Settings = Depends(get_settings)):
    
    file_name = file.filename
    
    directory_path = os.path.dirname(os.getcwd())
    file_path = os.path.join(directory_path+"/assests/CVs", file_name)
    
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNCK_SIZE):
                await f.write(chunk)
                
    except Exception as e:
        return JSONResponse(
            status_code = 400,
            content={
                "signal": "File Uploaded Unsuccessfully"
            }
        )        
    
    return JSONResponse(
        status_code=200,
        content={
            "file_ID":file_name
        }
    )