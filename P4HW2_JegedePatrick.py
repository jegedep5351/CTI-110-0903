# Name: Patrick O Jegede
# Date: 11/9/2025
# Assignment Name: P4HW2
# A brief description of the project: Code output to display employee payroll information.

total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

while True:
    name = input("Enter employee's name or \"Done\" to terminate: ")
    if name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Display individual employee summary
    print(f"\nEmployee name: {name}")
    print("Hours Worked | Pay Rate | Overtime | Overtime Pay | RegHour Pay | Gross Pay")
    print(f"{hours_worked:.1f}         | {pay_rate:.1f}     | {overtime_hours:.1f}      | ${overtime_pay:.2f}        | ${regular_pay:.2f}     | ${gross_pay:.2f}\n")

    # Update totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

# Final summary
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
