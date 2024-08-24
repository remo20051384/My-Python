import random  

class Human:  
    def __init__(self, name):  
        self.name = name  

class FootballPlayer(Human):  
    def __init__(self, name):  
        super().__init__(name)  

# List of player names  
player_names = [  
    "حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد",   
    "محمد", "خشایار", "میلاد", "مصطفی", "امین", "سعید",   
    "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل",   
    "بهروز", "شهروز", "سامان", "محسن"  
]  

# Create 22 FootballPlayer objects  
players = [FootballPlayer(name) for name in player_names]  

# Shuffle the players randomly  
random.shuffle(players)  

# Divide players into two teams  
team_A = players[:11]  # First 11 players for Team A  
team_B = players[11:]  # Remaining 11 players for Team B  

# Print players and their teams  
print("Team A:")  
for player in team_A:  
    print(f"{player.name} - Team A")  

print("\nTeam B:")  
for player in team_B:  
    print(f"{player.name} - Team B")