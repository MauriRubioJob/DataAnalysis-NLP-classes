# Read the external file named "sentences.txt" and load all of its content
# into a variable. Remember to close the file.
# All of the content must be split first into lines, and then into words,
# so we can comfortably work with it.

# After that, ask the user for a word as a console input.
# If the given word exists in the file, printed out: "It exists", otherwise
# print "It does not exist"

# TIP: If you follow the same name rules and code structure, you can
#      use a lot of the code from exercise 7


file = open("sentences.txt", "r")
contents = file.read()
file.close()

sentences = contents.splitlines()
looking_for = input()


words = []
for sentence in sentences:
    words.extend(sentence.split())

found = False
for word in words:
    if word.startswith(looking_for):
        found = True
        break

if found:
    print("It exists")
else:
    print("It does not exist")
