"""
This file is help to calculate the mathematics
related logics in my html code 
"""

from flask import Blueprint, request


sum_blueprint = Blueprint("sum_str", __name__)


@sum_blueprint.route("/sum", methods=["POST"])
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
