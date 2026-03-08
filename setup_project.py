import os

# ============================================================
# ファイル内容の定義
# ============================================================

files = {
    "matching_tool/requirements.txt": """\
Flask==3.0.0
python-dotenv==1.0.0
watchdog==4.0.0
openpyxl==3.1.2
""",

    "matching_tool/.env.example": """\
SECRET_KEY=your-secret-key-here
DATABASE_PATH=matching_tool.db
WATCH_FOLDER=watch_folder
DEBUG=True
""",

    "matching_tool/.gitignore": """\
__pycache__/
*.py[cod]
*.pyo
*.pyd
.env
venv/
.venv/
env/
*.db
*.sqlite3
.DS_Store
.vscode/
.idea/
dist/
build/
*.egg-info/
watch_folder/system_a/*.xlsx
watch_folder/system_b/*.xlsx
watch_folder/system_a/old/
watch_folder/system_b/old/
""",

    "matching_tool/config.py": """\
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-please-change")
    DATABASE_PATH = os.environ.get("DATABASE_PATH", "matching_tool.db")
    WATCH_FOLDER = os.environ.get("WATCH_FOLDER", "watch_folder")
    DEBUG = os.environ.get("DEBUG", "True") == "True"
""",

    "matching_tool/run.py": """\
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=5000)
""",

    "matching_tool/app/__init__.py": """\
from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
""",

    "matching_tool/app/routes/__init__.py": """\
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")
""",

    "matching_tool/app/models/__init__.py": """\
# Issue #3〜#7 にて各テーブルのモデルを追加予定
""",

    "matching_tool/app/services/__init__.py": """\
# Issue #8〜 にてビジネスロジックを追加予定
""",

    "matching_tool/tests/__init__.py": """\
# Issue #28〜#30 にてテストを追加予定
""",

    "matching_tool/app/templates/base.html": """\
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{% block title %}稟議突合チェックツール{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" />
</head>
<body>
  <header class="header">
    <h1>稟議突合チェックツール</h1>
  </header>

  <main class="main-content">
    {% block content %}{% endblock %}
  </main>

  <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
""",

    "matching_tool/app/templates/index.html": """\
{% extends "base.html" %}

{% block title %}稟議突合チェックツール - メイン{% endblock %}

{% block content %}
<p>環境構築完了 🎉 次のIssueで画面を実装していきます。</p>
{% endblock %}
""",

    "matching_tool/app/static/css/style.css": """\
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", sans-serif;
  font-size: 14px;
  color: #333;
  background-color: #f5f5f5;
}

.header {
  background-color: #2c3e50;
  color: #fff;
  padding: 12px 24px;
}

.header h1 {
  font-size: 18px;
  font-weight: bold;
}

.main-content {
  max-width: 1200px;
  margin: 24px auto;
  padding: 0 16px;
}
""",

    "matching_tool/app/static/js/main.js": """\
// Issue #16〜 にてフロントエンドロジックを追加予定
console.log("稟議突合チェックツール 起動完了");
""",

    "matching_tool/watch_folder/system_a/.gitkeep": "",
    "matching_tool/watch_folder/system_a/old/.gitkeep": "",
    "matching_tool/watch_folder/system_b/.gitkeep": "",
    "matching_tool/watch_folder/system_b/old/.gitkeep": "",
}

# ============================================================
# ファイルの作成処理
# ============================================================

for path, content in files.items():
    dir_path = os.path.dirname(path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 作成: {path}")

print("\n🎉 全ファイルの作成が完了しました！")