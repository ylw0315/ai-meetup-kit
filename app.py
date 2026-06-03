from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/agenda")
def agenda():
    return render_template("agenda.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/codex")
def codex():
    return render_template("codex.html")


if __name__ == "__main__":
    app.run(debug=True)
