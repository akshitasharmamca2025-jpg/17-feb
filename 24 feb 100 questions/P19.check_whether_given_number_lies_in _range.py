# Read input
number = float(input("Enter the number: "))
lower = float(input("Enter the lower bound: "))
upper = float(input("Enter the upper bound: "))

# Check if number is within range
if lower <= number <= upper:
    print(f"{number} lies within the range [{lower}, {upper}]")
else:
    print(f"{number} does not lie within the range [{lower}, {upper}]")
    #.....................................................

    #Input:
#Enter the number: 15
#Enter the lower bound: 10
#Enter the upper bound: 20

#Output:
#15.0 lies within the range [10.0, 20.0]