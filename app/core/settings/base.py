from enum import Enum

from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings

class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.test
    database_url: PostgresDsn
    secret_key: SecretStr
    debug: bool

    class Config:
        env_file = ".env"
