import logging

from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool
    title: str = "Test FastAPI example application"
    secret_key: SecretStr
    database_url: PostgresDsn
    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = "test.env"
