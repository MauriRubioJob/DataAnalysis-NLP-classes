'''
vamos a hacer un ejemplo para ver las herramientas necesarias para la propuesta 3.





'''
# Camino largo:

# archivo = open("imdb.csv" , "r" , encoding="utf8" )

# contenido = archivo.read()

# archivo.close()


# lineas = contenido.splitlines()

# # print(lineas[0])


# datos_celdas = []
# for linea in lineas:
#     datos_celdas.append( linea.split(",") )

# print("\n")
# # print(datos_celdas[0])


# '''
# dic_csv = {
#     "color" : [ ...... ],
#     "director_name" : [  .... ],
#     ...
# }

# '''

# dic_csv = {}
# for celda in datos_celdas[0]:
#     dic_csv [celda] = []

# # print(dic_csv)
# datos_celdas.pop(0)

# for fila in datos_celdas:
#     index = 0
#     for key in dic_csv:
#         dic_csv[key].append( fila[ index ] )
#         index += 1


# contador_color = 0
# contador_bn = 0

# for color in dic_csv["color"]:
#     if color == "Color":
#         contador_color += 1

#     elif color == " Black and White":
#         contador_bn += 1

# print("pelis de color hay" , contador_color)
# print("pelis de bn hay" , contador_bn)





# Camino corto

import csv

archivo = open("imdb.csv" , "r" , encoding="utf8" )

contenido = archivo.read()

archivo.close()


lineas = contenido.splitlines()

datos_celda = list( csv.reader(lineas) )

# print(type(datos_celda))

for i in range(5):
    datos_celda.pop(i)

contador_color = 0
contador_bn = 0

for fila in datos_celda:
    if fila[0] == "Color":
        contador_color += 1
    elif fila[0] == " Black and White":
        contador_bn += 1

        

print("pelis de color hay" , contador_color)
print("pelis de bn hay" , contador_bn)

