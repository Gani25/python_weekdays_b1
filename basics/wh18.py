'''
3. WAP to accept n and iteration (x). Then print table of n till x iteration
# Example n = 6 and x = 5
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
'''

n = int(input("Enter a number: "))
x = int(input("Enter number of iterations: "))
i = 1
while i <= x:
    table = i * n 
    print(f"{n} * {i} = {table}")
    i = i + 1