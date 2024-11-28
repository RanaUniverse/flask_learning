"""
This will help me to checking and learning aobut different types
of data entry in the html form fillup section
"""

from flask import Blueprint, render_template, request


input_type_checking_blueprint = Blueprint("input_str", __name__)
input_learning_blueprint = Blueprint("input_learn_str", __name__)


# This will just show the page of input type checking page.
@input_type_checking_blueprint.route("/input_type_checking")
def input_type():
    print("Input Type Checking Functions are running")
    return render_template("input_type_checking.html")


@input_learning_blueprint.route("/input_type_learning", methods=["GET"])
def input_type_processing_get():

    text: str = (
        f"<h1>Hello This is not valid get request, you need to form fillup and then submit</h1>"
        "<h1></h1>"
        f'<h1><a href="/input_type_checking">Press Here to fillup the form</a></h1>'
    )
    return text


@input_learning_blueprint.route("/input_type_learning", methods=["POST"])
def input_type_processing():
    print(request.form)

    text_value = request.form.get("type_text")
    password_value = request.form.get("password")
    email_value = request.form.get("email")
    age_value = request.form.get("age")

    return render_template(
        "input_type_submitted.html",
        type_text_data=text_value,
        password_data=password_value,
        email_data=email_value,
        age_data=age_value,
    )
