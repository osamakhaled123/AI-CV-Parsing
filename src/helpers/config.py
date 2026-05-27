from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME : str
    API_KEY : str
    OPENROUTER_MODEL : str
    OPENROUTER_BASE_URL : str
    
    FILE_DEFAULT_CHUNCK_SIZE: int
    
    
    class Config:
        env_file=".env"
        
def get_settings():
    return Settings()        