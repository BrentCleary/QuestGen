from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Page:
    def __init__(self, data):
        self.id = data['id']
        self.page = data['page']
        self.query = data['query']
        self.image = data['image']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.story_id = data['story_id']
        

    @classmethod
    def begin_story(data):
        query = """
                INSERT INTO pages (id, page, query, image, text)
                VALUES (%(id)s, %(page)s, %(query)s, %(image)s, %(text)s);  
                """
        results = connectToMySQL(DATABASE).query_db(query ,data)
        return results