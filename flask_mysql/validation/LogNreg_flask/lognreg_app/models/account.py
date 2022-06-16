from lognreg_app.config.mysqlconnection import connectToMySQL
from lognreg_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')



class User:
    db = "lognreg_schema"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# CLASS METHODS
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_email(cls,email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {"email" : email}
        result = connectToMySQL(cls.db).query_db(query,data)
        print(len(result))
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])


# STATIC METHODS
    @staticmethod
    def validate_reg(user):
        is_valid = True

        if not EMAIL_REGEX.match(user["email"]):
            is_valid = False
            flash("Invalid Email Address", "register") # CHANGE TO FLASH

        if user["firstpass"] == "" or user["secondpass"] == "":
            flash("Password field(s) can not be blank", "register")
            is_valid = False

        if user["firstpass"] != user["secondpass"]:
            flash("Passwords Do Not Match.", "register") # CHANGE TO FLASH
            is_valid=False

        query = "SELECT * FROM users WHERE email = %(email)s;"
        print(query)
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email Already Taken.", "register") # CHANGE TO FLASH
            is_valid=False

        return is_valid

    @staticmethod
    def validate_log(user):
        is_valid = True

        query = "SELECT * FROM users WHERE email = %(email)s;"
        print(query)
        results = connectToMySQL(User.db).query_db(query,user)

        if len(results) == 0:
            flash("No Account Found", "login") # CHANGE TO FLASH
            is_valid=False
            
        if len(results) == 1:
            row = User(results[0])
            if not bcrypt.check_password_hash(row.password,  user["password"]):
                flash("Passwords Do Not Match", "login") # CHANGE TO FLASH
                is_valid=False

        return is_valid




