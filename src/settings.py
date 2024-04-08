from dotenv import find_dotenv, load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    translator_url: str = Field(..., alias='TRANSLATOR_URL')
    trained_model_path: str = Field(..., alias='TRAINED_MODEL_PATH')


def get_settings() -> Settings:
    exists_dotenv = find_dotenv('.env', raise_error_if_not_found=False)
    if exists_dotenv:
        load_dotenv('.env')

    return Settings()
