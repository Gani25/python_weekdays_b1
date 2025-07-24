'''
Exceptions: Unusual condition that arises in program
and blocks normal flow of program is called as exception
'''



try:
    num1 =  int(input("Enter number 1: ")) 
    num2 =  int(input("Enter number 2: ")) 
    result = num1 / num2

    print(f"Dividing num1 = {num1}, num2 = {num2}")
    print(f"Result = {result}")
except Exception as e:
    print(e)
    
print("Hello")