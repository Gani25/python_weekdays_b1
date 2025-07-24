file = None
try:
    file = open("demo123.txt","r")
    print(file.read())
except Exception as e:
    print(e)
finally:
    if file:
        file.close()
        print("File Closed Successfully")
    else:
        print("File Not Opened")
