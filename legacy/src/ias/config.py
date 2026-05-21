from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    """
    Centralized configuration for the Intelligent Audio Scriber (IAS).
    Uses Pydantic V2 for validation and fail-fast principles.
    """
    
    # App Settings
    APP_NAME: str = "Intelligent Audio Scriber"
    DEBUG: bool = False
    
    # Storage Settings
    STORAGE_PATH: str = Field(default="./data", description="Base path for storing audio and processed data")
    OBSIDIAN_VAULT_PATH: Optional[str] = Field(default=None, description="Path to the Obsidian vault for knowledge compilation")
    
    # Model Settings (Local-First)
    WHISPER_MODEL: str = Field(default="base", description="Local Whisper model size to use")
    LLM_MODEL: str = Field(default="llama3", description="Local LLM model identifier (e.g., for Ollama)")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

# Singleton instance for the system
settings = Settings()
