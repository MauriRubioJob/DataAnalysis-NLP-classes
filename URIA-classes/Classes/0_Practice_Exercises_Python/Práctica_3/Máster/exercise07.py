# Create a Python program that tells the user if any word in a string starts with a chosen letter.

# First create a list of words, and then check one by one if each word
# "startswith()" the given letter. If any single word matches, print
# "It exists" and stop searching. Otherwise if no words match, print
# "It does not exist"


oracion = "Cuando no hay un campo magnético externo, estos imanes atómicos tienen una orientación aleatoria, de modo que sus efectos se contrarrestan."

# split: string -> lista 
palabras = oracion.split()

letra = input()

# 1) Vamos a crear una variable para informar al programa de si se ha encontrado coincidencia o no.
# 0 -> no se ha encontrado coincidencia.
# 1 -> sí se ha encontraod coincidencia.


# 2) Para comprobar cada palabra 1 a 1 utilizamos un for.


	# 3) Queremos preguntar si la palabra actual, empieza con la letra introducida por el usuario:


# 4) Debemos imprimir el resultaod dependiendo de si se ha encontrado la palabra o no:

