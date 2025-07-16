# Addition

def addition(num1, num2 = 0, num3 = 0 , num4 = 0 ):
    return num1+num2+num3+num4

def perimeter_and_area_of_rectangle(length, breadth):
    perimiter = 2 * (length + breadth)
    area = length * breadth

    print(f"Length = {length}\nBreadth = {breadth}")
    print(f"Area of Rectangle is = {area}")
    print(f"Perimiter of Rectangle is = {perimiter}")


print("Addition of 4 numebrs =",addition(5,3,10,15))
print("Addition of 2 numbers =",addition(10,-25))
print("Addition of 2 numbers =",addition(10))


perimeter_and_area_of_rectangle(10,5)

l = 15
b = 12
perimeter_and_area_of_rectangle(b,l)
perimeter_and_area_of_rectangle(breadth=b, length=l)