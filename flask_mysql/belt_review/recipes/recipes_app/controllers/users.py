from flask import render_template, redirect, session
from recipes_app.models.user import User
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/")
def register_login():
    return render_template ("login.html")
































