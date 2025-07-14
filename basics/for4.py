# WAP to check whether the number is a prime number or not
# start = 2, stop = n - 1, gap = 1

n = int(input("Enter a number: "))

is_prime = True 
if n <=1:
    is_prime = False 

for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break 

if is_prime:
    print(f"The Number {n} is a prime number")
else:
    print(f"The Number {n} is not a prime number")