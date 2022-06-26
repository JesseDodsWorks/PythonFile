
from flask import render_template, redirect, request, session
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/")
def register_login():
    return render_template ("login.html")

@app.route("/dashboard")
def dashboard():
    if not "logged_in" in session:
        return redirect ("/")

    return render_template ("dashboard.html", recipes_table = Recipe.get_all_recipes())


#### valid register > save user
@app.route("/register", methods=["POST"])
def create_user():  
    if not User.valid_register(request.form):
        return redirect ("/")

    hash_pw = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form['email'],
        "password" : hash_pw
    }

    user_id = User.save_user(data)

    session["logged_in"] = {
        "id" : user_id,
        "first_name" : data["first_name"],
        "email" : data["email"]
        }

    return redirect ("/dashboard")

#### valid login 
@app.route("/login", methods=["POST"])
def sign_in():
    if not User.valid_login(request.form):
        return redirect ("/")

    user = User.get_user(request.form["email"])
    session["logged_in"] = {
        "id" : user.id,
        "first_name" : user.first_name,
        "email" : user.email
        }

    return redirect ("/dashboard")

### logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect ("/")






























