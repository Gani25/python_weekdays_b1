# Cricket Player Information
# name, scores (list), yob, avg, age
import datetime as dt

def calculate_average(scores):
    return sum(scores)/len(scores)

def calculate_age(birth_year):
    return dt.datetime.now().year - birth_year

virat = {
    "first_name":"Virat",
    "last_name":"Kohli",
    "scores":[],
    "birth_year":1987,    
    "team":"India"
}

# virat= dt.datetime.now().year - virat["yob"]

virat["scores"].append(50) #score 1
virat["scores"].append(90) # score 2
virat["scores"].append(100) # score 3

print("Player Info")
print("Name =",virat["first_name"],virat["last_name"])
print("Team =",virat["team"])
print("Birth Year =",virat["birth_year"])
print("Age =",calculate_age(virat["birth_year"]))
print("Scores =",virat["scores"])
print("Average Scores =",calculate_average(virat["scores"]))


david = {
    "first_name":"David",
    "last_name":"Warner",
    "scores":[],
    "birth_year":1985,
    "team":"Australia"
}

david["scores"].append(0) #score 1
david["scores"].append(40) # score 2
david["scores"].append(35) # score 3
david["scores"].append(80) # score 4

print("Player Info")
print("Name =",david["first_name"],david["last_name"])
print("Team =",david["team"])
print("Birth Year =",david["birth_year"])
print("Age =",calculate_age(david["birth_year"]))
print("Scores =",david["scores"])
print("Average Scores =",calculate_average(david["scores"]))
