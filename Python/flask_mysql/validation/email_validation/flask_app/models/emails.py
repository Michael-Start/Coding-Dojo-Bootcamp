
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_At']

    @classmethod
    def new_email(cls, data):
        query = 'INSERT INTO emails (email) VALUES (%(email)s);'
        return connectToMySQL('email_val').query_db(query,data)

    @classmethod
    def list(cls):
        query = 'SELECT * FROM emails'
        results = connectToMySQL('email_val').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails


    @staticmethod
    def validate_email(email):
        validate_email = True
        query = 'SELECT * from emails WHERE email = %(email)s;'
        results = connectToMySQL('email_val').query_db(query, email)
        if len(results) >= 1:
            flash("Email already taken!")
            validate_email = False
        if not EMAIL_REGEX.match(email['email']):
            flash('invalid Email')
            validate_email = False
        return validate_email

    @classmethod 
    def delete(cls, data):
        query = 'DELETE from emails where ID = %(id)s;'
        return connectToMySQL('email_val').query_db(query, data)