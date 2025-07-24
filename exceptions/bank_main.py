from bank import *

try:
    obj1 = Account(200)

    obj1.display_details()
except Exception as e:
    print(e)
else:
    print("Hello")