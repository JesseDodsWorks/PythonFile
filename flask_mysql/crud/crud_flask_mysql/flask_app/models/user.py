
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.create_at = data["create_at"]
        self.update_at = data["update_at"]

# this class method allows us to get all values in a row from our DB user_entry
    @classmethod
    def get_rows(cls):
        query = "SELECT * FROM users"   #users is the name of the table inside user_entry
        results = connectToMySQL("user_entry").query_db(query)
        print(results)

        users = []
        for user in results:
            users.append( cls(user) )
        return users

# this class method allows us to send info to our DB user_entry
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, create_at, update_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL("user_entry").query_db( query, data )

# class that SELECTS ONE user
    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        print(query)
        results = connectToMySQL("user_entry").query_db(query, data)
        print(results)
        return cls(results[0])

# edit(UPDATE) classmethod for the ONE user
    @classmethod
    def save_edit(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, update_at = NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL("user_entry").query_db(query, data)

# delete classmethod for a selected user
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        print(query)
        return connectToMySQL("user_entry").query_db(query, data)