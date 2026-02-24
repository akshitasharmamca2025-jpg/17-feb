# Read input
n = int(input("Enter a non-negative integer: "))

# Initialize factorial
factorial = 1
i = 1

# Calculate factorial using while loop
while i <= n:
    factorial *= i
    i += 1

# Print the result
print(f"Factorial of {n} is {factorial}")
#-------------------------------------------

#Input:
#Enter a non-negative integer: 5

#Output:
#Factorial of 5 is 120