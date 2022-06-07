# #Countdown to Blast off!
# def countdown(i,m):
#     for x in range(i,-1,-m):
#         if x == 0:
#             print("Blast off!")
#             break
#         print(x)

# countdown(10,1)

# #Print and Return
# def print_and_return(x,y):
#     print(x)
#     return(y)

# print_and_return(5,20)

#First Plus Length 
# def first_plus_len(x):
#     y=x[0]
#     y = y + len(x)
#     print(y)
# first_plus_len([5,2,4])

#Values Greater than Second
# def greater_than_2nd(x):
#     print(x)
#     if len(x)<2:
#         return False
#     for i in range (len(x)):
#         y = x[1]
#         if x[i] < y:
#             x.pop(i)
#     print(x)

# greater_than_2nd([13,5,6,10,2])

# This Length, That Value 
# def length_value(x,y):
#     i=[]
#     while len(i)<x:
#         i.append(y)
#     print(i)
# length_value(2,8)