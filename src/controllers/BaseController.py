from helpers.config import get_settings, Settings
import os
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings : Settings = get_settings()
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.assets_dir = os.path.join(self.base_dir, "assets")
        self.files_dir = os.path.join(self.assets_dir, "files")
        self.cvs_dir = os.path.join(self.assets_dir, "CVs")
        self.parsed_cvs_dir = os.path.join(self.assets_dir, "parsed_CVs")
        
        
    def generate_random_string(self, length: int = 12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    