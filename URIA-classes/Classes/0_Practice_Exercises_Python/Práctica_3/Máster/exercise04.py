# You are given two lists of numbers. Add each number together element by element.
# Print out a total that is the product of the final numbers.

# Example:
#   a = [2, 3, 8]
#   b = [7, 2, 1]
#     2 + 7 = 9
#     3 + 2 = 5
#     8 + 1 = 9
#     9 * 5 * 9 = 405


# POS:	 0, 1, 2, ....                     , 12
list1 = [4, 7, 9, 2, 4, 5, 7, 5, 3, 3, 1, 2, 5]
list2 = [4, 6, 8, 9, 7, 4, 2, 6, 8, 9, 5, 2, 1]


# 1) Crear una lista donde vaya almacenando la suma de los elemento de cada posición de ambas lista.

prod = 1
# 2) Crear un for, cuya variable intermediaria tome los valores de las posiciones de los elementos de las listas y hacer la suma de los elementos y añadirlos a la nueva lista
for i in range ( len (list1)):
    prod *= list1[i]+list2[i]

print(prod)