# Read the external file named "sentences.txt" and load all of its content
# into a variable. Remember to close the file.
# All of the content must be split first into lines, and then into words,
# so we can comfortably work with it.

# After that, ask the user for a word as a console input.
# If the given word exists in the file, printed out: "It exists", otherwise
# print "It does not exist"

# TIP: If you follow the same name rules and code structure, you can
#      use a lot of the code from exercise 7

# 1) Abrimos el archivo externo, volcamos el contenido en una variable y lo cerramos:

file = open("sentences.txt", "r")
contents = file.read()
file.close()

# 2) Dividimos el contenido en líneas y solicitamos al usuario que introduzca la palabra a buscar:
sentences = contents.splitlines()
looking_for = input()

# 3) Creamos una lista vacía en la que guardar las palabras y con un bucle for vamos recorriendo línea a linea, haciéndole split y guardando las palabras de cada línea en la lista vacía con extend.
# Usamos extend para añadir cosas a la lista vacía porque el resultado de hacerle split a las líneas es una lista, y lo que nos interesa de esa lista son sus elementos y no la lista en si.
words = []
for sentence in sentences:
    words.extend(sentence.split())

# 4) Hacemos el mismo proceso que en el ejercicio 7.
found = False
for word in words:
	if word.startswith(looking_for):
		found = True
		break

if found:
	print("It exists")
else:
	print("It does not exist")
