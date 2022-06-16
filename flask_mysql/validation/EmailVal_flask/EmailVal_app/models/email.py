
from EmailVal_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# CLASS METHODS
    @classmethod
    def save(cls,data):
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        print(query)
        return connectToMySQL('email_validation_schema').query_db(query,data)

    @classmethod
    def get_emails(cls):
        query = "SELECT * FROM email ORDER BY email.created_at DESC;"
        print(query)
        results = connectToMySQL("email_validation_schema").query_db(query)
        emails = []
        for rows in results:
            emails.append(cls(rows))
        return emails
        
    @classmethod
    def delete_email(cls,data):
        query = "DELETE FROM email WHERE id = %(id)s"
        print(query)
        return connectToMySQL("email_validation_schema").query_db(query, data)

# STATIC METHODS
    @staticmethod
    def valid_email(email):
        is_valid = True

        if not EMAIL_REGEX.match(email["email"]):
            is_valid = False
            flash("Invalid email address")

        if EMAIL_REGEX.match(email["email"]):
            flash("Email Valid")
            return is_valid
