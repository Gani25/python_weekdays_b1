'''
Write a program that calculates the electricity bill
based on the following conditions:

For first 100 units: INR 5/unit
For next 100 units (101-200): INR 6/unit
For units above 200: INR 7/unit

Fixed charge of INR 150 in final amount

Then on total amount add 18% tax
'''

units = int(input("Enter units consumed: "))

if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = 500 + (units-100) * 6
else:
    bill_amount = 500 + 600 + (units-200) * 7

total_without_tax = bill_amount + 150

total_with_tax = total_without_tax + 0.18 * total_without_tax

print("-----------------------------------------------")
print(f"Units Consumed = {units}")
print("-----------------------------------------------")
print(f"Bill Amount = {bill_amount}")
print(f"Total Without Tax = {total_without_tax}")
print(f"Tax Amount = {total_with_tax - total_without_tax}")
print(f"Total With Tax = {total_with_tax}")
print("-----------------------------------------------")