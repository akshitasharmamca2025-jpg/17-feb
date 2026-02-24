# Read input
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if it is a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Classify by sides
    if a == b == c:
        triangle_type = "Equilateral triangle"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles triangle"
    else:
        triangle_type = "Scalene triangle"
    
    # Optional: classify by angles using Pythagorean theorem
    sides = sorted([a, b, c])
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6:
        angle_type = "Right-angled triangle"
    elif sides[0]**2 + sides[1]**2 > sides[2]**2:
        angle_type = "Acute-angled triangle"
    else:
        angle_type = "Obtuse-angled triangle"
    
    print(triangle_type)
    print(angle_type)
else:
    print("Not a valid triangle")
    #--------------------------------------

    #input: 
#Enter first side: 3
#Enter second side: 4
#Enter third side: 5

#Output:
#Scalene triangle
#Right-angled triangle