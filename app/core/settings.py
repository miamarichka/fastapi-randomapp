from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    RANDOM_BASE_URL: str = "https://random-data-api.com/api"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()
