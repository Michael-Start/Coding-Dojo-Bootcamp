from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('userrs_cr').query_db(query) #misspelled the database so userrs is correct here
        if len(results) == 0:
            return[]
        else:
            users =[]
            for user in results:
                users.append(cls(user))
            return users

    @classmethod #method to add a user to db
    def save(cls,data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());'
        return connectToMySQL('userrs_cr').query_db(query, data)

    @classmethod
    def one_user(cls, data):
        query = 'SELECT * from users WHERE id =%(id)s'
        result = connectToMySQL('userrs_cr').query_db(query, data)
        if len(result) == 0:
            return None
        else:
            return cls(result[0])

    @classmethod
    def update(cls,data):
        query = 'UPDATE users SET first_name=%(first_name)s, last_name = %(last_name)s , email =%(email)s WHERE id =%(id)s;' 
        return  connectToMySQL('userrs_cr').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return  connectToMySQL('userrs_cr').query_db(query, data)