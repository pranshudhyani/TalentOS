from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str = "TalentOS"

    VERSION: str = "1.0.0"

    ENV: str = "development"

    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str

    DATABASE_URL: str

    REDIS_URL: str

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()