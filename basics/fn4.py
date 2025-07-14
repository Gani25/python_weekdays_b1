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

if checkPrime(n):
    print(f"Number = {n} is a prime numebr")

else:
    print(f"Number = {n} is not a prime numebr")
    