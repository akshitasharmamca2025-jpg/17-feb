# List of employee salaries
salaries = [25000, 55000, 48000, 72000, 15000, 51000]

# Define minimum wage
minimum_wage = 20000

# Step 1: Remove salaries below minimum wage
valid_salaries = []
for s in salaries:
    if s >= minimum_wage:
        valid_salaries.append(s)

# Step 2: Add 5% bonus to salaries greater than 50,000
updated_salaries = []

for s in valid_salaries:
    if s > 50000:
        bonus = s * 0.05
        s = s + bonus
    updated_salaries.append(s)

# Step 3: Sort salaries in descending order
updated_salaries.sort(reverse=True)

# Step 4: Get top 3 highest salaries
top_3 = updated_salaries[:3]

# Display results
print("Processed Salaries:", updated_salaries)
print("Top 3 Highest Salaries:", top_3)