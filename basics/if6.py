# WAP to check whether the number is positive or negative or zero
# Conditions = 3
# input = 1

n = int(input("Enter a number: "))

if n > 0:
    print(f"Number = {n} is a positive number")
elif n < 0:
    print(f"Number = {n} is a negative number")
else:
    print("Number is zero")
