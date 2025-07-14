# WAP to check whether the given number is prime or not
# Divisible by Self and 1

n = int(input("Enter a number: "))
# assuming any value of n is prime only
# isPrime = True # assuming any value of n is prime only
is_prime = True 
i = 2

while i < n:
    if n % i == 0:
        # Not Prime
        is_prime = False
        break
    
    i = i + 1
if is_prime :
    print(f"Number {n} is a prime number")
else:
    print(f"Number {n} is not a prime number")
