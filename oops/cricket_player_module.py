from datetime import datetime
class cricket_player:
    # FIELDS
    
    # Method -> Constructor Parameterized
    def __init__(self,first_name, last_name, birth_year, team):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    # OVERRIDE
    def __str__(self):
        return f"-----------------------------------------------\n~~~Player Info~~~\n-----------------------------------------------\nName = {self.first_name} {self.last_name}\nTeam = {self.team}\nBirth Year = {self.birth_year}\nAge = {self.player_age()}\nScores = {self.scores}\nAverage Scores = {self.calculate_average()}"

    def player_age(self):
        return datetime.now().year - self.birth_year
    
    def add_scores(self,*runs):
        self.scores.extend(runs)
    
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    

# def player_age(birth_year:int) -> int:

# CLASS for Football Player -> first name, last name, birth year, goal