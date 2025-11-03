# Name: Patrick O Jegede
# Date: 11/2/2025
# Course: 110-0903.2025FA
# Description: Multiplication table using for loop and while loop

run_again = "yes"

while run_again.lower() == "yes":
    num = int(input("Enter an integer: "))
    
    # Use for loop to generate multiplication table
    for i in range(13):
        print(f"{num} * {i} = {num * i}")
    
    # Ask user if they want to run again
    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program...")