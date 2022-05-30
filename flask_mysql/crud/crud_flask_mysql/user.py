
from mysqlconnection import connectToMySQL

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
            users.append( User(user) )
        return users

# this class method allows us to send info to our DB user_entry
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, create_at, update_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL("user_entry").query_db( query, data )