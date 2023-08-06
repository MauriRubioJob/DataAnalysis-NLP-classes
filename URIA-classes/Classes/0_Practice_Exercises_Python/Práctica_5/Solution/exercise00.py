# Write a Python program that takes a string and encode it that the amount of symbols would be represented by integer and the symbol. Go to the editor
# For example, the string "AAAABBBCCDAAA" would be encoded as "4A3B2C1D3A"
# Sample Output:
# 4A3B2C1D3A
# 1P1H1P
# 4A3B3C1D2A1B1D4A1C

oracion = "AAAAABBBBCCCCGGGGJJJJJSSSS"

lista_or = list(oracion)

result = []

for car in lista_or:
	if car not in result:
		result.append(str(lista_or.count(car)))
		result.append(car)

result = "".join(result)
print(result)



