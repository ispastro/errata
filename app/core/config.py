"""
Application Configuration
==========================
This file manages all configuration settings for the DocTutor AI backend.

KEY CONCEPTS YOU'LL LEARN:
1. Pydantic Settings - Type-safe configuration from environment variables
2. Environment Variables - Keeping secrets (API keys) out of code
3. Dependency Injection - How FastAPI accesses config throughout the app
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    HOW IT WORKS:
    - Reads from .env file automatically
    - Validates types (str, int, list, etc.)
    - Provides defaults for optional values
    - Raises errors if required values are missing
    """
    
    # ===========================================
    # APPLICATION SETTINGS
    # ===========================================
    app_name: str = "DocTutor AI Backend"
    app_version: str = "1.0.0"
    debug: bool = False  # Set to True during development
    
    # ===========================================
    # CORS SETTINGS (for Chrome Extension)
    # ===========================================
    # CORS = Cross-Origin Resource Sharing
    # Allows your Chrome Extension (running at chrome-extension://...)
    # to make requests to this FastAPI backend
    cors_origins: List[str] = [
        "chrome-extension://*",  # Allows any Chrome extension
        "http://localhost:3000",  # For testing in browser
    ]
    
    # ===========================================
    # DATABASE SETTINGS
    # ===========================================
    # SQLite database file path
    # For production, you'd use PostgreSQL, but SQLite is perfect for learning
    database_url: str = "sqlite:///./doctutor.db"
    
    # SQLModel/SQLAlchemy setting - shows SQL queries in console when True
    database_echo: bool = False
    
    # ===========================================
    # AI API SETTINGS
    # ===========================================
    # We'll support multiple AI providers
    # You can use OpenAI, Google Gemini, or others
    openai_api_key: str = ""  # Will be loaded from .env
    gemini_api_key: str = ""  # Will be loaded from .env
    
    # Which AI provider to use: "openai" or "gemini"
    ai_provider: str = "gemini"
    
    # AI model to use
    ai_model: str = "gemini-1.5-flash"  # Fast and cheap for learning
    
    # ===========================================
    # SECURITY SETTINGS
    # ===========================================
    # Secret key for signing JWT tokens (user authentication)
    secret_key: str = "your-secret-key-change-this-in-production"
    
    # ===========================================
    # PYDANTIC CONFIGURATION
    # ===========================================
    model_config = SettingsConfigDict(
        env_file=".env",  # Read from .env file
        env_file_encoding="utf-8",  # File encoding
        case_sensitive=False,  # Environment variables can be lowercase or uppercase
        extra="allow",  # Allow extra fields not defined in this class
    )


# ===========================================
# SINGLETON INSTANCE
# ===========================================
# Create a single instance of settings that will be used throughout the app
# This is called the "Singleton Pattern" - we only create this once
settings = Settings()


# ===========================================
# DEPENDENCY FUNCTION
# ===========================================
def get_settings() -> Settings:
    """
    FastAPI dependency function.
    
    This function can be used in route handlers to inject settings.
    
    Example usage in a route:
        @router.get("/")
        async def root(settings: Settings = Depends(get_settings)):
            return {"app_name": settings.app_name}
    """
    return settings
