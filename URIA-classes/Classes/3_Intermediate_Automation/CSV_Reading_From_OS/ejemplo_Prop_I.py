# Sección de importar módulo:
import os

# Sección de funciones:


# 1) Función 1: leer el documento externo que yo le introduzca como argumento. Me devuelve el contenido leído
def leer_archivo (documento):
    archivo = open(documento , "r",encoding="utf8")
    contenido = archivo.read()
    archivo.close()
    return contenido


def procesar_texto ( contenido ):

    lineas = contenido.splitlines()

    lista_articulos = []

    texto_articulo = ""


    for linea in lineas:
        if ( ( linea.startswith ( "Artículo" ) and linea.endswith(".") ) or ( linea.startswith("Disposición"))):
                
            lista_articulos.append(texto_articulo)
            texto_articulo = ""

        texto_articulo += linea
        texto_articulo += "\n"

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
    
    for articulo in articulos_ordenados:
        texto = articulo["texto"]
        lineas=texto.splitlines()
        articulo["texto"] = []
        for linea in lineas:
            articulo["texto"].extend(linea.split())
    
    return articulos_ordenados


def extraer_informacion ( articulos , archivo , palabra):
    print(f"\nEn el archivo {archivo} aprece:\n")
    for articulo in articulos:
        if (palabra in articulo["texto"]):
            print("En el artículo {} aparece la palabra {}".format(articulo["título"], palabra) )
            # print("aparece")
        else:
            pass
            # print("No aparece")
            # input()
        # print(articulo)
        # input()
  

def limpiar_extensiones ( lista_archivos ):
    seguir = False
    archivos_limpios = []
    for archivo in lista_archivos:
        if archivo.endswith(".txt"):
            archivos_limpios.append(archivo)
        if "." not in archivo:
            seguir = True
            lista_carpeta = os.listdir(archivo)
            for i in range(len(lista_carpeta)):
                lista_carpeta[i] = archivo+"/"+lista_carpeta[i]
            archivos_limpios.extend(lista_carpeta)
            

    return archivos_limpios, seguir


# Programa Principal:   

lista_archivos = os.listdir(".")

print(type(lista_archivos))
print((lista_archivos))

'''

# Función 1: me limpia los archivo txt y las carpetas
archivos_ordenados = [ txt , carpetas , carpetas ]

# Función 2: viajar a la carpeta que se ha limpia con la función 1

'''

archivos_validos , seguir = limpiar_extensiones ( lista_archivos )
print(archivos_validos)

while(seguir):
    archivos_validos, seguir = limpiar_extensiones(archivos_validos)
    print(archivos_validos)


print("Ha acabado el bucle")

palabra = input("dime la palabra a buscar: ")

for archivo in archivos_validos:
    contenido = leer_archivo( archivo )
    articulos_ordenados = procesar_texto(contenido)

    extraer_informacion (articulos_ordenados , archivo , palabra )

