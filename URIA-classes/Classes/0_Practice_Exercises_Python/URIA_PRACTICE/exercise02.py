# Write a Python program to count how many times a number appears in a
# given list.

numbers = [2, 1, 34, 4, 4, 5, 6, 43, 45, 2, 24, 3, 4, 4, 324, 53, 4]
looking_for = int(input())

# Method 1
# count = 0
# for n in numbers:
#     if n == looking_for:
#         count = count + 1

# Method 2
count = numbers.count(looking_for)

print(count)
