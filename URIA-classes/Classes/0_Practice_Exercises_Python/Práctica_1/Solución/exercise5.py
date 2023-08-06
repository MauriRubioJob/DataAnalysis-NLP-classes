#  Write a Python program to find whether a given number is odd or even.
#  Print either "odd" or "even".
#  Note: The % operator can tell you the remainder from a division.
#  Example:
#    10 / 3 = 3.3333333
#    10 % 3 = 1
#    21 / 2 = 10.5
#    21 % 2 = 1
#    15 % 3 = 3

Given_num = int(input())
if(Given_num%2 == 0):
		print("even")
else: 
		print("odd")