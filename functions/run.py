# import utility
# import utility as util
# from utility import area_of_circle
from utility import *

r = int(input("Enter radius of a circle: "))

# print(f"Radius of Circle is {r} and Area of circle is {utility.area_of_circle(r)}")

# print(f"Radius of Circle is {r} and Area of circle is {util.area_of_circle(r)}")

print(f"Radius of Circle is {r} and Area of circle is {area_of_circle(r)}")
l = int(input("Enter length of a rectangle: "))
b = int(input("Enter breadth of a rectangle: "))
print(f"Length is {l}, Breadth is {b} and Area of Rectangle is {area_of_rectangle(l,b)}")