# Using the given list, you must save in a new list all the numbers that
# fullfill all of the following conditions:
#   Numbers that are even
#   Numbers that are greater than 254 (inclusive)
#   Numbers that are less than 582 (exclusive)

# Once the new list is created, print out the sum of the element in
# position 3 and the 7th element


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823,566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687,217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81,379, 843, 831, 445, 742, 717, 958,743, 527]


# Crear la lista nueva donde vamos a volver los elementos que cumplan la condición.
lista_nueva = []


# Vamos a hacer un bucle for que recorra toda la lista original.
for n in numbers:

	# Vamos a preguntarnos si el elemento actual cumple las 3 condiciones.
	if n%2 == 0 and n>=254 and n<582:
		# Guardar el elemento actual en la lista nueva:
		lista_nueva.append(n)

# Sumar elemento en la pos 3 y el 7º elemento:
# Posiciones 0 al total -1
# Elementos van del 1 al total
# Elemento en la pos 3 : lista_nueva[3]
# 7º elemento:           lista_nueva[6]

print(lista_nueva[3] + lista_nueva[6])