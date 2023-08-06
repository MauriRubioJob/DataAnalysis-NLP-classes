# Create a Python program that counts how many words in a given string.


oracion = "Por lo tanto, inicializaremos la posición, después utilizaremos una estructura repetitiva para que se mueva hacia delante, rebote si toca un borde y gire un poco de forma aleatoria."

# Partimmos de una oración (una línea). Es aoración debemos ir partiendo palabra a palabra, divididas por un espacio.
# El método que usarmeos será: split()

palabras = oracion.split()

# Palabras es 1 lista, donde cada elemento es 1 palabra. Para saber cuántos elemento (palabras) tengo, tendré que utilizar la función que me determina la longiitud de mi lista:

numero_de = len(palabras)
print(numero_de)
