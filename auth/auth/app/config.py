from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
    secret_key: str
    algorithm: str


@lru_cache()
def get_settings():
    return Settings()
