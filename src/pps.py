from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.getenv("HASH")

# In-memory user store
users = {}


@app.route("/")
def home():
    return render_template("home.html", user=current_user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)

        if user and check_password_hash(user["password"], password):
            session["username"] = username
            flash("Login successful!")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password!")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        username = request.form["username"]
        new_password = request.form["new_password"]

        if username in users:
            users[username]["password"] = generate_password_hash(new_password)
            flash("Password reset successful!")
            return redirect(url_for("login"))
        else:
            flash("User not found!")

    return render_template("reset_password.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]
        password2 = request.form["password2"]
        name = request.form["firstName"]

        if username in users:
            flash("Username already exists!", category="error")
        elif password != password2:
            flash("Passwords do not match!", category="error")
        else:
            users[username] = {"password": generate_password_hash(password), "name": name}
            flash("Registration successful! Please login.", category="success")

    return render_template("register.html", user=current_user)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
