from flask import render_template, redirect, session
from recipes_app.models.recipe import Recipes
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)