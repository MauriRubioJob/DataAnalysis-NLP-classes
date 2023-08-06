# Create a Python program that counts how many words in a given string.


oracion = "Por lo tanto, inicializaremos la posición, después utilizaremos una estructura repetitiva para que se mueva hacia delante, rebote si toca un borde y gire un poco de forma aleatoria."

# Method 1
palabras = oracion.split()
numero_de = len(palabras)

# Method 2
# numero_de = oracion.count(" ") + 1

print(numero_de)
