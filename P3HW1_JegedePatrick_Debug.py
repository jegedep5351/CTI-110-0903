# Name: Patrick O Jegede
# Date: 10/26/2025
# Course: 110.0903.2025FA
# Description: Code Debugging


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for all grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Dsiplay grading results
print(f"\nLowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Sum of grades: {total}")
print(f"Average grade: {avg:.2f}")

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') 





