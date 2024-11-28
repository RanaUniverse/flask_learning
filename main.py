"""
This is simple flask just in this main.py file
"""

from flask import Flask, render_template

app = Flask(__name__)

name = "Rana Universe"


from my_modules.flask_related.time_related import time_blueprint
from my_modules.flask_related.math_related import sum_blueprint
from my_modules.flask_related.image_processing_related import pillow_blueprint

from my_modules.flask_related.form_fillup_input_related import (
    input_type_checking_blueprint,
)
from my_modules.flask_related.form_fillup_input_related import input_learning_blueprint

from my_modules.flask_related.practise_files import (
    practise_submit_get_blueprint,
    practise_submit_post_blueprint,
)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(practise_submit_get_blueprint)
app.register_blueprint(practise_submit_post_blueprint)

app.register_blueprint(time_blueprint)
app.register_blueprint(sum_blueprint)
app.register_blueprint(pillow_blueprint)

app.register_blueprint(input_learning_blueprint)
app.register_blueprint(input_type_checking_blueprint)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
