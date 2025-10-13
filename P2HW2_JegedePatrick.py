#Name: Patrick O Jegede

#Date: 10/13/2025

#Assignment Name: P2HW2

#Description of Program: Grading Document





# Initialize an empty list to store grades
grades = []

# Get grades for 6 modules
for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)

# Calculate statistics
lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average = sum_grades / len(grades)

# Display results
print("\n" + "-" * 10 + "Results" + "-" * 15)
print(f"Lowest Grade:       {lowest_grade:.1f}")
print(f"Highest Grade:      {highest_grade:.1f}")
print(f"Sum of Grades:      {sum_grades:.1f}")
print(f"Average:            {average:.2f}")
print("-" * 35)