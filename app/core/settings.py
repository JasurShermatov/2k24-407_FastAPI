from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # PROJECT INFO
    PROJECT_NAME: str = 'PDP`s Hotel'
    PROJECT_DESCRIPTION: str = 'This is learning project'
    PROJECT_VERSION: str = '0.0.1'

    # POSTGRES CREDENTIALS
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    model_config = SettingsConfigDict(env_file='.env')


@cache
def get_settings() -> Settings:
    return Settings()
