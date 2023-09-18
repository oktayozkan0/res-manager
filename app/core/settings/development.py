import logging

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    title: str = "Dev FastAPI example application"
    logging_level: int = logging.DEBUG
