from DojoSurvey_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.create_at = data["created_at"]
        self.update_at = data["updated_at"]

# CLASS METHODS BELOW
    @classmethod
    def get_dojo(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        print(query)
        results = connectToMySQL("dojo_survey_schema").query_db(query)
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        print(query)
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

# STATIC METHODS BELOW

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid
