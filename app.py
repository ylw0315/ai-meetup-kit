import json
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)

REGISTRATIONS_PATH = Path(__file__).resolve().parent / "data" / "registrations.json"
REGISTRATION_FIELDS = (
    "name",
    "wechat",
    "occupation",
    "ai_experience",
    "learning_goal",
)

def load_registrations():
    try:
        raw_data = REGISTRATIONS_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return []
    except (OSError, UnicodeDecodeError):
        return []

    if not raw_data:
        return []

    try:
        registrations = json.loads(raw_data)
    except (TypeError, json.JSONDecodeError):
        return []

    if isinstance(registrations, list):
        return registrations

    return []


def save_registration(registration):
    REGISTRATIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    registrations = load_registrations()
    registrations.append(registration)
    REGISTRATIONS_PATH.write_text(
        json.dumps(registrations, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/agenda")
def agenda():
    return render_template("agenda.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        registration = {
            field: (request.form.get(field) or "").strip()
            for field in REGISTRATION_FIELDS
        }
        save_registration(registration)
        return render_template("register.html", success=True)

    return render_template("register.html")


@app.route("/codex")
def codex():
    return render_template("codex.html")


if __name__ == "__main__":
    app.run(debug=True)
