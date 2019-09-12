from app import flask_app as app
from flask import request
import json
from datetime import datetime


@app.route("/heartbeat")
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Homework_Template",
            "datetime": f"{datetime.now()}"
        }
    )


@app.route("/sample_classifier", methods=['POST'])
def sample_classifier():
    form = request.form
    print(form)
    x = form.get("x")
    y = form.get("y")

    x = int(x)
    y = int(y)

    print(x)
    print(y)

    results = {
        "result": x + y
    }

    return json.dumps(results)


@app.before_first_request
def load_app():
    print("Loading App Before First Request")
