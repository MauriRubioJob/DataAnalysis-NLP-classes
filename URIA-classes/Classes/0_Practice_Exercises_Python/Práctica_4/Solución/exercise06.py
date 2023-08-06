#  Write a Python program to get the maximum and minimum value in a dictionary. Then print out the substraction of maximum - min

my_dict = {'x':500, 'y':5874, 'z': 560}

mayor = max(my_dict)
menor = min(my_dict)

# for x in my_dict:

# 	if my_dict[x]>mayor:
# 		mayor = my_dict[x]
# 	if my_dict[x]<menor:
# 		menor = my_dict[x]
	
print(my_dict[mayor] - my_dict[menor])