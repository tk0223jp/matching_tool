# 稟議突合チェックツール

システムAの取引明細とシステムBの上限稟議額を突合し、超過をアラート表示するWebツールです。

## 技術スタック

- バックエンド: Python / Flask
- データベース: SQLite
- フロントエンド: HTML / CSS / JavaScript
- フォルダ監視: watchdog

## セットアップ手順

### 1. リポジトリのクローン

```bash
git clone <your-repo-url>
cd matching_tool
```

### 2. 仮想環境の作成・有効化

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

```bash
cp .env.example .env
# .env を編集して SECRET_KEY を変更してください
```

### 5. アプリの起動

```bash
python run.py
```

ブラウザで `http://localhost:5000` にアクセスして確認してください。

## フォルダ構成

| フォルダ | 用途 |
|---|---|
| `app/` | Flaskアプリ本体 |
| `app/routes/` | ルーティング |
| `app/models/` | DBモデル（Issue #3〜） |
| `app/services/` | ビジネスロジック（Issue #8〜） |
| `app/templates/` | HTMLテンプレート |
| `app/static/` | CSS / JS |
| `watch_folder/` | 自動取り込み用ウォッチフォルダ |
| `tests/` | テストコード（Issue #28〜） |