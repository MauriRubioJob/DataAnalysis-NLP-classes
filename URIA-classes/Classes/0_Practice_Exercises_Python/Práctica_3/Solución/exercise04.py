# You are given two lists of numbers. Add each number together element by
# element.
# Print out a total that is the product of the final numbers.

# Example:
#   a = [2, 3, 8]
#   b = [7, 2, 1]
#     2 + 7 = 9
#     3 + 2 = 5
#     8 + 1 = 9
#     9 * 5 * 9 = 405

list1 = [4, 7, 9, 2, 4, 5, 7, 5, 3, 3, 1, 2, 5]
list2 = [4, 6, 8, 9, 7, 4, 2, 6, 8, 9, 5, 2, 1]

# Crear una lista donde vaya almacenando la suma de los elemento de cada posición de ambas lista.
suma = []

# Crear un for, cuya variable itnermediaria tome los valores de las posiciones de los elementos de las listas.

for i in range(len(list1)):
    suma.append(list1[i] + list2[i])


total = 1
for n in suma:
    total = total * n

print(total)
