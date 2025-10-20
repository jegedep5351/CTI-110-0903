#Name: Patrick O Jegede
#Date: 10/19/2025
#Course: CTI-110.0903
#Description: Calculating coin breakdown.

# Get the amount of money from the user
amount = float(input("Enter the amount of money as a float: $"))

# Convert to cents to avoid floating point precision issues
total_cents = int(amount * 100 + 0.1)  # Adding 0.1 to handle floating point rounding

# Check if amount is zero
if total_cents == 0:
    print("\nNo Change")
else:
    # Calculate dollars and remaining cents
    dollars = total_cents // 100
    remaining_cents = total_cents % 100

    # Calculate the number of each coin using floor division
    quarters = remaining_cents // 25
    remaining_cents %= 25

    dimes = remaining_cents // 10
    remaining_cents %= 10

    nickels = remaining_cents // 5
    remaining_cents %= 5

    pennies = remaining_cents

    # Display the results
    results = []
    if dollars > 0:
        results.append(f"{dollars} Dollar{'s' if dollars != 1 else ''}")
    if quarters > 0:
        results.append(f"{quarters} Quarter{'s' if quarters != 1 else ''}")
    if dimes > 0:
        results.append(f"{dimes} Dime{'s' if dimes != 1 else ''}")
    if nickels > 0:
        results.append(f"{nickels} Nickel{'s' if nickels != 1 else ''}")
    if pennies > 0:
        results.append(f"{pennies} Penn{'y' if pennies == 1 else 'ies'}")
    
    # Print each result on a new line
    print()
    for result in results:
        print(result)