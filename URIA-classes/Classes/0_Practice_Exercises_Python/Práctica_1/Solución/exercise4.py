#  Write a Python program to calculate the sum of three given numbers.
#  If the all three numbers are equal, then return 3 times their sum.
#  
number1 = int(input())
number2 = int(input())
number3 = int(input())
if(number1==number2 and number2==number3):
		print(number1*9)
else:
		print(number1+number2+number3)