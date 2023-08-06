# Create a Python program to remove all punctuation from a sentence.

sentence = "'Then the Dormouse shall!' they both cried. 'Wake up, Dormouse!' And they pinched it on both sides at once."


punctuation = ",.:;-!?'"

# Deberéis usar el método REPLACE. Podéis comprobar en w3school cómo funciona.

for symbol in punctuation:
	# Opcional para ver qué valores toma symbol al recorrer una string:  
	# print(symbol)
	sentence = sentence.replace(symbol, "")

print(sentence)