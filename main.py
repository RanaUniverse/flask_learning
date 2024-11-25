"""
This is simple flask just in this main.py file
"""

import datetime
from pathlib import Path
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


@app.route("/sum", methods=["POST"])
def calculate_sum():
    try:
        num1 = int(request.form.get("num1", 0))
        num2 = int(request.form.get("num2", 0))

        total = num1 + num2
        result = f"<h1>The sum of {num1} and {num2} is: <br>{total}</h1>"
        bananas = f"<h2>{'🍌' * total}</h2>"

        return result + "<br>" + bananas

    except ValueError:
        return (
            "<h1>Invalid input! Please enter valid numbers.</h1><br>"
            "<h2>No Valid Bananas. You will not get!</h2>"
        )


@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)

    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    email = request.form.get("email")
    # image_path = "static/images/linux_logo.png"
    # image_path = "files/images/linux_logo.png"  # this not works
    image_path = Path("static") / "images" / "linux_logo.png"

    if not first_name:
        return "What is ur first name pls"

    if not email:
        return "Please give email id"

    return render_template(
        "fname_lname.html",
        first_name_data=first_name,
        last_name_data=last_name,
        email_id_data=email.upper(),
        image_path_data=image_path,
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact_info():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=False)
