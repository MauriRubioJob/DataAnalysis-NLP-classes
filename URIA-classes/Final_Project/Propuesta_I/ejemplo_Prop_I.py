'''
esta es la propuesta perosnal
del  ...

'''
# Sección de importar módulos.
import spacy


# es_parser = spacy.load("es_core_news_md")

# 1) Función 1: leer el documento externo que yo le introduzca como argumento. Me devuelve el contenido leído
def leer_archivo (documento):
    archivo = open(documento , "r",encoding="utf8")
    contenido = archivo.read()
    archivo.close()
    return contenido

contenido = leer_archivo("Articulos_Sociedades_Capital.txt" )



# 2) Ordenar la info en una variable apropiada

lineas = contenido.splitlines()

# print(len(lineas))


'''
En qué tipo de variable vamos a guardar toda la información.
Mucha información -> lista / diccionarios.

articulos_ordenados = [ 
                            {"Nº_Artículo": 1 , 
                            "Texto_Artículo": " ...... " } , 

                            {"Nº Artículo": 2 ,     
                            "Texto_Artículo": " ..... "} , 
                            ..... 
                            ]
'''
lista_articulos = []

texto_articulo = ""

# Vamos a diseñar un for para recorrer las líneas 1 a 1

for linea in lineas:
    if ( ( linea.startswith ( "Artículos " ) and linea.endswith(".") and linea[10].isdigit() ) or ( linea.startswith("Disposición") and linea.endswith("."))):
        linea_modif = linea.replace("Artículo ","")
        print(linea_modif)
        if (linea_modif [0].isdigit()):
            
            input()
            lista_articulos.append(texto_articulo)
            texto_articulo = ""

    texto_articulo += linea
    texto_articulo += "\n"
    # print(texto_articulo)



input() 

# print((lista_articulos[50]))
lista_articulos.pop(0)

articulos_ordenados = []

for articulo in lista_articulos:
    lineas_articulo = articulo.splitlines()
    
    dic_art = {
        "título" : 0,
        "texto" : ""
    }
    for linea in lineas_articulo:
        if linea.startswith("Artículo") or linea.startswith("Disposición"):
            dic_art["título"] = linea
        else:
            dic_art["texto"] += linea + " "
    
    articulos_ordenados.append(dic_art)

# for i in range(70):

#     print(lista_articulos[i])
#     print(articulos_ordenados[i])
#     input()
print(lista_articulos[1])
print(articulos_ordenados[1])

# 3) Pase por nltk (spacy) el texto de cada artículo
for articulo in articulos_ordenados:
    texto_procesado_con_spacy = es_parser( articulo["texto"] )
    articulo["texto"] = []
    for palabra in texto_procesado_con_spacy:
        articulo["texto"].append(palabra.lemma_)


print(articulos_ordenados[1])

for articulo in articulos_ordenados:
    if ("habilitar" in articulo["texto"] and "crédito" in articulo["texto"]):
        print("En el artículo", articulo["título"], "aparecen las palabras habilitar y crédito")


