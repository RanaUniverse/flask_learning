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


from my_modules.make_square_circle import make_square_circle_image


@app.route("/pillow1", methods=["POST"])
def pillow_1_submit():
    """
    This will execute when user will form fillup for the pillow
    part and then enter his data thsi is just for checking how
    i can conncect my html with python
    """
    print("Thanks")
    # print(request.form)

    # Below part is for Side Value Checking 🍌🍌🍌

    side = request.form.get("side")
    if not side:
        print("Side value has not come by the user")
        return f"You Must need to pass the side value which is IN first cell."

    if side.isdigit():
        side = int(side)
    else:
        return "You have not give good value, pls go back and enter int value"

    # upper part is for value checking, 🍌🍌🍌
    # Below part is for background color, 🍌🍌🍌

    bg_color = request.form.get("bg_color")
    if not bg_color:
        return "No Valid Tup of Int is get pls try again"
    try:
        bg_color = bg_color.strip("()")
        bg_color = bg_color.split(",")
        bg_color = map(int, bg_color)
        bg_color = tuple(bg_color)

        if len(bg_color) != 3:
            return f"RGB tuple must have exactly three values. but you gives, {len(bg_color)}<br> pla try again"

    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {str(e)}. Please provide valid RGB values (e.g., (255,255,255)). try again"

    # Upper part is for background color, 🍌🍌🍌
    # Below part is forcircle radius value 🍌🍌🍌

    radius = request.form.get("circle_radius")
    if not radius:
        return f"You Must pass the value of the circles's radius, try again"
    try:
        radius = int(radius)
        if radius < 1 or radius > 1000:
            return "The circle's radius must be between 1 and 1000., try again"
    except ValueError:
        return "The circle's radius must be a valid integer., try again"

    circle_fill = request.form.get("circle_fill")
    if not circle_fill:
        return "No Valid Tuple of Int is provided for Circle Fill Color"
    try:
        # Remove parentheses and split the string
        circle_fill = circle_fill.strip("()")
        circle_fill = circle_fill.split(",")
        circle_fill = map(int, circle_fill)
        circle_fill = tuple(circle_fill)

        # Check the length of the tuple
        if len(circle_fill) != 3:
            return f"RGB tuple must have exactly three values, but you provided {len(circle_fill)}."

    except Exception as e:
        print(f"Error: {e}")
        return (
            f"Error: {str(e)}. Please provide valid RGB values (e.g., (255,255,255))."
        )

    circle_outline = request.form.get("circle_outline")
    if not circle_outline:
        return "No Valid Tuple of Int is provided for Circle Outline Color"
    try:
        # Remove parentheses and split the string
        circle_outline = circle_outline.strip("()")
        circle_outline = circle_outline.split(",")
        circle_outline = map(int, circle_outline)
        circle_outline = tuple(circle_outline)

        # Check the length of the tuple
        if len(circle_outline) != 3:
            return f"RGB tuple must have exactly three values, but you provided {len(circle_outline)}."

    except Exception as e:
        print(f"Error: {e}")
        return (
            f"Error: {str(e)}. Please provide valid RGB values (e.g., (255,255,255))."
        )

    outline_width = request.form.get("outline_width")
    if not outline_width:
        return "Outline width is required., try again"
    try:
        outline_width = int(outline_width)
        if outline_width < 0:
            return "Outline width must be a non-negative integer., try again"
    except ValueError:
        return "Outline width must be a valid integer., try again"

    print(f"✅✅✅ Side: {side}")
    print(f"✅✅✅, BG Color, {bg_color}")
    print(f"✅✅✅, Radius: {radius}")
    print("✅✅✅, circle color", circle_fill)
    print("✅✅✅, outline color", circle_outline)
    print("✅✅✅ outline width", outline_width)

    im_location = make_square_circle_image(
        side=side,
        bg_color=bg_color,
        circle_radius=radius,
        circle_fill=circle_fill,
        circle_outline=circle_outline,
        outline_width=outline_width,
    )

    # return f"Image Form Submitted Successfully and processing has strted. Saved at {im_location}"
    return render_template(
        "image_generate.html",
        image_path_data=im_location,
        image_name="This is a pillow image",
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


@app.route("/image_checking")
def image_showing():
    print("A Image showing website has opening")
    return render_template("image_learning.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact_info():
    return render_template("contact.html")


# This will just show the page of input type checking page.
@app.route("/input_type_checking")
def input_type():
    print("Input Type Checking Functions are running")
    return render_template("input_type_checking.html")


@app.route("/input_type_learning", methods=["POST"])
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
