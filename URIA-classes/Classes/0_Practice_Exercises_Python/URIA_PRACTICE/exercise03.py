# Using the given list, you must save in a new list all the numbers that
# fullfill all of the following conditions:
#   Numbers that are even
#   Numbers that are greater than 254 (inclusive)
#   Numbers that are less than 582 (exclusive)

# Once the new list is created, print out the sum of the element in
# position 3 and the 7th element


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823,566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687,217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81,379, 843, 831, 445, 742, 717, 958,743, 527]


def is_even(n):
    return n % 2 == 0

# Method 1
# matched = []
# for n in numbers:
#     if is_even(n) and n >= 254 and n < 582:
#         matched.append(n)


# Method 2
def comparison(n):
    return is_even(n) and n >= 254 and n < 582

matched = list(filter(comparison, numbers))



print(matched[3] + matched[6])
