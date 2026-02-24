# Daily temperatures of a month (sample data)
temperatures = [35, 42, 39, 46, 38, 41, 44, 30, 47, 36]

# Step 1: Find hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)

# Step 2: Replace temperatures above 45°C with "Heat Alert"
updated_temperatures = []

for temp in temperatures:
    if temp > 45:
        updated_temperatures.append("Heat Alert")
    else:
        updated_temperatures.append(temp)

# Step 3: Count number of extreme days (> 40°C)
extreme_days = 0
for temp in temperatures:
    if temp > 40:
        extreme_days += 1

# Display results
print("Hottest Temperature:", hottest)
print("Coldest Temperature:", coldest)
print("Updated Temperature List:", updated_temperatures)
print("Number of Extreme Days (>40°C):", extreme_days)