from recipes_app.config.mysqlconnection import connectToMySQL
from recipes_app import app
from recipes_app.models import user
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



class Recipe:
    db = "users_recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.date = data["date"]
        self.halfhour = data["halfhour"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.held_recipe = None


#######################################################
#                       save
#######################################################
    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, instruction, date, halfhour, user_id, created_at, updated_at)
        VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(halfhour)s, %(user_id)s, NOW(), NOW());
        """
        return connectToMySQL(cls.db).query_db(query, data) 
######################################################

#######################################################
#                   get "all"
#######################################################
    @classmethod
    def get_all_recipes(cls):
        query = """SELECT *
        FROM recipes
        JOIN users on recipes.user_id = users.id
        """
        result = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        if not result:
            return False
        for a_recipe in result:
            new_recipe = cls(a_recipe)
            a_recipe = {
                "id" : a_recipe["users.id"],
                "first_name" : a_recipe["first_name"],
                "last_name" : a_recipe["last_name"],
                "email" : a_recipe["email"],
                "password" : a_recipe["password"],
                "created_at" : a_recipe["users.created_at"],
                "updated_at" : a_recipe["users.updated_at"]
            }
            new_recipe.held_recipe = user.User(a_recipe)
            all_recipes.append(new_recipe)

        return all_recipes
######################################################

#######################################################
#                   get "one"
#######################################################
    @classmethod
    def get_a_recipe(cls,data):
        query = """SELECT *
        FROM recipes
        JOIN users on recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        main = cls(result[0])

        data = {
            "id" : result[0]["users.id"],
            "first_name" : result[0]["first_name"],
            "last_name" : result[0]["last_name"],
            "email" : result[0]["email"],
            "password" : result[0]["password"],
            "created_at" : result[0]["users.created_at"],
            "updated_at" : result[0]["users.updated_at"]
        }
        main.held_recipe = user.User(data)
        print(main)
        return main
#######################################################

#######################################################
#                      Update
#######################################################
    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes
        SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date = %(date)s, halfhour = %(halfhour)s, user_id = %(user_id)s
        WHERE recipes.id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
#######################################################

#######################################################
#                      delete
#######################################################
    @classmethod
    def delete_recipe(cls, data):
        query = """DELETE FROM recipes
        WHERE recipes.id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
#######################################################

#######################################################
#                 validate recipe
#######################################################
    @staticmethod
    def valid_recipe(data):
        is_valid = True
        
        if data["date"] == "":
            flash("date is required", "recipe")
            is_valid = False
        if data["name"] == "":
            flash("name is required", "recipe")
            is_valid = False
        if len(data["name"]) <=2:
            flash("recipe name is not long enough, more than 2", "recipe")
            is_valid = False
        
        if data["description"] == "":
            flash("description is required", "recipe")
            is_valid = False
        if len(data["description"]) <= 14:
            flash("recipe description needs a minimum of 15 characters", "recipe")
            is_valid = False
        
        if data["instruction"] == "":
            flash("instructions is required", "recipe")
            is_valid = False
        if len(data["instruction"]) <= 14:
            flash("recipe instruction needs a minimum of 15 characters", "recipe")
            is_valid = False

        # if everything is good till point, check if the correct amount of items was passed, halfhour will be missing if not clicked
        if is_valid == True:
            if not len(data) == 6:
                flash("Yes or No option is required", "recipe")
                is_valid = False

        return is_valid
#######################################################

















