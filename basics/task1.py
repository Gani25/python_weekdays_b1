# WAP to convert Farenheit to Degree Celcius

# Accept input in Farenheit 
# Example
# input: 68
# Output: Temperature 68 Farenheit is 20 Degree Celcius

# Celsius = (Fahrenheit - 32) * 5 / 9

temp_in_farenheit = float(input("Enter temperature in farenheit: "))

# formula
temp_in_celcius = (temp_in_farenheit-32) * 5 / 9


# DISPLAY ANSWER
print(f"Temperature {temp_in_farenheit} Farenheit is {temp_in_celcius} Degree Celcius")
