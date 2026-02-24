# Read number from input
num = int(input())

# Initialize reversed number
rev = 0
n = num  # Keep a copy of the original number

# Reverse the number
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

# Print the reversed number
print(rev)
#-----------------------------------------

#input: 12345
#output: 54321