
from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__) #Creates our app. it's an instance from our earlier python projects
app.secret_key = 'keep me secret, keep me safe'

@app.route("/")
def show_data():
    users = User.get_rows() #creates a value, get to the return from the get_all def in User.py
    print(users) #prints the returned information inside the users value
    return render_template("read.html", all_users = users)

@app.route("/create")
def create():
    return render_template("create.html") #pops the index.html page

# @app.route("/show")
# def show():
#     return render_template("show.html") #pops the index.html page

# @app.route("/edit")
# def edit():
#     return render_template("edit.html") #pops the index.html page



# REDIRECTS BELOW POINT

# allows us to add a user to the DB user_entry by pulling info from our form in index.html
# assigning them to a value in data, then passing the info AGAIN into the class method save
# in the User class inside user.py
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





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.