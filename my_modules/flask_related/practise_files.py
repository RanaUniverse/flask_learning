"""
these are some practise files related to some submisiion of form
and so on
"""

from pathlib import Path

from flask import render_template, Blueprint, request


practise_submit_get_blueprint = Blueprint("submit_practise", __name__)
practise_submit_post_blueprint = Blueprint("submit_post", __name__)


@practise_submit_get_blueprint.route("/practise_submit", methods=["GET"])
def submit_get():
    return '<h2>&quot;Please visit the homepage to fill out the form!&quot;</h2><a href="/">Go To haomepage</a>'


@practise_submit_post_blueprint.route("/practise_submit", methods=["POST"])
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
