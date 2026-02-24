def analyze_marks(marks):
    # Remove invalid marks (less than 0 or greater than 100)
    valid_marks = [mark for mark in marks if 0 <= mark <= 100]
    
    if not valid_marks:
        return "No valid marks available."
    
    # Calculate average
    average = sum(valid_marks) / len(valid_marks)
    
    # Find topper(s)
    highest_mark = max(valid_marks)
    toppers = [mark for mark in valid_marks if mark == highest_mark]
    
    # Determine grade based on average
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
    
    # Output results
    results = {
        "valid_marks": valid_marks,
        "average": average,
        "topper(s)": toppers,
        "grade": grade
    }
    
    return results

# Example usage:
marks = [45, 78, 100, 150, -5, 89, 99, 72]
result = analyze_marks(marks)
print(result)


#input :
marks = [45, 78, 100, 150, -5, 89, 99, 72]

#output : 
{
    'valid_marks': [45, 78, 100, 89, 99, 72],
    'average': 80.5,
    'topper(s)': [100],
    'grade': 'B'
}