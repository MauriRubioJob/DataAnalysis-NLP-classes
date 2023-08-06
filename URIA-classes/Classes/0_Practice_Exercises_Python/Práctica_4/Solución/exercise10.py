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
    8) Agregar una lista [] vacía de telefonos al diccionario marido que fue agregado al usuario en el paso anterior
    9) Crear una funcion que agregue telefonos a una lista
    10) Usando la funcion anterior agregar el siguiente telefono 603345890
"""

import json
# from pprint import pprint



# 1) Crear una funcion que retorne el nombre del usuario, edad y teléfono
def consulta( diccionario ):
	return diccionario["nombre"],diccionario["edad"],diccionario["telefono"][0]

# 2) Crear una funcion que retorne los años que trabajo en sus trabajos anteriores y en qué empresa trabajó dichos años
def trabajo_previo( diccionario ):
	trabajo_anterior = []
	for trabajo in diccionario["trabajos"]:
		trabajo_anterior.append("En "+trabajo["empresa"]+" trabajó "+str(trabajo["años"])+" años")
	return trabajo_anterior

# 3) Crear una funcion que retorne la suma de los años que trabajo en sus trabajos anterior + el actual
def años_trabajados(diccionario):
	años_actuales = diccionario["empresa_actual"]["años"]
	años_previos = diccionario["trabajos"][0]["años"]+diccionario["trabajos"][1]["años"]
	return años_actuales + años_previos

# 4) Crear una funcion que returne la suma lo que ha ganado (Ejemplo años en la empresa 1 * sueldo) esta operacion
# se  tiene que repetir por cada trabajo incluyendo el actual para obtener un total y retornarlo
def ingreso_total (dic):
	ingreso_actual = dic["empresa_actual"]["años"]*dic["empresa_actual"]["sueldo"]
	ingresos_previos = 0
	for i in range(2):
		ingresos_previos += dic["trabajos"][0]["años"]*dic["trabajos"][0]["sueldo"]

	sueldo_total = ingreso_actual + ingresos_previos

	return sueldo_total

# 5) Crear una funcion que agrege hijos
def agregar_hijo( dic , hijo ):
	dic["hijos"].append(hijo)

# 6) Agregar los siguientes hijos (Juan 13 años, Maria 16, Julieta 2)
def agregar_hijos ( diccionario ):
	hijo1 = {"nombre":"Juan","años":13}
	agregar_hijo( diccionario , hijo1 )

	hijo2 = {"nombre":"Julieta","años":2}
	agregar_hijo( diccionario , hijo2 )

	hijo3 = {"nombre":"Maria","años":16}
	agregar_hijo( diccionario , hijo3 )

# 7) Agregar un nuevo elemento al diccionario usuario que sea marido y tengo un diccionario con 
# {'nombre': 'Luis', 'edad':26}
def agregar_marido( dic ):
	dic["marido"] = {"nombre":"Luis" , "edad":26}

# 8) Agregar una lista [] vacía de telefonos al diccionario esposa que fue agregado al usuario en el paso anterior
def agregar_telefono_marido( dic ):
	dic["marido"]["telefonos"] = []


# 9) Crear una funcion que agregue telefonos a una lista
def agregar_telefono( dic , telefono ):
	dic["marido"]["telefonos"].append(telefono)

# 10) Usando la funcion anterior agregar el siguiente telefono 603345890
def agregar_telefonos ( diccionario ):
	agregar_telefono( diccionario , "603345890")


# PROGRAMA PRINCIPAL:


usuario ='{"nombre": "Juan", "edad": 25, "dni": "93178422Y", "telefono": [663558874, 663418004], "hijos": [], "empresa_actual": {"nombre": "ING", "años": 1, "sueldo": 2500}, "trabajos": [{"empresa": "HP", "años": 2, "sueldo": 1500}, {"empresa": "Google", "años": 10, "sueldo": 2000}]}'

usuario = json.loads(usuario)


print("Consulta del diccionario: ")
print(consulta(usuario))
print("\n")

print("trabajo previo: ")
print(trabajo_previo(usuario))
print("\n")

print("años_trabajados: ")
print(años_trabajados(usuario))
print("\n")

print("ingreso total: ")
print(ingreso_total(usuario))
print("\n")

print("hijos agregados ")
(agregar_hijos(usuario))
print("\n")

print("marido agregado ")
(agregar_marido(usuario))
print("\n")

agregar_telefono_marido(usuario)

print("teléfono agregado ")
(agregar_telefonos(usuario))
print("\n")