from flask import render_template, redirect, request, session
from DN_app import app
from DN_app.models import ninja, dojo

@app.route("/create_ninja")
def create_ninja():
    return render_template("new_ninja.html", dojo_locations = dojo.Dojo.get_dojos())

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    data ={
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    ninja.Ninja.save(data)
    return redirect("/")