'''
    *
   **
  ***
 ****
*****
'''

n = int(input("Enter a number: "))

# ROWS (i)
for i in range(1,n+1):

    # SPACE
    for sp in range(1,n-i+1):
        print("  ",end="")

    # STAR(j)
    for j in range(1,i+1):
        print("* ",end="")
    
    print()