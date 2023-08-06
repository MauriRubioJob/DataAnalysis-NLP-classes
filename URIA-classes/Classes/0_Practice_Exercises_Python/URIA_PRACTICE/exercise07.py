# Create a Python program that tells the user if any word in a string
# starts with a chosen letter.

# First create a list of words, and then check one by one if each word
# "startswith()" the given letter. If any single word matches, print
# "It exists" and stop searching. Otherwise if no words match, print
# "It does not exist"


oracion = "Cuando no hay un campo magnético externo, estos imanes atómicos tienen una orientación aleatoria, de modo que sus efectos se contrarrestan."

words = oracion.split()
looking_for = input()

found = False
for word in words:
    if word.startswith(looking_for):
        found = True
        break

if found:
    print("It exists")
else:
    print("It does not exist")
        
