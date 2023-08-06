# Write a Python program that tells you, in a given string, how many words appear more than once.

# Example:
#   "The Python programming language, named after British comedy group Monty Python, is a general-purpose language that supports multiple paradigms. The reference implementation is built using the C programming language."

#   Words: the, python, programming, language, is -> 5


# To simplify things in this case, use a pre-formatted sentence with all punctuation removed and uppercase letters converted.

sentence = "the python programming language named after british comedy group monty python is a general purpose language that supports multiple paradigms the reference implementation is built using the c programming language"

# 1) dividir la oración en palabras y guardarlas en una lista:
palabras = sentence.split()

# print(palabras)


# 2) Crear una lista nueva donde vamos a guardar aquellas palabras que aparezcan más de 1 vez:


	# 3) Si la cuenta > 1 -> sí nos interesa.
	# Otra condición: Que no esté ya anotada en la lista "duplicadas"

print(duplicadas)