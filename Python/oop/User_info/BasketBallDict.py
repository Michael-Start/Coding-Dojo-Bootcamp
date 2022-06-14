class Player:
    def __init__(self, data):
        self.name = data ["name"]
        self.age = data ["age"]
        self.position = data ["position"]
        self.team = data ["team"]

    def __repr__(self):
        return f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}"

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }
    
jason ={
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    }
    
kyrie ={
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    }

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

def display_player(plyr):
    print(plyr.name)
    print(plyr.age)
    print(plyr.position)
    print(plyr.team)

display_player(player_kevin)
display_player(player_jason)
display_player(player_kyrie)

#list of dict
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, 
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, 
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]


#for loop to make player instances to list
new_team = []

for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)