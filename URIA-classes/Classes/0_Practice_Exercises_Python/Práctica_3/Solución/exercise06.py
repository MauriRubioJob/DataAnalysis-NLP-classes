# Create a Python program to reverse a string.

# Example:
#   "What have the Romans ever done for us?" ->
#          "?su rof enod reve snamoR eht evah tahW"

sentence = "What have the Romans ever done for us?"

# Método 1
as_list = list(sentence)
# as_list = sentence.split()
backwards = []
for i in range(len(as_list) - 1, -1, -1):
    backwards.append(as_list[i])

result = "".join(backwards)


# Método 2
# as_list = list(sentence)
# as_list.reverse()
# result = "".join(as_list)

# Método 3
# backwards = reversed(sentence)
# result = "".join(backwards)


print(result)
