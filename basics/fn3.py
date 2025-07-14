# Multiplication of 2 numbers

def multiply(n1,n2):
    res = n1*n2

    return res

# print(multiply(5,5))

# Table of n till x iteration

i = 1
n = int(input("Enter a number: "))
x = int(input("Enter number of iterations: "))
while i <=x:
    table =multiply(n,i)
    print(f"{n} * {i} = {table}")

    i = i + 1
 