# Read three numbers from standard input
a, b, c = map(int, input().split())

# Find the largest number
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
#--------------------------------------


    #input: 10
    25
    20
    #output: 25
