from DN_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.create_at = data["created_at"]
        self.update_at = data["updated_at"]


# CLASS METHODS BELOW
    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_ninjas").query_db(query)
        print(results)

        dojos = []
        for locations in results:
            dojos.append(cls(locations))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() );"
        return connectToMySQL("dojos_ninjas").query_db( query, data )

# ERRORS - TypeError: 'bool' object is not subscriptable
    @classmethod
    def select_one(cls, data):
        # query = "SELECT * FROM dojo WHERE id = %(id)s;"
        # print(query)
        # results = connectToMySQL("dojos_ninjas").query_db(query, data)
        return 

