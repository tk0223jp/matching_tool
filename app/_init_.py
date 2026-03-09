from flask import Flask
from config import Config
import sqlite3
import os
from flask import Flask, g
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Blueprint の登録
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

DATABASE = os.getenv("DATABASE_URL", "sqlite:///./database.db").replace("sqlite:///", "")

def get_db():
    """リクエストごとに DB 接続を取得する"""
    if "db" not in g:
        g.db = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    """リクエスト終了時に DB 接続を閉じる"""
    db = g.pop("db", None)
    if db is not None:
        db.close()