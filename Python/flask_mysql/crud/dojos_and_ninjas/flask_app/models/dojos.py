
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_on']
        self.updated_at = data['updated_on']
        self.ninjas = []

    @classmethod
    def new_dojo(cls, data):
        query ='INSERT INTO dojos (name, created_at, updated_at VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('dojos_&_ninjas').query_db(query, data)

    @classmethod
    def dojo_ninjas(cls,data):
        query = 'SELECT * from dojos left join ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_&_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_&_ninjas').query_db(query) 
        dojos =[]
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def one_dojo(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        result = connectToMySQL('dojos_&_ninjas').query_db(query, data)
        return cls(result[0])



class Ninja:
    def __innit__(self,db_data):
        self.id =db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.age = db_data['age']

    @classmethod
    def new_ninja(cls,data):
        query = 'INSERT INTO ninjas( first_name, last_name, age, email, dojo_id) Values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s;'
        return connectToMySQL('dojos_&_ninjas').query_db(query,data)