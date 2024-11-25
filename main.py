"""
This is simple flask just in this main.py file
"""

import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

name = "Rana Universe"


# I just added the time here.
@app.route("/time")
def hello():
    now_time_ist = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    )
    return render_template("home.html", name=name, time=now_time_ist)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)
    
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    email = request.form.get("email")

    if not first_name:
        return "What is ur first name pls"
    
    if not email:
        return "Please give email id"
    
    return render_template(
        "fname_lname.html",
        first_name_data=first_name,
        last_name_data=last_name,
        email_id_data = email.upper()
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact_info():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=False)
