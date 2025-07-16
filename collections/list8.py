arr = [
    [2,3,8,1],
    [1,4,5,6],
    [9,1,0,3]
]

r = len(arr)
c = len(arr[0])
for i in range(c):
    for j in range(r):
        print(arr[j][i],end=" ")

    print()