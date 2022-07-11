from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,db_data):
        self.id =db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.age = db_data['age']
        self.created_on = db_data['created_on']
        self.updated_on = db_data['updated_on']
        self.dojo_id = db_data['dojo_id']

    @classmethod
    def new_ninja(cls,data):
        query = 'INSERT INTO ninjas( first_name, last_name, email, age, dojo_id) Values (%(first_name)s, %(last_name)s, %(email)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL('dojos_&_ninjas').query_db(query,data)