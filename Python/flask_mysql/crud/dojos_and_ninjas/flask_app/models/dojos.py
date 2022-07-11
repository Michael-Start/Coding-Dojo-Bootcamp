from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_on']
        self.updated_at = data['updated_on']
        self.ninjas = []

    @classmethod
    def new_dojo(cls, data):
        query ='INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL('dojos_&_ninjas').query_db(query, data)

    @classmethod
    def dojo_ninjas(cls,data):
        query = 'SELECT * from dojos left join ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_&_ninjas').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_on' : row_from_db['ninjas.created_on'],
                'updated_on' : row_from_db['ninjas.updated_on'],
                'email'  : row_from_db['email'],
                'dojo_id': row_from_db['dojo_id']
                
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



# class Ninja:
#     def __init__(self,db_data):
#         self.id =db_data['id']
#         self.first_name = db_data['first_name']
#         self.last_name = db_data['last_name']
#         self.email = db_data['email']
#         self.age = db_data['age']
#         self.created_on = db_data['created_on']
#         self.updated_on = db_data['updated_on']
#         self.dojo_id = db_data['dojo_id']

#     @classmethod
#     def new_ninja(cls,data):
#         query = 'INSERT INTO ninjas( first_name, last_name, age, email, dojo_id) Values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s;'
#         return connectToMySQL('dojos_&_ninjas').query_db(query,data)

        # [
        #     {
        #         'id': 4,
        #          'name': 'dojo_1', 
        #          'created_on': None, 
        #          'updated_on': None, 
        #          'ninjas.id': 3, 
        #          'first_name': 'Mike', 
        #          'last_name': 'Start', 
        #          'email': 'address@email.com', 
        #          'age': 36, 
        #          'ninjas.created_on': None, 
        #          'ninjas.updated_on': None, 
        #          'dojo_id': 4
        #          }, {'id': 4, 'name': 'dojo_1', 'created_on': None, 'updated_on': None, 'ninjas.id': 4, 'first_name': 'Erika', 'last_name': 'McC', 'email': 'address@email.com', 'age': 29, 'ninjas.created_on': None, 'ninjas.updated_on': None, 'dojo_id': 4}, {'id': 4, 'name': 'dojo_1', 'created_on': None, 'updated_on': None, 'ninjas.id': 5, 'first_name': 'Ninja 3', 'last_name': '3', 'email': 'address@email.com', 'age': 34, 'ninjas.created_on': None, 'ninjas.updated_on': None, 'dojo_id': 4}]