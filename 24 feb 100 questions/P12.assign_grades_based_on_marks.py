# Read marks from input
marks = float(input())

# Assign grade based on marks
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the grade
print(grade)
#---------------------------------

#input: 85
#output: B