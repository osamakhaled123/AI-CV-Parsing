from helpers.config import get_settings, Settings
from fastapi import UploadFile
import os
import random
import string
from models import ProcessingEnum
import pdfplumber
import re
import io

class BaseController:
    def __init__(self):
        self.app_settings : Settings = get_settings()
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.assets_dir = os.path.join(self.base_dir, "assets")
        self.files_dir = os.path.join(self.assets_dir, "files")
        self.cvs_dir = os.path.join(self.assets_dir, "CVs")
        self.parsed_cvs_dir = os.path.join(self.assets_dir, "parsed_CVs")
        
        
    def generate_random_string(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, 
                                      k=ProcessingEnum.RANDOM_KEY_LEN.value))
    
    
    async def get_phone_number(self, file: UploadFile):
        phone_pattern = r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,6}'
         
        file_bytes = await file.read()
        
        await file.seek(0)
         
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text: # Ensure text isn't None
                    match = re.search(phone_pattern, text)
                    if match:
                        return match.group().strip()
            
        return self.generate_random_string()