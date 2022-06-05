
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def show_data():
    users = User.get_rows() #creates a value, get to the return from the get_all def in User.py
    print(users) #prints the returned information inside the users value
    return render_template("read.html", all_users = users)

@app.route("/create")
def create():
    return render_template("create.html") #pops the index.html page

@app.route("/add_user", methods=["POST"])
def add_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
# takes the information above and sends it the database. then redirects
    User.save(data)
    return redirect("/")

# select one user
@app.route("/select_one/<int:id>")
def select(id):
    data= {"id": id}
    return render_template ("show.html", user = User.select_one(data))

# Need to edit(UPDATE)
# grabbing the 
@app.route("/edit_one/<int:id>")
def edit(id):
    data ={"id":id}
    return render_template("edit.html", user=User.select_one(data))

@app.route("/update_edit", methods=["POST"])
def update():
    User.save_edit(request.form)
    return redirect("/")


# Need to delete(DELETE)
@app.route("/delete_user/<int:id>")
def delete(id):
    data ={"id":id}
    User.delete_user(data)
    return redirect("/")