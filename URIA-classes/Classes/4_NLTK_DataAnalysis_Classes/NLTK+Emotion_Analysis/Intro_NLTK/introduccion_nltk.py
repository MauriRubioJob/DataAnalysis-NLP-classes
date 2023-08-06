# Lo primero que vamos a hacer es dividir una oracion en conjunto de información cómodos y manejables.

# Vamos a importar el módulo "tokenize" del módulo "nltk"
from nltk import tokenize

oracion = "Hola Sr. Mauri, mi nombre es Luis. ¿Cómo está hoy? Me han comentado lo siguiente: Hace sol."

# tokenize, tokenizar algo significa dividir un texto/oración en conjuntos de información útiles.

tokenizado = tokenize.word_tokenize( oracion, language="spanish")
tokenizacion_frases = tokenize.sent_tokenize (oracion)

print("oración tokenizada: ")
print(tokenizado)


palabras = oracion.split()
print("oracióno spliteada: ")
print(palabras)


print("tokenización de frase: ")
print(tokenizacion_frases)


# Para continuar a partir de la tokenización, lo que nos queda es 
# hacer un proceso de limpieza y depuración, que lo haremos el próximo día.



