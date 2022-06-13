class User:
    def __init__(self, first_name, last_name, e_mail, age):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.Rewards_member= False
        self.gold_points = 0



    def display_info(self):
        print("User info") 
        print(f"First Name: {self.first_name}") 
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.e_mail}")
        print(f"Age: {self.age}")
        print(f"Is a Rewards Member? {self.Rewards_member}")
        print(f"Has {self.gold_points} Gold Points to Spend")
        return self

    def enroll(self):
        if self.Rewards_member == True:
            print("Already enrolled!")
            return self
        self.Rewards_member = True
        self.gold_points = 200
        return self

    def spend_points(self, point_cost):
        if point_cost < self.gold_points:
            self.gold_points = self.gold_points - point_cost
            print(f"You have {self.gold_points} left!")
        else:
            print("Not enough Points!")
        return self

Mike = User("Mike", "Start","someemail@place.com", 36)
Joe = User("Joe", "Smith", "anaddress@place.com", 25)
Jane = User("Jane", "Blane", "anemail@place.com", 43)

#display_info(Mike)
# display_info(Joe)
# display_info(Jane)
# enroll(Mike)
# spend_points(Mike, 50)
# enroll(Joe)
# spend_points(Joe, 80)
# spend_points(Jane, 40)
# display_info(Mike)
# display_info(Joe)
# display_info(Jane)



Mike.display_info().enroll().spend_points(50).display_info()
Joe.display_info().enroll().spend_points(80).display_info()
#Jane.display_info().spend_points(50).enroll().display_info().spend_points(50).display_info()
