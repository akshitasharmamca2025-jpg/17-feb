# List of student scores
scores = [25, 34, 67, 89, 30, 32, 45, 28, 90, 33]

# Step 1: Remove the lowest 2 scores
scores.sort()                  # Sort scores in ascending order
updated_scores = scores[2:]    # Remove first two (lowest) scores

# Step 2: Add grace marks of 5 to students scoring between 30–35
for i in range(len(updated_scores)):
    if 30 <= updated_scores[i] <= 35:
        updated_scores[i] += 5

# Step 3: Count number of students passed (marks >= 40)
pass_count = 0
for score in updated_scores:
    if score >= 40:
        pass_count += 1

# Display results
print("Updated Scores:", updated_scores)
print("Number of Students Passed:", pass_count)