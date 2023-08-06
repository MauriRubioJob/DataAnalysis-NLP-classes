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
nombre1 = "Juan"
nombre2 = "Elena"
nombre3 = "Pepe"

edad1 = 19
edad2 = 24
edad3 = 43

deuda1 = 320
deuda2 = 600
deuda3 = 1500

descuento1 = 0.15
descuento2 = 0.30
descuento3 = 0.08

# PROGRAMA PRINCIPAL: Imprimir la información de los usuarios TRAS recalcular la deuda además de imprimir los promedios.
deuda1 = recalculo(edad1,deuda1)
deuda2 = recalculo(edad2,deuda2)
deuda3 = recalculo(edad3,deuda3)

impresion(nombre1,edad1,deuda1)
impresion(nombre2,edad2,deuda2)
impresion(nombre3,edad3,deuda3)

print((edad1+edad2+edad3)/3)
print((deuda1+deuda2+deuda3)/3)