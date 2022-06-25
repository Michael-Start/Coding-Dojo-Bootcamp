<<<<<<< HEAD
# 1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15 #change 10 to 15
print(x) 

students[0]['last_name'] = 'Bryant' # Jordan = Bryant
print(students)

sports_directory['soccer'][0] = 'Andres' # Mess to Andres
print(sports_directory)

z[0]['y'] = 30 # 20 to 30
print(z)

# 2 iterate Through a List of Dictionaries

students = [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(x):
    for each_key in students:
        print(each_key)

iterateDictionary(students)  # print the names

#3 Get Values From a List of Dictionaries
def iterateDictionary2(y):
    i = 0
    b = 0
    for each_key in students:
        print(students[i]['first_name'])
        i = i+1
        if i > len(students)-1:
            break
    for each_key in students:
        print(students[b]['last_name'])
        b = b+1
        if b > len(students)-1:
            break

iterateDictionary2(students)    #make a list of first names, then last names

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



#Iterate Through a Dictionary with List Values
travel = {
    'Places_to_go': ['France', 'Fiji', 'Australia', 'Hawaii', 'Japan', 'Mexico', 'Columbia'],
    'Things_to_do': ['Museums', 'Surfing', 'Skydiving', 'Local food', 'Scuba-diving', 'Swimming', 'Acrobatics', 'Sight Seeing', 'Hiking']
}

def printInfo(h):
    print (len(travel['Places_to_go']))
    print("Places to go")
    print(travel ['Places_to_go'])
    print(len(travel['Things_to_do']))
    print('Things to do')
    print(travel['Things_to_do'] )


=======
# 1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15 #change 10 to 15
print(x) 

students[0]['last_name'] = 'Bryant' # Jordan = Bryant
print(students)

sports_directory['soccer'][0] = 'Andres' # Mess to Andres
print(sports_directory)

z[0]['y'] = 30 # 20 to 30
print(z)

# 2 iterate Through a List of Dictionaries

students = [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(x):
    for each_key in students:
        print(each_key)

iterateDictionary(students)  # print the names

#3 Get Values From a List of Dictionaries
def iterateDictionary2(y):
    i = 0
    b = 0
    for each_key in students:
        print(students[i]['first_name'])
        i = i+1
        if i > len(students)-1:
            break
    for each_key in students:
        print(students[b]['last_name'])
        b = b+1
        if b > len(students)-1:
            break

iterateDictionary2(students)    #make a list of first names, then last names

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



#Iterate Through a Dictionary with List Values
travel = {
    'Places_to_go': ['France', 'Fiji', 'Australia', 'Hawaii', 'Japan', 'Mexico', 'Columbia'],
    'Things_to_do': ['Museums', 'Surfing', 'Skydiving', 'Local food', 'Scuba-diving', 'Swimming', 'Acrobatics', 'Sight Seeing', 'Hiking']
}

def printInfo(h):
    print (len(travel['Places_to_go']))
    print("Places to go")
    print(travel ['Places_to_go'])
    print(len(travel['Things_to_do']))
    print('Things to do')
    print(travel['Things_to_do'] )


>>>>>>> a3c385909ef11b0c40a228c82f2ad81408017552
printInfo(travel)