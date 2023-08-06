'''
Este script lo vamos a dedicar a ver una forma más eficiente de utilizar print y crear strings.

'''

nombre = "Mauri"
Apellido = "Rubio"
Edad = 25

print( "Hola me llamo" , nombre , Apellido , "tengo", Edad , "años" )
print( "Hola me llamo " + nombre + " " +  Apellido + " tengo "+ str(Edad) + " años" )

print( f"Hola me llamo {nombre} {Apellido} tengo {Edad} años" )
print( "Hola me llamo {} {} tengo {} años".format(nombre,Apellido,Edad) )



