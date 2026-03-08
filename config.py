import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-please-change")
    DATABASE_PATH = os.environ.get("DATABASE_PATH", "matching_tool.db")
    WATCH_FOLDER = os.environ.get("WATCH_FOLDER", "watch_folder")
    DEBUG = os.environ.get("DEBUG", "True") == "True"