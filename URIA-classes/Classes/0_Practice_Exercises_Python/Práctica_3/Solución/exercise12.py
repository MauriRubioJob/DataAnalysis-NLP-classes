'''			ESPAÑOL
Utilizando el archivo externo que contiene el capítulo del libro "Moby Dick", el usuario debe definir una función que devuelva el número de veces que una determinada palabra dada como argumento de la función, aparece en el archivo. Específicamente la palabra va a ser "whale".

Adicionalmente, el usuario va a crear una función que haga el cálculo del promedio de palabras por línea del archivo, y el porcentaje de cuántas veces aparece la palabra "whale" con respecto a todas las palabras.

Por último, el usuario va a escribir cada línea en la que aparecen las palabras "whale", "Whale", "whales", "Whales", en el documento "whaleification.txt".

'''


# SECCIÓN: FUNCIONES
# Cada función debe recibir como argumento la información y datos que necesite para trabajar. (Contenido, líneas, palabras, palabra a buscar...)

# Función 1: Lectura del documento y guardado de contenido en variable a la que luego se le hace return.

def lecturaDoc (documento):
	archivo = open(documento,"r")
	content = archivo.read()
	archivo.close()
	return content

# Función 2: Separación en líneas del contenido del archivo externo y me devuelve la lista de líneas.

def delineador (content):
	return content.split("\n")

# Función 3: Separación en palabras a partir de las líneas y me devuelve la lista de palabras.
def palabrador (lines):
	words = []
	for line in lines:
		words.extend(line.split())
	
	return words

# Función 4: contador de palabras. Recibe como argumento la palabra que nos interesa contar y la lista en la que almacenamos todas las palabras del archivo.
def contador_palabra( words , word):
	count = 0
	for x in words:
		if x == word:
			count +=1
	
	return count

# Función 5: Cálculo de la media de palabras que hay por línea en el documento.

def promedio_palabra_linea (lines , words):
	average = len(words)/len(lines)
	return average

# Función 6: Cálculo del porcentaje de veces que aparece.

def porcentaje_palabra(words, word):
	porcentaje = (contador_palabra(words, word)/len(words) ) * 100
	return porcentaje

# Función 7: Escribir en el archivo externo cualquier linea en la que aparezca las palabras...

def escribir_palabras (document, lines):
	# Abrimos el documento modo escritura ('w')
	archivo = open(document, 'w')

	lista_palabras = ["whale","Whale","whales","Whales"]

	for line in lines:
		for word in line.split():
			if word in lista_palabras:
				archivo.write(line+"\n")
	
	archivo.close()

# SECCIÓN: VARIABLES

# SECCIÓN: PROGRAMA PRINCIPAL

# Abrir el archivo y leer el contenido
contenido = lecturaDoc("Moby Dick.txt")

# Distinguir las líneas del contenido:
lineas = delineador(contenido)

# Obtener la lista de palabras:
palabras = palabrador(lineas)

# Contar cuántas veces aparece la palabra "whale"
print(contador_palabra(palabras , "whale"))

# promedio palabras / linea:
print(promedio_palabra_linea(lineas , palabras))

# Calcular porcentaje:
print(porcentaje_palabra(palabras,"whale"))

# Escribir palabras en el documento:
escribir_palabras("whaleification.txt" , lineas)