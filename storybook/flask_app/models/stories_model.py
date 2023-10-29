from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Story:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def begin_story(data):
        query = """
                INSERT INTO stories (id, title)
                VALUES (%(id)s), "Your Story");  
                """
        results = connectToMySQL(DATABASE).query_db(query ,data)
        return results