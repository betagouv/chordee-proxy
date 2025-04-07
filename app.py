from dotenv import load_dotenv
from flask import Flask, render_template, request, session
import json
import os
import requests

from extract_session import extract_session

load_dotenv()
application = Flask(__name__)
application.secret_key = os.environ["SECRET_KEY"]


@application.route("/", methods=["GET", "POST"])
def index():
    args = {}
    if request.method == "POST":
        if "pwsh" in request.form:
            cmd = request.form["pwsh"]
            cookie = extract_session(cmd)
            print(cookie)
            session["cookie"] = cookie
        elif "cookie" in request.form:
            session.pop("cookie", None)
        elif "hidden" in request.form:
            if request.form["hidden"] == "test":
                url = f"{os.environ['JIRA_ROOT']}/jira/rest/api/latest/issue/CMDBRB-229"
                # url = "https://api.github.com/repos/betagouv/aides-jeunes/branches/main"
                headers = {
                    "Cookie": f"JSESSIONID={session['cookie']}",
                }
                try:
                    response = requests.get(url, headers=headers, verify=False)
                    args["result"] = json.dumps(
                        {
                            "status_code": response.status_code,
                            "headers": dict(response.headers),
                            "body": response.json(),
                        },
                        indent=2,
                    )
                except Exception as e:
                    args["result"] = {"error": str(e)}

    if "cookie" in session:
        args["cookie"] = session["cookie"]
    return render_template("index.html", **args)
