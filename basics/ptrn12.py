n = int(input("Number: "))

i = 1

while i<=n:
    j = 1
    while j <=n:
        if i == j or j == n-i+1:
            print("* ",end="")
        else:
            print("  ",end="")
        
        j = j + 1
    
    print()
    i = i + 1