num1 = None
num2 = None
while True:
    try:
        num1 = int(input("Enter a number 1: "))
        break
    except Exception:
        print("Please enter number only")
while True:
    try:
        num2 = int(input("Enter a number 2: "))
        if(num2 == 0):
            raise ZeroDivisionError("Please enter number greater than 0, Anything divide by 0 is infinite")
        break
    except ZeroDivisionError as ze:
        print(ze)
    except Exception: 
        print("Please enter number only")

print(f"Division of n1 = {num1}, n2 = {num2} is {num1/num2}")