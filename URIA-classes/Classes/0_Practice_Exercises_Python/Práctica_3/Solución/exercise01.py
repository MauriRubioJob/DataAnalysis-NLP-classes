# Write a Python program to find the largest number in a list and print
# it out on the screen. 

numbers = [250, 506, 406, 795, 314, 653, 382, 195, 427, 676, 359, 511, 722, 605, 180, 948, 210, 96, 266, 53]


# Vamos a crear una variable que almacene el número más grande.
# Al empezar, el número mayor es el primer elemento (posición 0).
maximo = numbers[0]

# FORMA 1: Utilizando un bucle for y haciendo preguntas con un if.
for n in numbers:
	if n > maximo:
		maximo = n

# FORMA 2: Utilizando el método sort.
# Sort nos permite ordenar las listas de menor a mayor

# El número más grande es el que está en la última posición.
# Última posicion = len(lista) - 1

# numbers.sort()
# maximo = numbers[len(numbers) - 1]
# maximo = numbers[- 1]

# Imprimir el resultado del número más grande:


# Método 3: Usando la instrucción max()
maximo = max(numbers)


print(maximo)

