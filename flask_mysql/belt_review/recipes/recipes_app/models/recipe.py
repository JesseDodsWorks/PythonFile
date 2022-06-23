from recipes_app.config.mysqlconnection import connectToMySQL
from recipes_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



class Recipes:
    def __init__(self, data):
        self.id = data["id"]















