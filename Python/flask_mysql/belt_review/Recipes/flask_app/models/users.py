from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
#from recipes import Recipes

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'recipes'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at =data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def new_user(cls,data):
        query = 'INSERT into users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)' 
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = 'select * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_email(cls,data):
        query = 'select * from users where email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])


    @staticmethod
    def validate_user(user):
        valid = True
        query = 'SELECT * from users WHERE email = %(email)s;'
        results = connectToMySQL('recipes').query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken!")
            valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('invalid Email')
            valid =False
        if len(user['first_name']) <= 2:
            flash ("First name must be at least three letters long")
            valid = False
        if len(user['last_name']) <=2:
            flash ('Last name must be three letters long')
            valid = False
        if len(user['password']) < 5:
            flash ('Password must be at least five characters')
            valid = False
        if user['password'] != user['confirm_password']:
            flash('Passwords must match')
            valid = False
        return valid
    
