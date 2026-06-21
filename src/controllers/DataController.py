from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os
from .JobController import JobController

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value
    

    def get_clean_file_name(self, orig_file_name: str):
        
        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name        
        
    async def generate_unique_file_path(self, file: UploadFile, job_id: str):
        job_controller = JobController()
        job_path = job_controller.get_files_path(job_id=job_id)
        
        cleaned_file_name = self.get_clean_file_name(orig_file_name=file.filename)
        
        random_key = await self.get_phone_number(file=file)
        
        new_file_name = random_key + "_" + cleaned_file_name
        
        new_file_path = os.path.join(
            job_path,
            random_key + "_" + cleaned_file_name
        )
        
        return new_file_path, new_file_name 