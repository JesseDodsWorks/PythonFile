from email import message
from flask import render_template, redirect, request, session
from lognreg_app import app
from lognreg_app.models.message import Message




# Showing Routes ############################


# Doing Routes ##############################

@app.route("/send_message", methods=["POST"])
def send_message():
    if not Message.validate_message(request.form):
        return redirect ("/show")

    data = {
        "sender_id" : session["logged_in"]["id"],
        "recipient_id" : request.form["selected_friend_id"],
        "message" : request.form["message"]
    }
    
    Message.send_save(data)

    return redirect("/show")


@app.route("/delete_message/<int:id>")
def delete_message(id):
    data ={"id": id}
    Message.delete(data)
    return redirect ("/show")













