'''
Utilizando el archivo externo que contiene el capítulo del libro "Moby Dick", 
el usuario debe definir una función que devuelva el número de veces que una 
determinada palabra dada como argumento de la función, aparece en el archivo. 
Específicamente la palabra va a ser "whale".

Adicionalmente, el usuario va a crear una función que haga el cálculo del 
promedio de palabras por línea del archivo, y el porcentaje de cuántas veces 
aparece la palabra "whale" con respecto a todas las palabras.

Por último, el usuario va a escribir cada línea en la que aparecen 
las palabras "whale", "Whale", "whales", "Whales", en el documento 
"whaleification.txt".
'''


from string import punctuation

# 1) función que me abra el archivo externo y me lea el contenido
def abrir_archivo(documento):

    with open(documento,"r",encoding="utf8") as archivo:
        contenido = archivo.read()

    return contenido

# 2) función que me obtenga las líneas que tiene el documento
def obtener_lineas(contenido):
    return contenido.splitlines()

# 3) función que me obtenga las palabras del documento
def obtener_palabras(lineas):
    palabras = []
    for linea in lineas:
        palabras.extend( linea.split() )
    
    return palabras

def procesar_texto (documento):
    with open(documento,"r",encoding="utf8") as archivo:
        contenido = archivo.read()
    
    for punct in punctuation:
        contenido = contenido.replace(punct , "")
    lineas = contenido.splitlines()

    palabras = []
    for linea in lineas:
        palabras.extend( linea.split() )
    
    return contenido , lineas , palabras


# 4) función que me cuente cuántas veces aparece la palabra "whale"
def contar_palabra ( palabra_contar , palabras ):

    cuenta = palabras.count( palabra_contar )
    return cuenta

# 5) función que me dé el promedio de palabras/línea
def promedio ( long_lineas , long_palabras ):
    prom =  long_palabras / long_lineas 
    return prom

# 6) función que me dé el porcentaje de veces que aparece una cierta palabra
def porcentaje ( palabra , palabras ):
    porc = contar_palabra ( palabra , palabras ) / len(palabras) * 100

    return porc


# 7) función que  me escriba en un doc externo las líneas en las que aprece cierta 
# palabra
def extraer_info ( documento , lineas , palabra ):

    # 1) abrir el documento en modo escritura:
    # with open(documento , "w" ) as archivo:
    archivo = open(documento , "w")
    for linea in lineas:
        palabras = linea.split()
        plural = palabra+"s"

        CON1 = palabra in palabras
        CON2 = plural in palabras
        CON3 = palabra.capitalize() in palabras
        CON4 = plural.capitalize() in palabras

        if   CON1 or CON2 or CON3 or CON4:
            
            archivo.write(linea+"\n")
            
    archivo.close()
    
    print("Ya ha acabado")

    # No devolvemos nada.



# Programa principal

# contenido = abrir_archivo("Moby Dick.txt")
# lineas = obtener_lineas(contenido)
# palabras = obtener_palabras(lineas)

contenido , lineas , palabras = procesar_texto ("Moby Dick.txt")

# palabras = obtener_palabras(    obtener_lineas(  abrir_archivo("Moby Dick.txt")    )    )


cuenta_whale = contar_palabra("whale" , palabras )
print(f"whale aparece en el texto {cuenta_whale} veces")

cuenta_city = contar_palabra("city" , palabras )
print(f"city aparece en el texto {cuenta_city} veces")

print(f"el promedio de pal/lin es: { promedio ( len(lineas) , len(palabras) ) }")

palabra = "whale"
print(f"la palabra {palabra} aparece un { porcentaje(palabra, palabras)} % de veces en el texto")

palabra = "city"
print(f"la palabra {palabra} aparece un { porcentaje(palabra, palabras)} % de veces en el texto")

extraer_info("whaleification.txt",lineas ,"whale")


