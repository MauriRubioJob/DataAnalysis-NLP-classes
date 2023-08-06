# # # # # # ENGLISH:

# Knowing that 1 pound = 1.15 euro.
# Define a function tthat changes from euro -> pound
# And a function that changes from pound -> euros

# After that, in your main program, you shall ask the user to type "P" to convert (€ -> £) or "E" to convert otherwise. After making the conversion, the result of it must be printed out.

# # # # # # ESPAÑOL:

# Sabiendo que 1 libra = 1,15 euros.
# Definir una función que cambie de euro -> libra
# Y una función que cambie de libra -> euros

# Después de eso, en el programa principal, le pedirá al usuario que teclee "P" para convertir (EUR -> £) o "E" para hacer la conversión contraria. Después de hacer la conversión, el resultado de la misma debe ser impreso en pantalla. 

# Definir las funciones de conversión

# FUNCIÓN 1: Conversión € -> £
def toPounds():
	euros = input()
	print(round(float(euros)/1.15))

# FUNCIÓN 2: Conversión £ -> €
def toEuros():
	pounds = input()
	print(round(float(pounds)*1.15))

# PROGRAMA PRINCIPAL:

# 1) solicitar elección del usuario. "P" ó "E"
eleccion = input()
# 2) En función de esa elección, ejecutar una conversión u otra.
if(eleccion == "P"):
	toPounds()
elif(eleccion == "E"):
	toEuros()
else:
	print("error")