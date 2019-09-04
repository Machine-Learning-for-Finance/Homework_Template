from app import flask_app as app
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


@app.before_first_request
def load_app():
    print("Loading App Before First Request")
