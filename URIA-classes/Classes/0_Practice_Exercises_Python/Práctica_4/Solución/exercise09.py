# Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# Sample string : 'tres tristes tigres'
# Expected result = {
# 	't' : 4,
# 	'r' : 3,
# 	'e' : 3,
# 	's' : 4,
# 	' ' : 2,
# 	'i' : 2,
# 	'g' : 1
# }

oracion = 'tres tristes tigres'

my_dict = {}

for car in oracion:
	if car in my_dict:
		my_dict[car] += 1
	else:
		my_dict[car] = 1

print(my_dict)