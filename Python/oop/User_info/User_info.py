class User:
    def __init__(self, first_name, last_name, e_mail, age):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.Rewards_member= False
        self.gold_points = 10


Mike = User("Mike", "Start","someemail@place.com", 36)

def user_info(self):
    print("User info") 
    print(f"{self.first_name}") 
    print(f"{self.last_name}")
    print(f"{self.e_mail}")
    print(f"{self.age}")

def enroll(self):
    self.Rewards_member = True
    self.gold_points = 200
    print(self.Rewards_member)
    print(self.gold_points)

def spend_points(self, point_cost):
    if point_cost < self.gold_points:
        self.gold_points = self.gold_points - point_cost
        print(self.gold_points)
    else:
        print("Not enough Points!")


user_info(Mike)
enroll(Mike)
spend_points(Mike, 150)

