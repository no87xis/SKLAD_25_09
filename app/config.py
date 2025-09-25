import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import validator, Field


class Settings(BaseSettings):
    # Database
    database_url: str = Field(
        default="sqlite:///./sirius.db",
        description="Database connection URL"
    )
    
    # Security
    secret_key: str = Field(
        default="dev-super-secret-key-32-characters-long-2024",
        min_length=32,
        description="Secret key for session encryption"
    )
    session_max_age: int = Field(
        default=86400,
        ge=300,
        le=604800,
        description="Session max age in seconds (5 min to 7 days)"
    )
    
    # Telegram notifications
    telegram_bot_token: Optional[str] = Field(
        default=None,
        description="Telegram bot token for notifications"
    )
    telegram_chat_id: Optional[str] = Field(
        default=None,
        description="Telegram chat ID for notifications"
    )
    
    # Email (optional)
    smtp_host: Optional[str] = Field(
        default=None,
        description="SMTP server host"
    )
    smtp_port: Optional[int] = Field(
        default=None,
        ge=1,
        le=65535,
        description="SMTP server port"
    )
    smtp_username: Optional[str] = Field(
        default=None,
        description="SMTP username"
    )
    smtp_password: Optional[str] = Field(
        default=None,
        description="SMTP password"
    )
    
    # Environment
    environment: str = Field(
        default="development",
        regex="^(development|staging|production)$",
        description="Application environment"
    )
    debug: bool = Field(
        default=True,
        description="Debug mode"
    )
    
    # Logging
    log_level: str = Field(
        default="INFO",
        regex="^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$",
        description="Logging level"
    )
    
    @validator('secret_key')
    def validate_secret_key(cls, v, values):
        environment = values.get('environment', 'development')
        if environment == "production" and v == "dev-super-secret-key-32-characters-long-2024":
            raise ValueError("SECRET_KEY must be changed in production")
        return v
    
    @validator('telegram_bot_token')
    def validate_telegram_token(cls, v):
        if v and not v.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
            raise ValueError("Invalid Telegram bot token format")
        return v

    class Config:
        env_file = "env.example"  # Используем env.example как шаблон
        case_sensitive = False
        env_file_encoding = 'utf-8'


# Используем только переменные окружения и значения по умолчанию
settings = Settings()
