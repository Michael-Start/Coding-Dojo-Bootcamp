<<<<<<< HEAD
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_on']
        self.updated_at = data['updated_on']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
# make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
# Create an empty list to append our instances of friends
        friends = []
# Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO friends (first_name, last_name, occupation, created_on, updated_on) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());'
        #data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db(query, data)

=======
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_on']
        self.updated_at = data['updated_on']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
# make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
# Create an empty list to append our instances of friends
        friends = []
# Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

>>>>>>> e7d0478fbf1ab043623e4921430e41c0d5112a08
