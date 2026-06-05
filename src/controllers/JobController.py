from .BaseController import BaseController
import os

class JobController(BaseController):
    def __init__(self):
        super().__init__()
        
    
    def get_job_path(self, job_id: str):
        job_dir = os.path.join(self.files_dir, job_id)
         
        if not os.path.exists(job_dir):
            os.makedirs(job_dir)
        
        return job_dir   