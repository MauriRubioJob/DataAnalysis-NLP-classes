#  Write a Python program that accepts an integer (n) as input and computes the value of n+nn+nnn
#  Example: 
#    Value of n is 5
#    5 + 55 + 555 = 615

n = input()
result = int(n) + int(n+n) + int(n+n+n)

print(result)

