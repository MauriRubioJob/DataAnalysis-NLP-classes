# Write a Python program to calculate the total of all the items in a
# list using a for loop.

numbers = [91, 156, 98, 79, 62, 44, 164, 73, 7]

# Method 1
total = 0
for n in numbers:
    total = total + n

# Method 2
# total = sum(numbers)

print(total)
