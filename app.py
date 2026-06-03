import json
from pathlib import Path

from flask import Flask, render_template, render_template_string, request


app = Flask(__name__)

REGISTRATIONS_PATH = Path(__file__).resolve().parent / "data" / "registrations.json"
REGISTRATION_FIELDS = (
    "name",
    "wechat",
    "occupation",
    "ai_experience",
    "learning_goal",
)

SUCCESS_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>报名成功 - AI Meetup Kit</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header class="site-header">
        <nav class="nav">
            <a class="brand" href="{{ url_for('index') }}">AI Meetup Kit</a>
            <div class="nav-links">
                <a href="{{ url_for('index') }}">首页</a>
                <a href="{{ url_for('agenda') }}">活动议程</a>
                <a href="{{ url_for('register') }}">我要报名</a>
                <a href="{{ url_for('codex') }}">Codex 教学</a>
            </div>
        </nav>
    </header>

    <main class="page">
        <section class="section narrow">
            <p class="eyebrow">Success</p>
            <h1>报名已提交</h1>
            <p class="lead">我们已经保存你的报名信息，活动前会再联系你确认细节。</p>
            <a class="button" href="{{ url_for('register') }}">返回报名页</a>
        </section>
    </main>
</body>
</html>
"""


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
        return render_template_string(SUCCESS_TEMPLATE)

    return render_template("register.html")


@app.route("/codex")
def codex():
    return render_template("codex.html")


if __name__ == "__main__":
    app.run(debug=True)
