from DN_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.create_at = data["created_at"]
        self.update_at = data["updated_at"]

# CLASS METHODS BELOW

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW() );"
        print(query)
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        print (results)
        return results