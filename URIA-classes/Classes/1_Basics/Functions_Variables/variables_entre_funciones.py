# Cuando utilizamos la orden print entre paréntesis yo le tengo que dar
# cierta información. Esa información que doy entre paréntesis, se llama ARGUMENTO DE LA FUNCION
# texto = "Hello"
# print(texto)


# Vamos a trabajar creando nuestra propias funciones, las cuales tienen argumentos

def suma_2_numeros ( num1 , num2 ):
    resultado = num1 + num2
    return resultado
    
def resta_2_numeros ( num1 , num2 ):
    resultado = num1-num2
    return resultado


# La función "suma_2_numeros" necesita como argumento 2 elementos de información.

# Sección Programa principal.

num1 = 70
num2 = 94

resultado = suma_2_numeros ( num1 , num2 )
print(resultado)

resultado = resta_2_numeros ( num1 , num2 )
print(resultado)




