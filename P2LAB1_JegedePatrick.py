#Name: Patrick O Jegede
#Date: 10/12/2025
#Assignment Name: P2LAB1
#Description: Calculation output for area of a circle

radius = float(input("What is the radius of the circle? "))

# Calculate other properties
diameter = 2 * radius
circumference = 2 * 3.14159 * radius
area = 3.14159 * radius * radius

# Output results
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
