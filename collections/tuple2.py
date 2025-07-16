def my_fun(a:int, b:int):
    
    sum = a + b 
    return sum 

def sum_prod_power(a:int,b:int):
    prod = a * b 
    sum = my_fun(a,b)
    power = a ** b

    return sum, prod, power

result = sum_prod_power(5,3)
print(result)
print(type(result))

add , multiply, raise_to = sum_prod_power(6,3)
print(f"Value of sum is {add}")
print(f"Value of product is {multiply}")
print(f"Value of power is {raise_to}")
