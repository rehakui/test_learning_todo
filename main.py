# from flask import Flask, request, render_template, redirect, url_for
# from pathlib import Path
#
# app = Flask(__name__)
#
#
# CONTENTS_FILE = Path("./test_learning_todo/contents.txt")
#
#
#
# def load_contents():
#     loading_contents = CONTENTS_FILE.read_text()
#     # リストに入れてる
#     # return [line for line in loading_contents.splitlines()]
#     return loading_contents.splitlines()
#
#
# def save_contents(lines):
#     # saving_contents = CONTENTS_FILE.write_text()
#     CONTENTS_FILE.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
#     # return saving_contents
#
#
# @app.get("/")
# def index():
#     contents = load_contents()
#     return render_template("index.html", contents=contents)
#
#
# @app.post("/save")
# def save():
#     raw_contents = request.form.get("contents")
#
#     with open(CONTENTS_FILE, "a") as f:
#         f.write(raw_contents + "\n")
#
#     return redirect(url_for("index"))
#
#
# @app.get("/edit/<int:idx>")
# def edit_page(idx: int):
#     lines = load_contents()
#
#     return render_template("edit.html", idx=idx, value=lines[idx])
#
#
# @app.post("/edit")
# def edit_save():
#     idx = int(request.form["idx"])
#     new_text = (request.form.get("new_text") or "").strip()
#
#     lines = load_contents()
#
#     lines[idx] = new_text
#     save_contents(lines)
#     return redirect(url_for("index"))
#
#
#
# @app.post("/delete")
# def delete():
#     idx_str = request.form.get("idx")
#
#     idx = int(idx_str)
#     lines = load_contents()
#
#     del lines[idx]
#     save_contents(lines)
#     return redirect(url_for("index"))
#
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#
