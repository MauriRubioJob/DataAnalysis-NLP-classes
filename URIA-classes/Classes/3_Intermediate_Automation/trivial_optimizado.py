# Importar los módulo que necesitemos:
import random
import requests


# FUNCIÓN 1: Función que lea el contenido del archivo externo y procese los conjuntos de preguntas y respuestas, y los guarde en una lista.

def procesar_preguntas ( contenido ):


    conjuntos = contenido.split("\n\n")

    procesado = []

    for conjunto in conjuntos:

        # 1) dividir el conjunto en líneas:
        lineas = conjunto.split("\n")
        # Vamos a establecer una condición:
        if len(lineas) < 4:
        # Si el conjunto es inválido, no lo procesamos
            continue

        # Pregunta válida:
        else:

            if lineas[-3].startswith("^"):
                # Preguntas tipo TRUE/FALSE
                pregunta_diccionario = {}
                pregunta_diccionario["B"] = lineas.pop(-1)

                pregunta_diccionario["A"] = lineas.pop(-1)

                pregunta_diccionario["correcta"] = lineas.pop(-1)

                pregunta_diccionario["pregunta"] = "".join(lineas)

                procesado.append(pregunta_diccionario)


            else:
                # Múltiples respuestas (A,B,C,D)
                pregunta_diccionario = {}

                pregunta_diccionario["D"] = lineas.pop(-1)

                pregunta_diccionario["C"] = lineas.pop(-1)

                pregunta_diccionario["B"] = lineas.pop(-1)

                pregunta_diccionario["A"] = lineas.pop(-1)

                pregunta_diccionario["correcta"] = lineas.pop(-1)

                pregunta_diccionario["pregunta"] = "".join(lineas)
                procesado.append(pregunta_diccionario)

        # Al acabar el bucle FOR, en la lista procesado están guardado todos y cada uno de los conjuntos ya procesados.
    return procesado

# Función 2: Función que se encarga de elegir aleatoriamente una pregunta:
def elegir_pregunta (lista_preguntas):
    return random.choice(lista_preguntas)

# Función 3: Función que va a mostrar la pregunta y posibles respuestas al usuario:
def mostrar_pregunta(pregunta):
    print("La pregunta es:")
    print("\n")
    print(pregunta [ "pregunta" ])
    print("Posibles respuestas: ")
    print("\n")
    print(pregunta [ "A" ])
    print(pregunta [ "B" ])

    if "C" in pregunta:
        print(pregunta [ "C" ])
        print(pregunta [ "D" ])
        print("\n")
        print("Introduce tu respuesta ('A' , 'B' , 'C' , 'D' ): ")
    else:
        print("\n")
        print("Introduce tu respuesta ('A' , 'B' ): ")

    respuesta = input()

    return respuesta

# Función 4: Esta función lo que va a  hacer es comprobar el resultado:
def comprobacion ( pregunta, respuesta ):
    resp_usuario = pregunta [ respuesta ][2:]
    resp_correcta = pregunta ["correcta"][2:]

    if resp_usuario == resp_correcta:
        print("HE ACERTADO")
        return True
    else:
        print("Lo siento, no has acertado :(")
        print("La respuesta correcta era: "+resp_correcta)
        return False

# Función 5: Solicitar al usuario la categoría a la que quiere jugar:
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


# PROGRAMA PRINCIPAL

while(True):

    cat = preguntar_categoria()

    contenido = obtener_contenido (cat)

    preguntas = procesar_preguntas( contenido )

    preg = elegir_pregunta ( preguntas )

    resp = mostrar_pregunta (preg)



    if(comprobacion (preg , resp)):
        break
    else:
        print("\nHas fallado :( prueba de nuevo\n\n")

print("Felicidades has ganado el juego")

