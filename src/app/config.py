"""Camino configuration via environment variables."""

from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["settings"]


class Settings(BaseSettings):
    HTTP_PROXY: str
    CAMINO_ATTACH: SecretStr

    model_config = SettingsConfigDict(
        case_sensitive=True,
        validate_default=False,
        extra="ignore",
    )


settings = Settings()  # Singleton for settings
