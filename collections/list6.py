# List inside a list
# Multi dimension array

nums = [[2,10,25],[9,18,30],[12,15,6]]

print(nums)
print(nums[1][1])
print(nums[0])
print(nums[0][0])

new_nums = [
    [10,25,35,65,90],
    [2,30,6],
    [100,"Hello","SPRK",85,60],
    "Python"
]

print(new_nums)
print(new_nums[2][2])
print(new_nums[0][1:4])

print("ROWS are: ")
for row in new_nums:
    print(row)


nums = [[2,10,25,80,35],[9,18,30,25,35],[-5,-9,12,15,6]]
print("ROWS WITH CONDITIONS")
for row in nums:
    print(row[1:4])

print("Printing elements in matrix form")
for row in nums:
    for col in row:
        print(col,end="  ")
    
    print()