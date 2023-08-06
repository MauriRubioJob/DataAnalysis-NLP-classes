
a = "string"
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("Dividing by b + 1 instead")
    print(a / (b + 1))
except TypeError:
    print("Don't be silly, that doesn't work")

print("Program finished.")