# Convert a normal sentence, that uses spaces to separate words, to a string
# that separates words using the character given by the user.

# Example:
#   Chosen character ">"
#   "Hello my name is" = "Hello>my>name>is"


oracion = "Cualquier duda que un alumno tenga debe preguntarla"

character = input()

words = oracion.split()

result = character.join(words)
print(result)
