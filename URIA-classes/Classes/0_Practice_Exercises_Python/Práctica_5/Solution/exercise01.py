# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

oracion = "green-red-yellow-black-white"

result = oracion.split("-")
result.sort()
result = "-".join(result)
print(result)