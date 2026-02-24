# Todo App (Flask + SQLAlchemy)

Flask と SQLAlchemy を使ったシンプルな Todo アプリです。

## Features
- Todo 一覧表示
- Todo 追加
- 完了/未完了の切り替え
- Todo 削除

## Tech Stack
- Python 3.12
- Flask
- SQLAlchemy
- SQLite

## Setup (Local)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# .env を作成（例）
cp .env.example .env

python app.py