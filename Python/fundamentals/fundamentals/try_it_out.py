# # List of dictionaries
# users = [
#     {"first": "Ada", "last": "Lovelace"}, # index 0
#     {"first": "Alan", "last": "Turing"}, # index 1
#     {"first": "Eric", "last": "Idle"} # index 2
# ]
# # Dictionary of lists
# resume_data = {
#     #        	     0           1           2
#     "skills": ["front-end", "back-end", "database"],
#     #                0           1
#     "languages": ["Python", "JavaScript"],
#     "hobbies":["rock climbing", "knitting"]
# }

# print(resume_data["skills"][1])
# print(users[2]["first"])


# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team


# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# # Uncomment the line below to test
# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])

# class Carrier:
#     overseer = "FAA"
#     def __init__(self, year, name, city):
#         self.year = year
#         self.name= name
#         self.city= city
#         self.flights = [] #list of flights
#         self.total_workers = 0 #number of workers
        

#     def hire_workers(self):
#         self.total_workers+=1
#         return self

# carrier_1 = Carrier(2022, "Coding Dojo Airlines", "Coding Dojo City")
# carrier_2 = Carrier(2000, "Rapid Flights", "Far Away", )

# carrier_1.hire_workers().hire_workers()
# print(carrier_1.total_workers,
# carrier_1.name)


#favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
#print(f'Your favorite color is: {favorite_color}') #output, prints the color given to the console

#from distutils.util import change_root


class Carrier: # Define your class here
    # Class variable: list that will hold your carriers - this is 
    # how we can access individual Carriers when we cannot
    # otherwise do so
    all_carriers = [] 
    overseer = "FAA" # Class variable

    def __init__(self, year, name, city):
        self.year = year
        self.name = name
        self.city = city
        self.flights = [] # List of flights
        self.total_workers = 0 # Workforce for this carrier
        Carrier.all_carriers.append(self) # Add this carrier
        # self here is used to hold the info on this new carrier

    @classmethod
    def change_overseer(cls, new_name):
        cls.overseer = new_name
        print(cls.overseer)
        return cls

    # @staticmethod
    # def enough_workers(num_of_workers, needed_workers):
    #     if num_of_workers < needed_workers:
    #         print("Hire more workers!")
    #     else:
    #         print("We have enough workers")

    change_overseer("New thing")