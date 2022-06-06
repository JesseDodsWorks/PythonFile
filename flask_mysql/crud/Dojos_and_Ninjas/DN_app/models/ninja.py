from DN_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.create_at = data["created_at"]
        self.update_at = data["updated_at"]
        self.dojo_id = data["dojo.id"]

# CLASS METHODS BELOW

    