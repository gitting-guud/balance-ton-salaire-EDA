from pydantic import BaseSettings


class Settings(BaseSettings):
    TWITTER_API_KEY: str = "123"
    TWITTER_API_KEY_SECRET: str = "123"
    BEARER_TOKEN: str = "123"
    OUTPUTDIR: str = "123"

    class Config:
        env_file = "/home/alhouceine@ljnad.lajavaness.com/balance-ton-salaire-EDA/.env"


settings = Settings()
