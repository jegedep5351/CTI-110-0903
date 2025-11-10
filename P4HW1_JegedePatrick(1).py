num_scores = int(input("How many scores do you want to enter? "))

scores = []
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i + 1} again:")

# Remove the lowest score
lowest_score = min(scores)
scores.remove(lowest_score)

# Calculate average
average = sum(scores) / len(scores)

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score : {lowest_score:.1f}")
print(f"Modified List : {[round(s, 1) for s in scores]}")
print(f"Scores Average: {average:.2f}")
print(f"Grade        : {grade}")