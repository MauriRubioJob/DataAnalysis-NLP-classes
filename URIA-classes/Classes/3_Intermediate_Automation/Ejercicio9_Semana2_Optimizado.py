#  Esta tarea tendrá múltiples partes.
 
#  En primer lugar, escribir una función que imprima la siguiente información:
#  "NOMBRE_DE_CLIENTE tiene una edad de EDAD_CLIENTE y su deuda actual es: DEUDA_CLIENTE"
 
#  Esta función debe recibir los datos del usuario como entrada (nombre, edad, deuda)
 
 
# En segundo lugar, crear una función que pueda aplicar descuentos a las personas en función de su edad y situación financiera.
#  Aplicar el descuento_1 si el cliente es mayor de 20 años y su deuda es menor de 800
#  Aplicar el descuento_2 si el cliente tiene menos de 20 años y una deuda inferior a 500
#  Aplica un descuento del 8% para el resto de los clientes.
# descuento1 = 0.15 (15%)
# descuento2 = 0.30 (30%)

 
#  Por último, utilizando las dos funciones creadas anteriormente, imprima toda la información de
#  las tres personas:
#  Juan, 19, 320
#  Elena, 24, 600
#  Pepe, 43, 1500
 
#  Y luego calcula la edad promedio y la deuda promedio:
#  Edad promedio: XXX
#  Deuda promedio: YYY


nombres = [ "Juan" , "Elena" , "Pepe" ] 
edades = [ 19 , 24 , 43 ]
deudas = [ 320 , 600 , 1500 ] 

descuento1 = 0.15
descuento2 = 0.30
descuento3 = 0.08

# Creación de funciones:

# Función 1: función que imprima la información de los usuarios.
def impresion(nombre,edad,deuda):
	print(nombre+" tiene una edad de "+str(edad)+" y su deuda actual es: "+str(deuda))

# función 2: función que recalcule la deuda de los usuarios y la devuelva (return)
def recalculo(edad,deuda):
	if(edad > 20 and deuda < 800):
		return deuda*descuento1
	elif (edad < 20  and  deuda < 500):
		return deuda*descuento2
	else:
		return deuda*descuento3


# VARIABLES DEL PROGRAMA PRINCIPAL:

personas = [
    {
        "nombre":"Juan",
        "edad" : 19,
        "deuda" : 320
    },
    {
        "nombre":"Elena",
        "edad" : 24,
        "deuda" : 600
    },
    {
        "nombre":"Pepe",
        "edad" : 43,
        "deuda" : 1500
    }
]

nombres = [ "Juan" , "Elena" , "Pepe" ] 
edades = [ 19 , 24 , 43 ]
deudas = [ 320 , 600 , 1500 ] 

descuento1 = 0.15
descuento2 = 0.30
descuento3 = 0.08

# PROGRAMA PRINCIPAL: Imprimir la información de los usuarios TRAS recalcular la deuda además de imprimir los promedios.


suma_edad = 0
suma_deuda = 0
for persona in personas:
    persona["deuda"] = recalculo ( persona["edad"] , persona["deuda"])
    impresion(persona["nombre"],persona["edad"],persona["deuda"])

    suma_edad += persona["edad"]
    suma_deuda += persona["deuda"]

print("El promedio de edad es: ", suma_edad/len(personas))
print("El promedio de deuda es: ", suma_deuda/len(personas))