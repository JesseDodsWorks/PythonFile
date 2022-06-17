from lognreg_app.config.mysqlconnection import connectToMySQL
from lognreg_app import app
from flask import flash

class Message:
    db = "added_messages_schema"
    def __init__(self,data):
        self.id = data["id"]
        self.message = data["message"]
        self.sender_id = data["sender_id"]
        self.recipient_id = data["recipient_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# CLASS METHODS ##################################

    @classmethod
    def send_save(cls,data):
        query = "INSERT INTO messages (message, sender_id, recipient_id, created_at, updated_at) VALUES (%(message)s,%(sender_id)s,%(recipient_id)s, NOW(), NOW());"
        print(query)
        return connectToMySQL(cls.db).query_db(query, data)





# STATIC METHODS ##################################






