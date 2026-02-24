import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for, flash
from sqlalchemy import Boolean, DateTime, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# --- SQLAlchemy setup ---
class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///todo.db")

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def init_db() -> None:
    Base.metadata.create_all(engine)

# --- Flask setup ---
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

@app.get("/")
def index():
    init_db()
    with SessionLocal() as db:
        todos = db.execute(select(Todo).order_by(Todo.created_at.desc())).scalars().all()
    return render_template("index.html", todos=todos)

@app.post("/todos")
def create_todo():
    title = (request.form.get("title") or "").strip()
    if not title:
        flash("内容が空です")
        return redirect(url_for("index"))

    with SessionLocal() as db:
        db.add(Todo(title=title))
        db.commit()
    return redirect(url_for("index"))

@app.post("/todos/<int:todo_id>/toggle")
def toggle_todo(todo_id: int):
    with SessionLocal() as db:
        todo = db.get(Todo, todo_id)
        if todo is None:
            flash("Todoが見つかりません")
            return redirect(url_for("index"))
        todo.done = not todo.done
        db.commit()
    return redirect(url_for("index"))

@app.post("/todos/<int:todo_id>/delete")
def delete_todo(todo_id: int):
    with SessionLocal() as db:
        todo = db.get(Todo, todo_id)
        if todo is None:
            flash("Todoが見つかりません")
            return redirect(url_for("index"))
        db.delete(todo)
        db.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)