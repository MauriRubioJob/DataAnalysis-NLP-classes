# Write a Python program to find the largest number in a list and print
# it out on the screen. 

numbers = [250, 506, 406, 795, 314, 653, 382, 195, 427, 676, 359, 511, 722, 605, 180, 948, 210, 96, 266, 53]

# Method 1
# maximum = 0
# for n in numbers:
#     if n > maximum:
#         maximum = n

# Method 2
maximum = max(numbers)

# Method 3
# numbers.sort()
# maximum = numbers[len(numbers) - 1]
# maximum = numbers[- 1]


print(maximum)

