# Name: Patrick Jegede
# Date: 9/30/2025
# Assignment Name: P1HW1
# Description: Calculating Exponents, Adding and Subtracting Numbers.

print("-----Calculating Exponents-----")


base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

power_result = base ** exponent
print(f"{base} raised to the power of {exponent} is: {power_result} !!\n")

print("-----Addition and Subtraction-----")


start_int = int(input("Enter a starting integer: "))
add_value = int(input("Enter an integer to add: "))
sub_value = int(input("Enter an integer to subtract: "))


sum_result = start_int + add_value
diff_result = start_int - sub_value

print(f"{start_int} + {add_value} {sub_value} {diff_result} is equal to {sum_result}")



