from helpers.config import get_settings, Settings
import os
import random
import string
from models import ProcessingEnum

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
    