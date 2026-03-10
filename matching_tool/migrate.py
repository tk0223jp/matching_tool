# migrate.py
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("DATABASE_URL", "sqlite:///./database.db").replace("sqlite:///", "")
MIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), "migrations")


def run_migrations():
    """migrations/ フォルダ内の .sql ファイルを順番に実行する"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # マイグレーション管理テーブルを作成
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_migrations (
            filename TEXT PRIMARY KEY,
            applied_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

    # 適用済みのマイグレーションを取得
    applied = {row[0] for row in cursor.execute("SELECT filename FROM schema_migrations")}

    # migrations/ フォルダの .sql ファイルをソート順に取得
    sql_files = sorted([
        f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql")
    ])

    for filename in sql_files:
        if filename in applied:
            print(f"[SKIP] {filename} (already applied)")
            continue

        filepath = os.path.join(MIGRATIONS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            sql = f.read()

        try:
            cursor.executescript(sql)
            cursor.execute(
                "INSERT INTO schema_migrations (filename) VALUES (?)", (filename,)
            )
            conn.commit()
            print(f"[OK]   {filename}")
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] {filename}: {e}")
            break

    conn.close()


if __name__ == "__main__":
    run_migrations()