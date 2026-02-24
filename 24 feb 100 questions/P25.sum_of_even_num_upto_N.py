# Read input
N = int(input("Enter a positive integer N: "))

# Initialize sum
sum_even = 0
i = 2  # Start from the first even number

# Use while loop to sum even numbers
while i <= N:
    sum_even += i
    i += 2  # Move to the next even number

# Print the result
print("Sum of even numbers up to", N, "is:", sum_even)
#-------------------------------------------------------

#Input:
#Enter a positive integer N: 10

#Output:
#Sum of even numbers up to 10 is: 30