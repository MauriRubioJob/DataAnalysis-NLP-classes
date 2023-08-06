'''
1) Una función/instrucción es una fomra que tenemos de darle una orden al ordenador para obtener un resultado concreto

2) Podemos crear nuestras propias funciones.
    - Se crean utilizando la palabra "def"
    - Le tenemos que dar un nombre a esa función. El nombre no puede tener espacio entre palabra
    - El nombre que le dé no puede ser igual a un nombre de una función que python ya tenga definida
    - Mi función va a ejecutar todas las instrucciones (todo el código) que esté indentando 
        tras los 2 puntos después de definir el nombre de la función. 
    - Una función por si misma no hace NADA hasta que yo en el programa principal no la ejecute.

'''

# SECCIÓN DE FUNCIONES: 

# Función 1: en 2 variable guardado 2 números que luego suma, e imprime el resultado.
def suma_2_numeros ():
    num1 = 4
    num2 = 6
    resultado = num1 + num2
    print(resultado)


# SECCIÓN DEL PROGRAMA PRINCIPAL
print("Practicando con funciones.")
print("\n")
print("Aprendiendo a utilizar una función básica:")

suma_2_numeros()


