# Write a Python program to count how many times a number appears in a
# given list.

numbers = [2, 1, 34, 4, 4, 5, 6, 43, 45, 2, 24, 3, 4, 4, 324, 53, 4]
looking_for = int(input())

# Vamos a crear una varibale que me almacene la cuenta
cuenta = 0

# # FORMA 1:
# # Vamos a crear un bucle for para consultar todos los elementos de la lista
# for n in numbers:

# 	# Internamente nos preguntaremos si el número introducido por el usuario coincide con el elemento actual que estemos analizando.
	# if n == looking_for:

# 		# Si la repsuesta a esa pregunta es afirmativa -> cuenta += 1
# 		cuenta = cuenta + 1


# FORMA 2: Utilizar el método count
cuenta = numbers.count(looking_for)

# Imprimimos el resultado:

print(cuenta)
