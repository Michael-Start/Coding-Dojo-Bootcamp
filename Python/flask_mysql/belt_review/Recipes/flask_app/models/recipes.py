
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.users import User

class Recipe:
    db = 'recipes'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.time = data['time']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.user = User.get_by_id({'id':self.users_id})

    @staticmethod
    def validate_recipe(data):
        valid = True
        if  len(data) >= 1:
            flash('Recipe already uploaded')
            valid = False
        if  len(data['name']) < 2:
            flash('Name must be longer than 2 characters')
            valid = False
        if  len(data['description']) <3:
            flash ('Description must be at least 3 characters!')
            valid = False
        if  len(data['instructions']) < 3:
            flash ('Instructions must be at least 3 characters!')
        if  len(data['date_made']) <  10:
            flash('Date required!')
            valid = False
        #if len(data['time']) <2:
            #flash('Thirty minutes or less?')
            #valid = False
        return valid

    @classmethod 
    def add_recipe(cls,data):
        query = 'INSERT into recipes (name, time, description, instructions, date_made, users_id) VALUES (%(name)s, %(time)s, %(description)s, %(instructions)s,%(date_made)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def view_all(cls,data):
        query = 'SELECT * from recipes'
        results= connectToMySQL(cls.db).query_db(query,data)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def view_one(cls, data):
        query = 'SELECT * from recipes where id = %(id)s;'
        results= connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])


    @classmethod
    def edit(cls, data):
        query = 'UPDATE recipes set name = %(name)s, time = %(time)s, description = %(description)s, instructions = %(instructions)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipes where id = %(id)s'
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def recipe_and_author(cls):
        query ='SELECT * FROM recipes'
        results= connectToMySQL(cls.db).query_db(query)
        recipes =[]
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_recipe_by_id(cls):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        results= connectToMySQL(cls.db).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
