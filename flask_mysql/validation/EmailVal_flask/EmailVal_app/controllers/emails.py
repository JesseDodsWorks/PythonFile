from flask import render_template, redirect, request
from EmailVal_app import app
from EmailVal_app.models.email import Email

# Showing Routes ############################
@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/show")
def show():
    return render_template ("show.html", email_table = Email.get_emails())

# Doing Routes ############################
@app.route("/checkemail", methods=["POST"])
def check_email():
    print(request.form)
    if not Email.valid_email(request.form):
        return redirect ("/")

    Email.save(request.form)
    return redirect ("/show")

@app.route("/delete/<int:id>")
def delete(id):
    data = {"id" : id}
    Email.delete_email(data)
    return redirect ("/show")