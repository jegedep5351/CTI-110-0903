# Name: Patrick O Jegede
# Date: 10/26/2025
# Course: 110.0903.2025FA
# Description: Employee payroll calculation

# Collect employee information
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate regular and overtime hours
regular_hours = 40
overtime_hours = max(0, hours_worked - regular_hours)

# Calculate pay
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = min(hours_worked, regular_hours) * pay_rate
gross_pay = regular_pay + overtime_pay

# Display results
print("-------------------------------------")
print(f"Employee name: {name}")
print("Hours Worked  Pay Rate  OverTime   OverTime Pay  RegHour Pay  Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f"{hours_worked:<14}{pay_rate:<10}{overtime_hours:<11}{overtime_pay:<15.2f}${regular_pay:<13.2f}${gross_pay:.2f}")