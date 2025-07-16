def addition(*numbers,name:str = "SPRK"):
    print(f"Name = {name}")
    print(numbers)
    print(sum(numbers))
    print(type(numbers))

addition(1,5,9,3)
addition(5,6,25,1, name="ABDUL")