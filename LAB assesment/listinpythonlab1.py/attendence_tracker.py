# Attendance list (1 = Present, 0 = Absent)
attendance = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]

# Step 1: Calculate attendance percentage
total_days = len(attendance)
present_days = sum(attendance)
percentage = (present_days / total_days) * 100

# Step 2: Check if attendance is below 75%
if percentage < 75:
    below_75 = True
else:
    below_75 = False

# Step 3: Replace consecutive absences with warning flag
attendance_flagged = attendance.copy()

for i in range(len(attendance_flagged) - 1):
    if attendance_flagged[i] == 0 and attendance_flagged[i + 1] == 0:
        attendance_flagged[i] = "⚠"
        attendance_flagged[i + 1] = "⚠"

# Display results
print("Attendance Percentage:", round(percentage, 2), "%")
print("Below 75%:", below_75)
print("Attendance with Warning Flags:", attendance_flagged)