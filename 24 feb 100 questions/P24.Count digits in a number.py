# Read input
num = int(input("Enter a number: "))

# Handle negative numbers
num = abs(num)

# Initialize count
count = 0

# Special case for 0
if num == 0:
    count = 1
else:
    # Count digits using while loop
    while num > 0:
        num //= 10
        count += 1

# Print the result
print("Number of digits:", count)
#---------------------------------------------

#Input:
#Enter a number: 12345

#Output:
#Number of digits: 5