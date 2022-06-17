from pets import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"{self.first_name} takes {self.pet.name} for a walk!")
        Pet.play(self.pet)
        return self

    def feed(self):
        print(f"{self.first_name} feeds{self.pet.name} {self.pet_food}!")
        Pet.eat(self.pet)
        return self

    def bathe(self):
        print(f"{self.first_name} gives {self.pet.name} a bath!")
        Pet.shout(self.pet)
        return self