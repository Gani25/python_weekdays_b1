# Factorial of n using recursion
# a function calling it self within a function

def fact(n:int):
    if n <0:
        return -1
    if n == 0 or n == 1:
        return 1

    return n * fact(n-1)

num = int(input("Enter a number: "))

print(f"The factorial of {num} is {fact(num)}")

# WAP to calculate sum of first n natural number using recursion
