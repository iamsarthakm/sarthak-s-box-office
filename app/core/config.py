import os
from pathlib import Path


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./box_office.db")
    DATABASE_PATH = Path("./box_office.db")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
