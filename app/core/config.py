from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    postgres_database_url: PostgresDsn

    class Config:
        env_file: str = ".env"


settings = Settings()
