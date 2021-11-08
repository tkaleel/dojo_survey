from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO surveys ( name, location, language, comments, created_at, updated_at ) VALUES ( %(name)s, %(location)s, %(language)s, %(comments)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('surveys_schema').query_db( query, data )
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM surveys WHERE id = %(id)s;"
        result = connectToMySQL('surveys_schema').query_db(query,data)
        return cls(result[0])
        
    @staticmethod
    def validate_survey(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(data['comments']) < 1:
            flash("Please don't leave the comments blank! We would love to hear from you.")
            is_valid = False
        return is_valid