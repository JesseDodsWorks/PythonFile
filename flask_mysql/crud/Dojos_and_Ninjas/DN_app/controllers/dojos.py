from flask import render_template, redirect, request, session
from DN_app import app
from DN_app.models.dojo import Dojo

@app.route("/")
def show_dojos():
    dojo_locations = Dojo.get_dojos()
    print(dojo_locations)
    return render_template("main_dojo.html", dojo_locations = dojo_locations)


@app.route("/add_dojo", methods=["POST"])
def add_dojo():
    data ={
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect("/")

@app.route("/select_dojo")
def select_dojo():
    return render_template ("selected_dojo.html")