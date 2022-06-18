
from flask import render_template, redirect, request, session
from lognreg_app import app
from lognreg_app.models.account import User
from lognreg_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# Showing Routes ############################
@app.route("/")
def index():
    return render_template ("register.html")

@app.route("/show")
def show():
    if not "logged_in" in session:
        return redirect ("/")
    
    return render_template ("show.html",
    friends= User.get_friends(session["logged_in"]["id"]),
    messages = Message.get_messages(session["logged_in"]["id"]), 
    my_messages = Message.user_sent_messages(session["logged_in"]["id"]))


# Doing Routes ##############################

            ###################### validate_register #########################
@app.route("/validate_register", methods=["POST"])
def validate_register():
    if not User.validate_reg(request.form):
        return redirect ("/")
    
    # Hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['firstpass'])

    # put the pw_hash into the data dictionary
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form['email'],
        "password" : pw_hash
    }

    user_id = User.save(data)

    session["logged_in"] = {
        "id" : user_id,
        "first_name" : data["first_name"],
        "email" : data["email"]
        }

    return redirect ("/show")

            ###################### validate_login #########################
@app.route("/validate_login", methods=["POST"])
def validate_log():

    if not User.validate_log(request.form):
        return redirect ("/")
    
    user = User.get_by_email(request.form["email"])

    session["logged_in"] = {
        "id" : user.id,
        "first_name" : user.first_name,
        "email" : user.email
        }

    return redirect ("/show")


            ###################### clear_session #########################
@app.route("/clear_session")
def clear_route():
    session.clear()
    return redirect ("/")







