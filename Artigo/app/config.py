from dotenv import load_dotenv
from os import environ

load_dotenv()


class Settings:
    def __init__(self):
        self.database_url = environ.get("DATABASE_URL")


settings = Settings()
