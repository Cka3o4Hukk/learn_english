# from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_POST: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # @model_validator(mode="before") # "after"
    # def get_database_url(cls, v):
    #    v["DATABASE_URL"] = f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASS']}@{v['DB_PASS']}:{v['DB_POST']}/{v['DB_NAME']}"

    @property
    def DATEBASE_URL(self) -> str:  # noqa: N802
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_POST}/{self.DB_NAME}"


    class Config:
        env_file = ".env"

settings = Settings()
