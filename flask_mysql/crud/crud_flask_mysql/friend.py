# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('user_entry').query_db(query)
        # Create an empty list to append our instances of users
        users = []# Iterate over the db results and create instances of users with cls.
        for friend in results:
            users.append( cls(friend) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_entry').query_db( query, data )
