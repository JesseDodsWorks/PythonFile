from recipes_app.config.mysqlconnection import connectToMySQL
from recipes_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class User:
    db = "users_recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s, NOW(), NOW());
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user(cls,email):
        query = """SELECT *
        FROM users
        WHERE email = %(email)s;
        """
        data = {"email" : email}
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])



    @staticmethod
    def valid_register(data):
        is_valid = True
        #current validation requires fields not be left blank
        if data["first_name"] == "":
            flash("first name is required", "register")
            is_valid = False
        if len(data["first_name"]) <=2:
            flash("first name needs to be longer than 2", "register")
            is_valid = False

        if data["last_name"] == "":
            flash("last name is required", "register")
            is_valid = False
        if len(data["last_name"]) <=2:
            flash("last name needs to be longer than 2", "register")
            is_valid = False

        if data["email"] == "":
            flash("email is required", "register")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("invalid email address - sample@email.com", "register")
            is_valid = False

        if data["password"] == "":
            flash("password is required", "register")
            is_valid = False
        if len(data["password"]) <7:
            flash("password needs to be 8 character or longer", "register")
            is_valid = False

        if data["confirm"] == "":
            flash("confirm is required", "register")
            is_valid = False
        if data["password"] != (data["confirm"]):
            flash("passwords do not match", "register")
            is_valid = False

        if is_valid == True:
            query = "SELECT * FROM users WHERE email = %(email)s;"
            print(query)
            results = connectToMySQL(User.db).query_db(query,data)
            if len(results) >= 1:
                flash("email is already been used.", "register")
                is_valid=False

        return is_valid

    @staticmethod
    def valid_login(data):
        is_valid = True
        #current validation requires fields not be left blank
        if data["email"] == "":
            flash("email is required", "sign_in")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("invalid email address - sample@email.com", "sign_in")
            is_valid = False

        if data["password"] == "":
            flash("password is required", "sign_in")
            is_valid = False
        if len(data["password"]) <7:
            flash("password needs to be 8 character or longer", "sign_in")
            is_valid = False
        
        if is_valid == True:
            query = "SELECT * FROM users WHERE email = %(email)s;"
            print(query)
            results = connectToMySQL(User.db).query_db(query,data)
            if len(results) <= 0:
                flash("no account has this email", "sign_in")
                is_valid=False

            if len(results) == 1:
                user = User(results[0])
                if not bcrypt.check_password_hash(user.password, data["password"]):
                    flash("password is incorrect", "sign_in")
                    is_valid=False

        return is_valid