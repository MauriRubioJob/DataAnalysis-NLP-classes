'''
En python sabemos que una variable es una palabra en la cual guardo una cierta información.

Para crear una variable pongo el nombre de la palabra (no puede ser una palabra que python ya recoja en su lenguaje)

NOMBRE_PALABRA = INFORMACION

Esta información hemos visto que existe en python en distintas formas:
'''


print("Tipo de información de 1 solo dato")

print("Esto es un número entero o int: ", 5)
print("Esto es un número decimal o float: ", 5.864)
print("Esto es un carácter: ", "h")
print("Esto es un booleano: ", True )

print("\n")

print("Tipo de información de varios datos")

# En la cadena de carácteres cada carácter es 1 elemento.
print("Esto es una cadena de caracteres: " , 'Hola me llamo Mauri')

# En la lista tengo varios elementos separados por comas. Los elementos de una lista pueden ser de cualquier
# tipo de información. Cada elemento tiene un número de posición.
print("Esto es una LISTA: ", [ 53 , 1.2 , False , "h" , "Mauri" , [1,2] ])

# En un diccionario siempre tengo una pareja (key : value). La información se guarda asociada una key/propiedad
# La información que puedo guardar en un diccionario es de cualquier tipo.
print("Esto es un diccionario: ", { "nombre" : "Mauri" , "edad" : 25 , "oficio": ["administrativo","profesor"] , "estado laboral": True })


'''
Lo más importante de los tipos de informaicón / variables que guardan varops datos es que con 1 sola variable, puedo
guardar mucha información

Este tipo de variable son recorrible con un BUCLE FOR.

'''

alumnos = ["Miguel" , "carmen" , "satur" , "alejandro"]

# for VAR_INTERMEDIARIA in VARIABLE_A_RECORRER:

# Si recorro una lista, la variable intermediaria es cada elemento de la lista:
for alumno in alumnos:
    print(alumno)
    # input("pulsa enter para continuar al siguiente alumno")

# Si recorro una cadena de caracteres, la variable intermediaria va a tomar el valor de cada caracter de mi cadena
oracion = "Hola mundo"

for caracter in oracion:
    print(caracter)
    # input("pulsa enter para continuar al siguiente caracter")

# Si recorro un diccionario, la variable intermediaria va a tomar el valor de cada key de mi diccionario

persona = {
    "nombre" : "Mauri",
    "edad" : 25, 
    "oficio" : "profesor"
}

for propiedad in persona:
    print(propiedad)
    print(persona [propiedad] )
    # input("pulsa enter para ver la siguiente key")


print("\n\n")
# Posiciones: 0 , 1  , 2  , 3  , 4
ganancias = [ 52 , 13 , 78 , 14 , 52 ]
pocentaje = [ 0.8 , 0.2 , 0.5 , 0.4 , 0.6 ]
# 
# print(ganacias[])

for ganancia in ganancias:
    print(ganancia)


for i in range( 5 ):
    print(ganancias[i])
    print(pocentaje[i])