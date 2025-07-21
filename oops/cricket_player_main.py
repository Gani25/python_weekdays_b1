# import cricket_player_module as cpm
from cricket_player_module import cricket_player,calculate_avg
# from cricket_player_module import *

# virat = cricket_player_module.cricket_player()

# virat = cpm.cricket_player
virat = cricket_player(birth_year=1987, first_name="Virat", last_name="Kohli",team="India")

print("Player Info")
print("Name =",virat.first_name ,virat.last_name)
print("Team =",virat.team)
print("Birth Year =",virat.birth_year)
print("Scores =",virat.scores)


david = cricket_player(birth_year=1985, first_name="David", last_name="Warner",team="Australia")
print("\nPlayer Info")
print("Name =",david.first_name ,david.last_name)
print("Team =",david.team)
print("Birth Year =",david.birth_year)
print("Scores =",david.scores)

