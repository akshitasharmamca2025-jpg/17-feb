# List of team points (may include negative points)
points = [45, 60, -10, 30, 75, 50, -5]

# Step 1: Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

# Step 2: Sort leaderboard in descending order
points.sort(reverse=True)

# Step 3: Find winner and runner-up
if len(points) >= 2:
    winner = points[0]
    runner_up = points[1]
elif len(points) == 1:
    winner = points[0]
    runner_up = None
else:
    winner = None
    runner_up = None

# Display results
print("Updated Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)