from flask import render_template, redirect, request, session
from DN_app import app
from DN_app.models.ninja import Ninja

@app.route("/")
def show_data():
    return render_template("main_dojo.html")