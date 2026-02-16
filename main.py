from flask import Flask, request, render_template, redirect, url_for
from pathlib import Path

app = Flask(__name__)


CONTENTS_FILE = Path("contents.txt")



def load_contents():
    loading_contents = CONTENTS_FILE.read_text()
    return loading_contents.splitlines()


# def save_contents():
#     saving_contents = CONTENTS_FILE.write_text()
#     return saving_contents


@app.get("/")
def index():
    contents = load_contents()
    return render_template("index.html", contents=contents)


@app.post("/save")
def save():
    raw_contents = request.form.get("contents")

    with open("contents.txt", "a") as f:
        f.write(raw_contents + "\n")

    return redirect(url_for("index"))


@app.post("/edit")
def edit():
    request.form.get("")



if __name__ == "__main__":
    app.run(debug=True)


