# Program to delete all occurrences of a number except the first occurrence

# create list of 20 numbers
numbers = [5, 10, 15, 5, 20, 25, 5, 30, 35, 40, 5, 45, 50, 5, 55, 60, 5, 65, 70, 5]

print("Original List:", numbers)

# user input
num = int(input("Enter number to delete its occurrences except first: "))

# check if number exists
if num in numbers:
    first_index = numbers.index(num)   # find first occurrence
    
    # create new list
    new_list = []
    count = 0
    
    for i in numbers:
        if i == num:
            count += 1
            if count == 1:
                new_list.append(i)   # keep first occurrence
        else:
            new_list.append(i)
    
    numbers = new_list

print("Updated List:", numbers)


# Example Output:
# Original List: [5, 10, 15, 5, 20, 25, 5, 30, 35, 40, 5, 45, 50, 5, 55, 60, 5, 65, 70, 5]
# Enter number to delete its occurrences except first: 5
# Updated List: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]





