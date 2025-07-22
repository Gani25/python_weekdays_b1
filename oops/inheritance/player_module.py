from datetime import datetime
class player:
    # FIELDS
    
    # Method -> Constructor Parameterized
    def __init__(self,first_name, last_name, birth_year, team):
        print("Player Created")

        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.team = team

    # OVERRIDE
    def __str__(self):
        return f"-----------------------------------------------\n~~~Player Info~~~\n-----------------------------------------------\nName = {self.first_name} {self.last_name}\nTeam = {self.team}\nBirth Year = {self.birth_year}\nAge = {self.player_age()}"

    def player_age(self):
        return datetime.now().year - self.birth_year
