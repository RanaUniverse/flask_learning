# import datetime

# from flask import render_template


# from main import app, name


# # I just added the time here.
# @app.route("/time")
# def hello():
#     now_time_ist = datetime.datetime.now(
#         datetime.timezone(datetime.timedelta(hours=5, minutes=30))
#     )
#     return render_template("home.html", name=name, time=now_time_ist)


# time_related.py
from flask import Blueprint, render_template
import datetime


time_blueprint = Blueprint("time_blueprint_str", __name__)


@time_blueprint.route("/time")
def show_time():
    now_time_ist = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    )
    return render_template("time_now.html", time=now_time_ist, name_data="Rana Universe")
