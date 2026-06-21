from .BaseController import BaseController
import os
import json
from services.cv_extractor import extract_text
from services.prompt_builder import load_job_description, build_prompt
from services.llm_service import call_llm
from models import ResponseSignal, ProcessingEnum

class JobController(BaseController):
    def __init__(self):
        super().__init__()
        
    
    def get_files_path(self, job_id: str):
        file_dir = os.path.join(self.files_dir, job_id)
         
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        return file_dir   
    
    def get_cvs_path(self, job_id: str):
        cv_dir = os.path.join(
            self.cvs_dir, 
            job_id)
        
        if not os.path.exists(cv_dir):
            os.makedirs(cv_dir)
        
        return cv_dir
    
    def get_parsed_cvs_dir_path(self, job_id: str):
        parsed_cvs = os.path.join(
            self.parsed_cvs_dir, job_id
        )
        
        if not os.path.exists(parsed_cvs):
            os.makedirs(parsed_cvs)
            
        return parsed_cvs    
    
    
    def get_files_names(self, json_file:str):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            filenames = [objects_["filename"] 
                for objects_ in data]
        
            return filenames
        
    
    def parsing_CVs(self, UPLOAD_DIR: str, 
                    json_file: str):
        job_description = load_job_description()
        
        for file in os.listdir(UPLOAD_DIR):
        
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                filenames = self.get_files_names(json_file=json_file)
                if file[ProcessingEnum.RANDOM_KEY_LEN.value+1:] in filenames:
                    continue
            
            
            file_path = os.path.join(
                UPLOAD_DIR,
                file
            )
            cv_text = extract_text(file_path=file_path)

            prompt = build_prompt(
                cv_text=cv_text,
                job_description=job_description
            )

            llm_response = call_llm(prompt)

            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            data.append(llm_response)
            
            
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)    

        return {
            "success": True,
            "llm_response": ResponseSignal.CVS_PARSED_SUCCESS.value
    }