from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:844622@localhost:5432/ogurets"

    class Config:
        env_file = ".env"

settings = Settings()
