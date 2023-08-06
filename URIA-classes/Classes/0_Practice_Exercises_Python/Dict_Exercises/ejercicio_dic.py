"""
En este ejercicio os es entregada una variable recibida a través de internet que describe el currículum de un usuario. Deberéis realizar las solicitudes que se os muestran a continuación, aunque antes deberéis transoformar la string recibida en un conjunto de datos manejables en python...

    1) Crear una funcion que retorne el nombre del usuario, edad y teléfono
    2) Crear una funcion que retorne los años que trabajo en sus trabajos anteriores y en qué empresa trabajó dichos años
    3) Crear una funcion que retorne la suma de los años que trabajo en sus trabajos anterior + el actual
    4) Crear una funcion que returne la suma lo que ha ganado (Ejemplo años en la empresa 1 * sueldo) esta operacion
    se  tiene que repetir por cada trabajo incluyendo el actual para obtener un total y retornarlo
    5) Crear una funcion que agrege hijos
    6) Agregar los siguientes hijos (Juan 13 años, Maria 16, Julieta 2)
    7) Agregar un nuevo elemento al diccionario usuario que sea esposa y tengo un diccionario con 
    {'nombre': 'Petra', 'edad':26}
    8) Agregar una lista [] basia de telefonos al diccionario esposa que fue agregado al usuario en el paso anterior
    9) Crear una funcion que agregue telefonos a una lista
    10) Usando la funcion anterior agregar el siguiente telefono 603345890
"""

# Sección de importación de módulos:

import json
import pprint

# Sección de FUNCIONES:

# 1) Crear una funcion que retorne el nombre del usuario, edad y teléfono
def consulta_nombre_edad_tel ( informacion ):
    nombre = informacion["nombre"]
    edad = informacion["edad"]
    telefono = informacion["telefono"]
    return nombre, edad, telefono

# 2) Crear una funcion que retorne los años que trabajo en sus trabajos anteriores y en qué empresa trabajó dichos años
def consulta_trabajos_anteriores ( informacion ):
    años_anteriores = []
    empresas_anteriores = []
    for trabajo in informacion:
        empresas_anteriores.append(trabajo["empresa"])
        años_anteriores.append(trabajo["años"])

    return empresas_anteriores , años_anteriores



# 3) Crear una funcion que retorne la suma de los años que trabajo en sus trabajos anterior + el actual
def suma_años ( trabajo_actual , años_anteriores ):
    años_actuales = trabajo_actual["años"]
    
    años_totales = años_actuales

    for año in años_anteriores:
        años_totales += año

    return años_totales

# 4) Crear una funcion que returne la suma lo que ha ganado (Ejemplo años en la empresa 1 * 12 * sueldo) esta operacion
# se  tiene que repetir por cada trabajo incluyendo el actual para obtener un total y retornarlo

def dinero_ganado( trabajo_actual , trabajos_anteriores ):
    dinero_actual = trabajo_actual["años"] * trabajo_actual["sueldo"] * 12

    dinero_anteriores = 0
    for trabajo in trabajos_anteriores:
        dinero_anteriores += trabajo["años"] * trabajo["sueldo"] * 12

    dinero_total = dinero_actual + dinero_anteriores

    return dinero_total 



# 5) Crear una funcion que agrege la hijos
# 6) Agregar los siguientes hijos (Juan 13 años, Maria 16, Julieta 2)

'''
usuario{
    ...
    "hijos" : [ {   "nombre" : "Juan" , 
                    "edad" : 13 } ,
                    "nombre" : "Maria" , 
                    "edad" : 9 } ,
    
    
                 ...]
}

'''
def agregar_hijos (informacion , nombres , edades ):
    informacion["hijos"] = []
    
    dic = {}
    for i in range ( len (nombres)):
        dic["nombre"] = nombres[i]
        dic["edad"] = edades[i]

        informacion["hijos"].append(dic)
        dic = {}
    
    return informacion



# 7) Agregar un nuevo elemento al diccionario usuario que sea esposa y tenga un diccionario con 
# {'nombre': 'Petra', 'edad':26}
def agregar_pareja ():
    usuario ["pareja"] = {'nombre': 'Petra', 'edad':26}


# 8) Agregar una lista [] vacia de telefonos al diccionario pareja que fue agregado al usuario en el paso anterior
def agregar_lista_telefonos ():
    usuario["pareja"]["telefonos"] = []

# 9) Crear una funcion que agregue telefonos a una lista
# 10) Usando la funcion anterior agregar el siguiente telefono 603345890
def agregar_telf ( telefono ):
    usuario["pareja"]["telefonos"].append(telefono)

# Secciónd e mi Programa Principal:
usuario ='{"nombre": "Juan", "edad": 25, "dni": "93178422Y", "telefono": [663558874, 663418004], "empresa_actual": {"nombre": "ING", "años": 1, "sueldo": 2500}, "trabajos": [{"empresa": "HP", "años": 2, "sueldo": 1500}, {"empresa": "Google", "años": 10, "sueldo": 2000}]}'
# Tenemos que pasar de string json -> variable de python (diccionario)
usuario = json.loads(usuario)
print(type(usuario))
pprint.pprint(usuario)

nombre, edad, telefonos = consulta_nombre_edad_tel( usuario )
print( f"Nombre: {nombre}\nEdad: {edad}\nTelefonos: {telefonos[0]} y {telefonos[1]}" )

empresas_anteriores , años_anteriores = consulta_trabajos_anteriores ( usuario["trabajos"] )

for i in range(2):
    print(f"En la empresa {empresas_anteriores[i]} trabajó {años_anteriores[i]} años.")


total_años_trabajados = suma_años ( usuario["empresa_actual"] , años_anteriores )
print(f"Esta persona ha trabajado en su vida {total_años_trabajados} años.")


dinero_total = dinero_ganado( usuario["empresa_actual"] , usuario["trabajos"] )
print(f"Esta persona en toda su vida ha ganado {dinero_total} euros.")

nombre_hijos = [ "Juan" , "Pepito" , "Maria" , "menganito"]
edad_hijos = [16 , 13 , 9 , 0]

usuario = agregar_hijos(usuario , nombre_hijos , edad_hijos )
pprint.pprint(usuario)

agregar_pareja()
pprint.pprint(usuario)

agregar_lista_telefonos()
pprint.pprint(usuario)

agregar_telf(603345890)
agregar_telf(603344363243545890)
pprint.pprint(usuario)