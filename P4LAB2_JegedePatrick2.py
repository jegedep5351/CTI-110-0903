# Name: Patrick O Jegede
# Date: 11/2/2025
# Course: 110-0903.2025FA
# Description: Multiplication table using for loop and while loop with negative number check

run_again = "yes"

while run_again.lower() == "yes":
    num = int(input("Enter an integer: "))
    
    if num < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
    
    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program...")