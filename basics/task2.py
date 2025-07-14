
# WAP to accept/input marks of 3 subject print sum and average
# m1 = 55, m2 = 80, m3 = 58
# sum = m1+m2+m3 = 193
# avg = sum / 3 = 64.333
# Output = Sum of marks is 193 and average is 64.333

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

sum = marks1 + marks2 + marks3
avg = sum / 3
print(f"Sum of marks is {sum} and average is {avg}")