# List of product stock quantities
stock = [0, 5, 20, 8, 50, 0, 3, 15]

# Step 1: Remove items with 0 stock
available_stock = []
for item in stock:
    if item > 0:
        available_stock.append(item)

# Step 2: Add restock of 50 units to items below 10
for i in range(len(available_stock)):
    if available_stock[i] < 10:
        available_stock[i] += 50

# Step 3: Find total inventory count
total_inventory = sum(available_stock)

# Display results
print("Updated Stock List:", available_stock)
print("Total Inventory Count:", total_inventory)