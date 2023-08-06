# Write a Python program that tells you, in a given string, how many words
# appear more than once.

# Example:
#   "The Python programming language, named after British comedy group
#    Monty Python, is a general-purpose language that supports multiple 
#    paradigms. The reference implementation is built using the C
#    programming language."

#   Words: the, python, programming, language, is -> 5


# To simplify things in this case, use a pre-formatted sentence with all
# punctuation removed and uppercase letters converted.


sentence = "the python programming language named after british comedy group monty python is a general purpose language that supports multiple paradigms the reference implementation is built using the c programming language"
words = sentence.split()


duplicates = []
for word in words:
    if words.count(word) > 1 and not word in duplicates:
        duplicates.append(word)

print(len(duplicates))
