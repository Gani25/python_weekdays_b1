# WAP to print series of prime number from 1 to n

def checkPrime(num):

    if num <= 1:
        return False
    i = 2
    while i < num:
        if(num % i == 0):
            return False
        
        i = i  + 1
    return True

n = int(input("Enter a number: "))
if n > 1:
    print(f"The series of prime number from 1 to {n} is:")
    i = 2
    while i <= n:
        if checkPrime(i):
            print(i,end=" ")
        
        i = i + 1
else:
    print("Please enter positive number greater than 1")