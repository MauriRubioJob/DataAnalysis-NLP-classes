# fix the errors in the following program.


def Calculadora():

	# Pedir datos por teclado

	numero1 = int(input())
	numero2 = int(input())
	operacion = input()

	# Evaluación de la operación solicitada

	if operacion == '+':
		Resultado = numero1 + numero2
		print(Resultado)
	elif operacion == '-':
		Resultado = numero1 - numero2
		print(Resultado)
	elif operacion == '*':
		Resultado = numero1 * numero2
		print(Resultado)
	elif operacion == '/':
		Resultado = numero1 / numero2
		print(Resultado)
	else:
		print("Error")

Calculadora()