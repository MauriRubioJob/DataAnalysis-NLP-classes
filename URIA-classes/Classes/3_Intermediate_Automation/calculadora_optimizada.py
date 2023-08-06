# Hacer una calculadora

'''
1º) Presentación del proyecto
2º) Recepción de información -> 2 números y 1 operador
3º) Distinguir qué operación debemos hacer.

'''

# Vamos a crear las funciones necesarias para nuestor proyecto

# Función 1: Presentar proyecto.
def presentacion_proyecto():
    print ( "Esto es una calculadora.")
    print("Introduce la información necesaria para el proyecto")



# Función 2.1: Solicitar primer número:
def solicitar_datos():	

    n1 = input("Introduce el primer número: ")

    while True:

        if (n1.replace(".","").isdigit()):
            break
        else:
            print("Introduce un número")
            n1 = input("Introduce el primer número: ")



    n2 = input("Introduce el segundo número: ")

    while True:
        if (n2.replace(".","").isdigit()):
            break
        else:
            print("Introduce un número")
            n2 = input("Introduce el segundo número: ")

    operadores = ["+","-","/","*"]
    op = input("introduce el operador: ")
    while True:
        if (op in operadores):
            break
        else:
            print("Introduce un operador válido de entre: ", operadores)
            op = input("Introduce el operador: ")

    # Vamos a hacer que la función nos entregue las información que hay en n1:
    return n1 , n2 , op


# Funcion 3: distinguir la operación a realizar.
def calculo_realizar( numero1 , numero2 , operacion ):
    # Depende de operación, hago una cosa u otra.

    # Si el operador que hay en la variable operacion es un  + -> sumamos
    if ( operacion == "+"):
        resultado = numero1 + numero2

    # Si el operador que hay en la variable operacion es un  - -> restamos
    elif ( operacion == "-"):
        resultado = numero1 - numero2

    # Si el operador que hay en la variable operación es un  * -> multiplicamos
    elif ( operacion == "*"):
        resultado = numero1 * numero2

    # Si el operador que hay en la variable operación es un  / -> dividimos
    elif ( operacion == "/"):
        resultado = numero1 / numero2

    # Nos falta expresar la condición de cualquier otro carácter.
    else:
        resultado = "INVALIDO"

    return resultado


def Calculadora():
# A partir de aquí vamos a programar el proyecto utilizando las funciones
    presentacion_proyecto()

    while ( True ) :

        num1 , num2 , operador  = solicitar_datos()

        res = calculo_realizar (  float(num1) , float(num2) , operador )

        # Por último, saco por pantalla el resultado de la operación
        print ("El resultado de mi operación " , num1 , operador , num2 ,  " es: " , res) 

        break



Calculadora()
