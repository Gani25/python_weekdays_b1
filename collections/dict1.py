phone_book = {"Aman":"+91 1234 5678","Ayush":"+91 5858 9586"}

print(phone_book)
phone_book["Abdul"] = "+91 7506 2589"
print(phone_book)
phone_book["Aman"] = "+91 8888 7777"
print(phone_book)

phone_book.update({"Rohit":"+91 8585 8585","Subham":"+91 1000 1000"})
print(phone_book)
print("Number of Rohit = ",phone_book["Rohit"])
print("Number of Rohit = ",phone_book.get("Rohit"))

print(phone_book.pop("SPRK","Not Found"))

print(phone_book)
del phone_book["Abdul"]

print(phone_book)
print(phone_book.keys())
print(phone_book.values())
for key in phone_book.keys( ):
    print(key,"->",phone_book.get(key) )

print(phone_book.items())
for k, v in phone_book.items():
    print(k,"->",v )