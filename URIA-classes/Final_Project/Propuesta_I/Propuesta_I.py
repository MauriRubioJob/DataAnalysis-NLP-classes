'''
En este script se desarrolla la resolución de la propuesta I.
'''

# Sección de importar módulos.
import spacy




# 1) Función 1: leer el documento externo que yo le introduzca como argumento. Me devuelve el contenido leído
def leer_archivo (documento):
    archivo = open(documento , "r",encoding="utf8")
    contenido = archivo.read()
    archivo.close()
    return contenido





# 2) Ordenar la info en una variable apropiada
def procesar_articulos (contenido):

    lineas = contenido.splitlines()
    articulos_ordenados = []
    dic_art = { "título" : 0 , "texto" : "" }

    for linea in lineas:
        if len(linea)<11:
            dic_art["texto"] += linea+"\n"
        else:
            CON1 = linea.startswith ( "Artículos " )
            CON2 = linea.endswith(".")
            CON3 = linea[10].isdigit()

            CON4 = linea.startswith("Disposición")

            CON5 = linea.startswith ( "Artículo " )
            CON6 = linea[9].isdigit()

            if ( (CON1 and CON2 and CON3) or (CON4 and CON2) or (CON5 and CON2 and CON6) ):
                
                articulos_ordenados.append(dic_art)
                dic_art = { "título" : linea , "texto" : "" }
            else:
                dic_art["texto"] += linea+"\n"

    articulos_ordenados.pop(0)

    return articulos_ordenados


# 3) Pase por nltk (spacy) el texto de cada artículo

def procesar_spacy (articulos_ordenados):

    for articulo in articulos_ordenados:
        texto_procesado_con_spacy = es_parser( articulo["texto"] )
        articulo["texto"] = []
        for palabra in texto_procesado_con_spacy:
            articulo["texto"].append(palabra.lemma_)
    
    return articulos_ordenados

def procesar_texto_articulo (articulos_original):
    
    for articulo in articulos_original:
        lineas = articulo["texto"].splitlines()
        articulo["texto"] = []
        for linea in lineas:
            articulo["texto"].extend(linea.split())
    
    return articulos_original

def extraer_info(articulos , palabras):
    
    for articulo in articulos:
        encontrado = "NO"
        for palabra in palabras:
            if(palabra in articulo["texto"]):
                encontrado = "SÍ"
            else:
                encontrado = "NO"
                break
        if encontrado != "NO":
            print(f"En el artículo {articulo['título']} se encuentras las palabras {palabras}")







contenido = leer_archivo("Archivo_Propuesta_I.txt" )

articulos_original = procesar_articulos (contenido)

# es_parser = spacy.load("es_core_news_md")
# articulos_spacy = procesar_spacy (articulos_original)
articulo_texto_procesado = procesar_texto_articulo ( articulos_original)

palabras = []
while(True):
    pal = input("Introduce la palabra a buscar (enter para parar): ")
    if (pal == "" and palabras != []):
        break
    else:
        palabras.append(pal)

extraer_info(articulos_original , palabras)
# extraer_info(articulos_spacy , palabras)

