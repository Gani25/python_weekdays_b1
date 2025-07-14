# WAP to check whether the number is Armstrong number or not


num_str = input("Enter a number: ")

digits = len(num_str)

num = int(num_str)
i = num 
sum = 0
while i != 0:
    remainder = i % 10
    power = remainder ** digits
    sum = sum + power
    i = i // 10

if sum == num:
    print(f"Number = {num} is a Armstrong number, Sum is {sum}")
else:
    print(f"Number = {num} is not a Armstrong number, Sum is {sum}")


'''
1. WAP to print sum of square of number from 1 to 5
# 1 + 4 + 9 + 16 + 25
2. WAP to print series of prime number from 1 to n
3. WAP to accept n and iteration (x). Then print table of n till x iteration
# Example n = 6 and x = 5
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
'''