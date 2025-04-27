from flask import (
    Blueprint,
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy

from src.models import User
from src import db

import os
import logging

logger = logging.getLogger(__name__)
views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html", user=current_user)


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         user = users.get(username)

#         if user and check_password_hash(user["password"], password):
#             session["username"] = username
#             flash("Login successful!")
#             return redirect(url_for("home"))
#         else:
#             flash("Invalid username or password!")

#     return render_template("login.html")


# @app.route("/logout")
# def logout():
#     session.pop("username", None)
#     flash("You have been logged out.")
#     return redirect(url_for("home"))


# @app.route("/reset_password", methods=["GET", "POST"])
# def reset_password():
#     if request.method == "POST":
#         username = request.form["username"]
#         new_password = request.form["new_password"]

#         if username in users:
#             users[username]["password"] = generate_password_hash(new_password)
#             flash("Password reset successful!")
#             return redirect(url_for("login"))
#         else:
#             flash("User not found!")

#     return render_template("reset_password.html")


@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]
        password2 = request.form["password2"]
        name = request.form["firstName"]

        user = User.query.filter_by(email=username).first()
        if user:
            flash("Username already exists!", category="error")
        elif password != password2:
            flash("Passwords do not match!", category="error")
        else:
            user = User(email=username, name=name, password=password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful! Please login.", category="success")

    return render_template("register.html", user=current_user)
