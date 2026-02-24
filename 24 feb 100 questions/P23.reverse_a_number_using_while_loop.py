# Read input
num = int(input("Enter a number: "))
original_num = num  # Store original number
reversed_num = 0

# Handle negative numbers
is_negative = False
if num < 0:
    is_negative = True
    num = -num

# Reverse the number using while loop
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Restore negative sign if needed
if is_negative:
    reversed_num = -reversed_num

# Print the result
print(f"Reversed number: {reversed_num}")
#---------------------------------------------------

#Input:Input:
#Enter a number: 12345

#Output:
#Reversed number: 54321