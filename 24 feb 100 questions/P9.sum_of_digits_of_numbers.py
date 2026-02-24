# Read the number from input
num = int(input())

# Initialize sum
sum_digits = 0

# Calculate sum of digits
while num > 0:
    sum_digits += num % 10
    num //= 10

# Print the result
print(sum_digits)
#------------------------------

#input:1234
#output: 10