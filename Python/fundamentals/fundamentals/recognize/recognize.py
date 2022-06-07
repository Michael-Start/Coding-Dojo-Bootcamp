num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, decimal/float
boolean = True # boolean
string = 'Hello World' # string variable
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize 
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) # log statement, access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) # log statement and access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # log statement access value, tuple

if num1 > 45: #conditional if, evaluation
    print("It's greater") # log statement
else:          #conditional else
    print("It's lower") # log statement

if len(string) < 5: #conditional if and string length
    print("It's a short word!") # log statement
elif len(string) > 15: #conditional else if, evaluation
    print("It's a long word!") # log statement
else:                   # conditional else
    print("Just right!")  # log statement
 
for x in range(5): #for loop, start 0 go up to 5
    print(x) #log statement
for x in range(2,5): # for loop initialize at 2 end at 5
    print(x) #log statement
for x in range(2,10,3): # for loop, start at 2 up to 10, increment by 3
    print(x) #log statement
x = 0 #variable declaration
while(x < 5): #while loop
    print(x)  #log statement
    x += 1 # increment

pizza_toppings.pop() #list delete final value
pizza_toppings.pop(1) #list delete value at index 1

print(person) #log statement
person.pop('eye_color') # dictionary remove value
print(person) #log statement

for topping in pizza_toppings: #for loop through list
    if topping == 'Pepperoni': #if statement condition
        continue # if statement continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement condition
        break #stop loop

def print_hello_ten_times():  #function define
    for num in range(10): #function parameter
        print('Hello') # log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function define
    for num in range(x): #function parameter, for loop
        print('Hello') #log statement

print_hello_x_times(4) # function call, argument

def print_hello_x_or_ten_times(x = 10): #function define, with default parameter
    for num in range(x): #for loop
        print('Hello') #log statement 

print_hello_x_or_ten_times() #function call default
print_hello_x_or_ten_times(4) #function call to 4


"""
Bonus section               multi line comment
"""

# print(num3)               #NameError: name <variable name> is not defined
# num3 = 72         # variable declared
# fruit[0] = 'cranberry'    #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])     #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #index error
#   print(boolean)
# fruit.append('raspberry')     #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                  #AttributeError: 'tuple' object has no attribute 'pop'