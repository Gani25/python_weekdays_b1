student_1={
    "first_name":"Rohit",
    "last_name":"Raj",
    "marks": list(),
    "percentage":None
}

student_1["marks"].extend([50,80,60,90,70])
print(student_1)

student_1["percentage"] = sum(student_1.get("marks")) / len(student_1.get("marks"))
print(student_1)

