import logging

from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    title: str = "Test FastAPI example application"
    secret_key: SecretStr
    database_url: PostgresDsn
    logging_level: int = logging.DEBUG
