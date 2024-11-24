"""
This is simple flask just in this main.py file
"""

import datetime
from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)

name = "Rana Universe"


@app.route("/")
def hello():
    now_time_ist = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    )
    # Render the template with dynamic data
    return render_template("home.html", name=name, time=now_time_ist)


@app.route("/about")
def about():
    return f"This is the About page."


@app.route("/contact")
def contact_info():
    text = f"Hello i am {name.upper()} Please Mail me at: <br>RanaUniverse321@gmail.com"
    return text


if __name__ == "__main__":
    # app.run(debug=False)
    app.run(host="0.0.0.0", port=5000, debug=False)
