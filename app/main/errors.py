from flask import render_template
from . import main

# for error custom handling

@main.app_errorhandler(404)
def not_found_error(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500
