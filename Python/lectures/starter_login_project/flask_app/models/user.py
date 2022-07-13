from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
# from flask_app.models import ???
from flask import flash
from flask_app import app # Might need to import the app in certain cases
import re
#Get email_regex line
class User:
    db_name = "users_lecture" # Replace this with the name of your schema name

    def __init__(self,data): # data is a DICTIONARY
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # self.recipes = [] # Empty list holding many items for this user, e.g. Recipes; add as many attributes as needed

    @staticmethod
    def validate_user(form_data):
        is_valid = True #assume it's all good
        #check each field individually
        if len(form_data['first_name'])<3:
            is_valid = False 
            flash('First name must be 3 or more characters')
        if len(form_data['last_name'] <3):
            is_valid = False 
            flash('Last name must be 3 or more characters')
        if not EMAIL_REGEX.match(form_data['email']): #check format of email
            is_valid = False
            flash("Email is not correct format")
            #check to see if email is already taken
        if len(form_data(['password'])) < 8
        is_valid = False
        flash('Password must be 8 or more characters')
        if form_data['password'] != form_data['confirm_password']
            is_valid = False
            flash('Passwords must match')
        return is_valid
        
        pass