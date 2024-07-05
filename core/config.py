import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Aviator"
    PROJECT_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"
    DATABASE_URL: str = os.getenv("url")

settings = Settings()