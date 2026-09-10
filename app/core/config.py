from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field
from functools import lru_cache
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.getenv(".Env_FILE",".env"),extra="ignore")

    app_name : str = Field(...,alias="APP_NAME")
    environment : str = Field(...,alias="ENVIRONMENT")
    database_url : str = Field(...,alias="DATABASE_URL")
    prefix_app : str = Field(...,alias="PREFIX_APP")


@lru_cache
def get_settings() -> Settings:
    return Settings()