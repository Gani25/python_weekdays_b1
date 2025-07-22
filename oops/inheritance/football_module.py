from player_module import player
class football_player(player):
    # FIELDS
    
    # Method -> Constructor Parameterized
    def __init__(self,first_name, last_name, birth_year, team):
        super().__init__(first_name,last_name,birth_year,team)
        self.goals = []

    # OVERRIDE
    def __str__(self):
        return f"{super().__str__()}\nGoals = {self.goals}\nAverage Goals = {self.calculate_average()}"

    
    def add_goals(self,*goals):
        self.goals.extend(goals)
    
    def calculate_average(self):
        return sum(self.goals) / len(self.goals)

    
