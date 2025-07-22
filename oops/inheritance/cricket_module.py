from player_module import player

class cricket_player(player):

    def __init__(self,first_name, last_name, birth_year, team):
        super().__init__(first_name, last_name, birth_year, team)
        print("Cricket Player Creater")
        self.scores = []

    def add_scores(self,*runs):
        self.scores.extend(runs)
    
    def __str__(self):
        return f"{super().__str__()}\nScores = {self.scores}\nAverage Scores = {self.calculate_average()}"
    
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)


    