from flask import Blueprint, render_template

main = Blueprint("main", __name__)

# routes for app

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@main.route("/login")
def login():
    return render_template("login.html")


@main.route("/signup")
def signup():
    return render_template("signup.html")


@main.route("/about")
def about():
    return render_template("about.html")
