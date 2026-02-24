# List of transactions (positive = deposit, negative = withdrawal)
transactions = [15000, -5000, 20000, -12000, 8000, -3000, 25000]

# Step 1: Calculate total balance
total_balance = sum(transactions)

# Step 2: Find largest withdrawal
largest_withdrawal = 0
for t in transactions:
    if t < 0:  # Only withdrawals
        if t < largest_withdrawal:
            largest_withdrawal = t

# Step 3: Count number of deposits greater than ₹10,000
deposit_count = 0
for t in transactions:
    if t > 10000:
        deposit_count += 1

# Display results
print("Total Balance:", total_balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits Greater Than ₹10,000:", deposit_count)