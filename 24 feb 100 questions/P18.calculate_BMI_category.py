# Read input
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Print result
print("BMI:", round(bmi, 2))
print("Category:", category)
#-------------------------------------------------

#Input:
#Enter weight in kg: 70
#Enter height in meters: 1.75

#Output:
#BMI: 22.86
#Category: Normal weight