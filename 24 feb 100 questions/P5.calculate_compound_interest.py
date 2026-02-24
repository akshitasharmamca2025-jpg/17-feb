# Calculate Compound Interest

P = float(input())
R = float(input())
T = float(input())

A = P * (1 + R/100) ** T
CI = A - P

print("Compound Interest =", CI)
#--------------------------------------------

#input: 1000
5
2

#output: Compound Interest = 102.5