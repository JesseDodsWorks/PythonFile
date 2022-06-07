from DN_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.create_at = data["created_at"]
        self.update_at = data["updated_at"]
        self.students = []

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

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.students.append( Ninja(n) )
        return dojo

    