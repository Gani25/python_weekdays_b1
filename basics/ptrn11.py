# Butterfly Pattern
n =  int(input("Enter a number: "))

# UPPER HALF
i = 1
while i <= n:

    # LEFT STARS
    j = 1
    while j <= i:
        print("* ", end="")
        j = j + 1
    
    # SPACE
    sp = 1
    while sp <= 2 * (n-i) - 1:
        print("  ", end="")
        sp = sp + 1
    
     # RIGHT STARS
    j = 1
    while j <= i:
        if j != n:
            print("* ", end="")
        j = j + 1
    i = i + 1
    print()

# LOWER HALD
i = n-1
while i >= 1:

    # LEFT STARS
    j = 1
    while j <= i:
        print("* ", end="")
        j = j + 1
    
    # SPACE
    sp = 1
    while sp <= 2 * (n-i) - 1:
        print("  ", end="")
        sp = sp + 1
    
     # RIGHT STARS
    j = 1
    while j <= i:
        if j != n:
            print("* ", end="")
        j = j + 1
    i = i - 1
    print()