# El siguiente programa realiza y contiene todas las funciones necesarias para desarrollar el juego de trivia.
# Se deberá realizar los siguiente:
# 1) Modificar la función "preguntar_categoria()" para que la elección no dependa del usuario, si no que se realice una elección aleatoria.
# 2) Hacer que el programa se ejecute infinitamente hasta que se acierte correctamente a la pregunta que se le realice al usuario.


import random
import requests

#################################################################

# SECCIÓN FUNCIONES:

def procesar_preguntas ( contenido ):
	conjuntos = contenido.split("\n\n")
	procesado = []

	for conjunto in conjuntos:
		lineas = conjunto.split("\n")
		if len(lineas) < 4:
			continue
		else:
			if lineas[-3].startswith("^"):
				pregunta_diccionario = {}
				pregunta_diccionario["B"] = lineas.pop(-1)
				pregunta_diccionario["A"] = lineas.pop(-1)
				pregunta_diccionario["correcta"] = lineas.pop(-1)
				pregunta_diccionario["pregunta"] = "".join(lineas)
			else:
				pregunta_diccionario = {}
				pregunta_diccionario["D"] = lineas.pop(-1)
				pregunta_diccionario["C"] = lineas.pop(-1)
				pregunta_diccionario["B"] = lineas.pop(-1)
				pregunta_diccionario["A"] = lineas.pop(-1)
				pregunta_diccionario["correcta"] = lineas.pop(-1)
				pregunta_diccionario["pregunta"] = "".join(lineas)

			procesado.append(pregunta_diccionario)

	return procesado

def elegir_pregunta (lista_preguntas):
	return random.choice(lista_preguntas)

def mostrar_pregunta(pregunta):
	print("La pregunta es:\n{}".format(pregunta['pregunta']))
	print("Posibles respuestas:\n")
	print(pregunta [ "A" ]);print(pregunta [ "B" ])

	if "C" in pregunta:
		print(pregunta [ "C" ]);print(pregunta [ "D" ])
		print("\nIntroduce tu respuesta ('A' , 'B' , 'C' , 'D' ): ")
	else:
		print("\nIntroduce tu respuesta ('A' , 'B' ): ")
	
	respuesta = input()
	return respuesta


def comprobacion ( pregunta, respuesta ):
	resp_usuario = pregunta [ respuesta ][2:]
	resp_correcta = pregunta ["correcta"][2:]

	if resp_usuario == resp_correcta:
		print("HE ACERTADO")
	else:
		print("Lo siento, no has acertado :(")
		print("La respuesta correcta era: "+resp_correcta)


def preguntar_categoria():
	lista_categorias = ["music", "people" , "general" , "history" , "movies", "humanities" , "literature"]
	
	print("Elige una categoría de entre las siguientes: " , lista_categorias)

	print("\n")

	categoria = input()

	if categoria in lista_categorias:
		return categoria
	else:
		return preguntar_categoria()

def obtener_contenido (categoria):
	url_base = "https://raw.githubusercontent.com/uberspot/OpenTriviaQA/master/categories/"
	url_obtener = url_base + categoria
	respuesta = requests.get (url_obtener)
	
	if respuesta.status_code == 200:
		print("success")
		return respuesta.text
	else:
		print("Problema")

#################################################################


# SECCION: PROGRAMA PRINCIPAL

# Solicitar al usuario que me indique una categoría:
cat = preguntar_categoria()

# En función de la categoria elegida, vamos a cargar un contenido u otro con request
cont = obtener_contenido(cat)

preguntas = procesar_preguntas ( cont )
preg = elegir_pregunta ( preguntas )
resp = mostrar_pregunta (preg)

# Vamos a checkear si la respuesta del usuario es acertada o no:
comprobacion (preg , resp)
