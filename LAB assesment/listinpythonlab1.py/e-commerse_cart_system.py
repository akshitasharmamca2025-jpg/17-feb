# E-Commerce Cart System

# Taking input from user
prices = list(map(float, input("Enter product prices separated by space: ").split()))

# 1. Remove duplicate items
unique_prices = list(set(prices))

# 2. Calculate total
total = sum(unique_prices)

# 3. Apply 10% discount if total > 5000
if total > 5000:
    discount = total * 0.10
    total -= discount
    print("Discount Applied: ₹", discount)
else:
    print("No Discount Applied")

# 4. Add GST 18%
gst = total * 0.18
final_amount = total + gst

# 5. Display final payable amount
print("GST (18%): ₹", gst)
print("Final Payable Amount: ₹", final_amount)

#input:
#Enter product prices separated by space: 2000 1500 2000 1800

#output:
#No Discount Applied
#GST (18%): ₹ 540.0
#Final Payable Amount: ₹ 3540.0