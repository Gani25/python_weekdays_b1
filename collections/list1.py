marks = [] #empty list
marks_1 = list() # empty list

print(marks)
print(marks_1)
print(f"Type of marks is: {type(marks)}")
print(f"Type of marks_1 is: {type(marks_1)}")

marks.append(50)
marks.append(65)
print(f"Marks = {marks}")
marks.append(80)
marks.append(90)
marks.append(85)
print(f"Marks = {marks}")
print(f"Marks at index 0 = {marks[0]}")
print(f"Marks at index 1 = {marks[1]}")
print(f"Marks at index 2 = {marks[2]}")
print(f"Marks at index 3 = {marks[3]}")
print(f"Marks at index 4 = {marks[4]}")
# print(f"Marks at index 5 = {marks[5]}")

print("Hello")

marks.insert(1,35)
print(f"Marks = {marks}")

marks[0] = 60

print(f"Marks = {marks}")
marks.extend([55,25,60,35,60,12])
print(f"Marks = {marks}")

marks_1.extend([50,90,12,35,85])
print(f"Marks_1 = {marks_1}")


marks.remove(60)
print(f"Marks = {marks}")

print(f"Element deleted = {marks.pop()}")
print(f"Marks = {marks}")
print(f"Element deleted with INDEX CALL = {marks.pop(marks.index(60))}")
print(f"Marks = {marks}")
marks.extend([60,55,25,60,35,60,12])

print(f"Marks = {marks}")
print(f"First occurence index of 60 is {marks.index(60)}")
print(f"Mid occurence index of 60 is {marks.index(60,10)}")
print(f"Last occurence index of 60 is {marks.index(60,13)}")

print(f"Size of marks list is = {len(marks)}")

print(f"Marks = {marks}")
marks.reverse()
print(f"In Reverse Order Marks = {marks}")
marks.sort()
print(f"Sorted Marks = {marks}")
marks.sort(reverse=True)
print(f"Sorted Marks in DESC = {marks}")

