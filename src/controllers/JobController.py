from .BaseController import BaseController
import os

class JobController(BaseController):
    def __init__(self):
        super().__init__()
        
    
    def get_files_path(self, job_id: str):
        file_dir = os.path.join(self.files_dir, job_id)
         
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        return file_dir   
    
    def get_cvs_path(self, job_id: str):
        cv_dir = os.path.join(self.cvs_dir, job_id)
        
        if not os.path.exists(cv_dir):
            os.makedirs(cv_dir)
        
        return cv_dir