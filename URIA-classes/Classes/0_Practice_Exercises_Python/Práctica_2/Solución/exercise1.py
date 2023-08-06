# Write a python program to check if a given number is positive or negative.
# If it's negative. print "negative".
# If it's positive. print "positive".
# If it's neither. print "neither".

# Remember: print only the expected result of the program

num = int(input())
if(num<0):
	print("negative")
elif(num>0):
	print("positive")
elif (num == 0):
	print("neither")