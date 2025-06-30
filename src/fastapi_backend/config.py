from pydantic import BaseSettings
import os
import dotenv

dotenv.load_dotenv()

class Settings(BaseSettings):
    REDIS_URL = os.getenv("REDIS_URL")
    MODEL_URL = os.getenv("MODEL_URL")

    class Config:
        env_file = ".env"

settings = Settings()
