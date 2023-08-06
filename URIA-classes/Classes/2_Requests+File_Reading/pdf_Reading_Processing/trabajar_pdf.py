'''
En este script se detallará la forma en la que podemos trabajar con pdf en python.

Lo primero, vamos a instalar 2 módulos nuevos.

    1) pip install pypdf2
    2) pip install pdfminer.six

Una vez instalados ya los podemos utilizar y trabajar con ellos.

    import  PyPDF2
    import pdfminer

Cada uno de estos módulos es distintos, vamos a estudiar qué diferencias nos aportan.

'''
# Trabajar con pdfminer
'''

1) Importar el módulo
2) abrir con open el archivo externo, modo de lectura binario
3) utilizar sobre el archivo abierto la función correspondiente

'''

# Paso 1)
import pdfminer.high_level

# Paso 2)
archivo = open("Codigo_penal_militar.pdf", "rb")

# Paso 3)
contenido = pdfminer.high_level.extract_text ( archivo )

archivo.close()


# Lo siguiente se encarga de filtrar las cabeceras y 
# números de página del contenido leído del pdf. Todo ello es 
# información que no necesitamos y la filtramos

# Por último, el contenido filtrado se guarda en "volcado.txt"

lineas = contenido.splitlines()

lineas_limpias = []
for linea in lineas:
    if linea.startswith("–") or linea.startswith("§") or linea.startswith("CÓDIGO PENAL Y LEGISLACIÓN COMPLEMENTARIA"):
        continue
    else:
        lineas_limpias.append(linea)



archivo = open("volcado.txt","w")
contenido2 = "\n".join(lineas_limpias)
archivo.write(contenido2)
archivo.close()


#    https://realpython.com/pdf-python/

