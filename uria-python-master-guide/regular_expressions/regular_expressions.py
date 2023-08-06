import re


filename = "text.txt"
with open(filename) as file:
    text = file.read()


match = re.search("\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4} ", text)
print(match)
