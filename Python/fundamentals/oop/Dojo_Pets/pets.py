class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 50
        self. energy = 50

    def sleep(self):
        self.energy +=25
        print(f"{self.name} Takes a nap! Current pet energy {self.energy}")
        return self

    def eat(self):
        self.energy+= 5
        self.health += 10
        print(f"{self.name} Chows down the food! Current pet health is: {self.health}, and current energy is {self.energy}")
        return self

    def play(self):
        self.health +=5
        print(f"{self.name} is {self.tricks} around gleefully! Current pet health is {self.health}")
        return self

    def shout(self):
        print(f"{self.name} let's out a loud {self.noise}")
        return self
