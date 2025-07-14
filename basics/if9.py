# 2. WAP to check whether the number have 3 digits or not
    # input = 153 -> Number = 153 contains 3 digits
    # input = 80 -> Number = 80 doesnot contains 3 digits
    # input = -856 -> Number = -856 contains 3 digits
# Input = 1
# COnditions = 2

n = int(input("Enter a number: "))

if (n >= 100 and n <=999) or (n >=-999 and n <= -100):
    print(f"Number = {n} contains 3 digits")
else:
    print(f"Number = {n} doesnot contains 3 digits")

'''
WAP to check whether the triangle is a equilateral, isoceles, scalene
# INPUT = 3
Equilateral -> All 3 sides are equal -> s1 == s2 == s3
Isoceles -> Any 2 sides are equal -> s1 == s2 || s2 == s3 || s1 == s3
Scalene -> No Sides are equal
'''
