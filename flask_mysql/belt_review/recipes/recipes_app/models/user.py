from recipes_app.config.mysqlconnection import connectToMySQL
from recipes_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
