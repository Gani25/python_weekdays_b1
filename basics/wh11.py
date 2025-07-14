# WAP to print sum of 1 to n

n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i

    i = i + 1

print(f"The sum of 1 to {n} is {sum}")