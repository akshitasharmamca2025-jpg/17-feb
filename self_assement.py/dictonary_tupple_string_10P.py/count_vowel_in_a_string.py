text = "Python Programming"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
#-------------------------------------------

#output:Number of vowels: 4
