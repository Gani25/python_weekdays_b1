nums = [
    [1,3,5,9,5],
    [2,4,6,9,4],
    [3,8,4,9,6],
    [1,6,5,6,1],
    [1,6,5,6,0]
]

r = len(nums)
c = len(nums[0])

print(f"Row length = {r}\nColumn length = {c}")
if(r !=c):
    print("Diagonal can be displayed for square matrix")
else:

    # ROW
    for i in range(r):

        # COLUMN
        for j in range(c):
            if(i == j or i+j == c-1):
                print(nums[i][j], end=" ")
            else:
                print(" ", end=" ")
        
        print()