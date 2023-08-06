
mi_variable = True   # False


'''
Una variable booleana:

    - Se suele utilizar para preguntar con if o para controlar un bucle while.


'''

enchufada = True
bombilla_rota = False


# # Partimos de que la lámpara no funciona

# if ( enchufada == False ):
#     print("Pues enchufa la lámpara")

# if ( enchufada == True):
#     if (bombilla_rota == True):
#         print("Pues compra otra bombilla")
    
#     if( bombilla_rota == False ):
#         print("Pues compra otra lámpara")


dia = True

# if (dia == True):
#     # Apagar todas las luces de la ciudad

# if (dia == False):
#     # Encender todas las luces de la ciudad

hora = 18
while ( dia ):
    
    print("Son las", hora, ". Es de día")

    if ( hora == 22 ):
        dia = False
    
    hora += 1


print( "Es de noche" )

