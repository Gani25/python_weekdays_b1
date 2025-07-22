# import cricket_player_module as cpm
from cricket_player_module import cricket_player
# from cricket_player_module import *

# virat = cricket_player_module.cricket_player()

# virat = cpm.cricket_player
player1 = cricket_player(birth_year=1987, first_name="Virat", last_name="Kohli",team="India")
player1.add_scores(50,80,60)
player1.add_scores(30)
print(player1)

player2 = cricket_player("David","Warner",1985,"Australia")
player2.add_scores(80,0,50,30,25,100)
print(player2)


