# kwargs -> Keyword Arguments

def info(**studentInfo):
    print("Student Info")

    # print(type(studentInfo))
    for k, v in studentInfo.items():
        print(f"{k}:{v}")

info(roll_no=20,name="Rohit Gupta",age = 35)