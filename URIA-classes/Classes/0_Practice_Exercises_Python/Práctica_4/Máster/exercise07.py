# https://python.techtalents.cloud/python/exercises/7 returns a dictionary of ages. This program prints the oldest and youngest person after reading and proccessing the inforrmation of that external file.
# fix the errors of this exercises.

import random
import json

url = "https://python.techtalents.cloud/exercises/7
response = requests.get(url)
if response.stutas_code == 200:
    dictionary = response.text
else:
  exit()

conversion = json.loads(dictionario_edades)

mayor = 0
menor = 100

for x in conversion:

	if conversion[x]>mayor:
		mayor = conversion[]
		oldest = x
	if conversion[x]<menor
		menor = conversion[x]
		youngest = x
	

print(oldest+"es la persona más mayor. Tiene"+conversion[oldest]+"años")

print(youngest+"es la persona más joven. Tiene"+conversion[youngest]+"años")