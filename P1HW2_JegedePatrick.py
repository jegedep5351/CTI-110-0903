# Name: Patrick Jegede
# Date: 10/1/2025
# Assignment Name: P1HW2
# Description: Travel and Budget Itenary output

# Travel Expense Calculator

print("This program calculate and displays travel expenses")
print("Enter Budget: 1200")
print("Enter your travel destination: Nashville")
print("How much do you think you will spend on gas? 250")
print("Approximately, how much will you need for accomodation/hotel? 600")
print("Last, how much do you need for food? 300")

print("------------Travel Expenses------------")

destination = input("\nEnter your travel destination: ")
budget = float(input("Enter Budget:"))
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses


print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"\nFuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print(f"\nRemaining Balance: ${remaining_balance:.2f}")
