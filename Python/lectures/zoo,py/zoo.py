class Zoo:
    def __init__(self, city, name, size, visitor_capacity, opening_date):
        self.city = city
        self.name = name
        self.size = size
        self.visitor_capacity = visitor_capacity
        self.opening_date= opening_date


class Animal:
    def __init__(self, species, name, weight, color, height, birth_date = None):
        self.species = species
        self.name= name
        self.weight = weight
        self.color = color
        self.height = height
        self.birthdate = birth_date

    def eat(self, food):
        print(f"{self.species} named {self.name} is eating {food}")
        return self


portland_zoo = Zoo("Portland", "The Oregon Zoo", 500, 10000, "1888-08-15")
seattle_zoo = Zoo("Seattle", "Woodlawn Park Zoo", 92, 15000, "1940-03-05")

famous_penguin = Animal("Penguin", "Steve", 20, "Black and White", 50)
this_panda = Animal("Panda", "Jane", 250, "Mixed", 75, "1985-01-15")
