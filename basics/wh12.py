# WAP to print odd sum and even sum from 1 to 20 using one loop
# even sum = 2 + 4 + 6 + ... 20
# odd sum = 1 + 3 + 5 ... 19
# start = 1, stop = 20, gap = 1

odd_sum = 0
even_sum = 0
i = 1

while i <= 20:

    if i % 2 == 0:
        # Even -> Add value of i to even sum
        even_sum = even_sum + i
    else:
        # Odd -> Add value of i to odd sum
        odd_sum = odd_sum + i

    i = i + 1


print(f"The odd sum from 1 to 20 is {odd_sum}")
print(f"The even sum from 1 to 20 is {even_sum}")

# FIZZ BUZZ
# WAP to iterate from 1 to n and display msg based on criteria
# if num divisible by 3 and 5 both -> FIZZBUZZ
# if num divisible by 3 -> FIZZ
# if num divisible by 5 -> BUZZ
# if num is not divisible by any  -> num
# n = 100
# 1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ 11 FIZZ 13 14 FIZZBUZZ ... 

# WAP to print sum of digits
# 153 -> 1 + 5 + 3