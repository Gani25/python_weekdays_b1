# SETS -> Unique Values, Unordered

my_set = set()
print(type(my_set))
my_set.add(5)

my_set.add("Hello")
print(f"My Set = {my_set}")
my_set.add(10)
my_set.add(5)
print(f"My Set = {my_set}")

my_set.add("Hello")
print(f"My Set = {my_set}")
my_set.add(True)
print(f"My Set = {my_set}")
my_set.add(100)
print(f"My Set = {my_set}")

my_set.update(["SPRK",-5,"Hello",15])
print(f"My Set = {my_set}")

my_set.discard("SPRK")
print(f"My Set = {my_set}")
my_set.discard("SPRK")
print(f"My Set = {my_set}")

# my_set.remove("SPRK") KeyError
print(f"My Set = {my_set}")

print(f"Element Deleted is = {my_set.pop()}")
print(f"My Set = {my_set}")
print(f"Element Deleted is = {my_set.pop()}")
print(f"My Set = {my_set}")
print(f"Element Deleted is = {my_set.pop()}")
print(f"My Set = {my_set}")
print(f"Element Deleted is = {my_set.pop()}")
print(f"My Set = {my_set}")
my_set.add(False)
print(f"My Set = {my_set}")
print(f"Element Deleted is = {my_set.pop()}")
print(f"My Set = {my_set}")