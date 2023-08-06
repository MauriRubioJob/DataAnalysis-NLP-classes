# Using the module random, you must create a list of 1000 elements of random values between 1 and 10. After creating it, you have to loop through the list, and calculate the average of the sum of all the elements.
# Once that is done, round the result and print it.

import random

lista = []

for i in range(100):
	lista.append(random.randint(1,10))

suma = 0

for num in lista:
	suma += num

print(round(suma/100))
