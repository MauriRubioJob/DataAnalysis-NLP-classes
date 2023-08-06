# Write a Python program that tells you, in a given string, how many words
# appear more than once.

# Example:
#   "The Python programming language, named after British comedy group
#    Monty Python, is a general-purpose language that supports multiple 
#    paradigms. The reference implementation is built using the C
#    programming language."

#   Words: the, python, programming, language, is -> 5

# To simplify things in this case, use a pre-formatted sentence with all
# punctuation removed and uppercase letters converted.

sentence = "the python programming language named after british comedy group monty python is a general purpose language that supports multiple paradigms the reference implementation is built using the c programming language"

# 1) dividir la oración en palabras y guardarlas en una lista:
palabras = sentence.split()

# 2) Crear una lista nueva donde vamos a guardar aquellas palabras que aparezcan más de 1 vez:
duplicadas = []

for word in palabras:

	# 3) Si la cuennta > 1 -> sí nos interesa.
	# Otra condición: Que no esté ya anotada en la lista "duplicadas"
	if ( palabras.count(word) > 1 ) and ( not word in duplicadas  ) :
		duplicadas.append(word)

# Imprimimos la cantidad de palabras duplicadas.

print(len(duplicadas))