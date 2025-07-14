# Take 2 numbers from user and display sum/addition

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

print("Type of num1 =",type(num1))
print("Type of num2 =",type(num2))

# change str to int
num1 = int(num1)
num2 = int(num2)
print("Type of num1 =",type(num1))
print("Type of num2 =",type(num2))

sum = num1+num2 
print("The addition is =",sum)