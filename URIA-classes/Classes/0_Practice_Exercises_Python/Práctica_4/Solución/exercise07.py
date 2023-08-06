# ages_dict.txt is an external files which contains a string with dictionary values of the ages of people. This program prints the oldest and youngest person after reading and proccessing the inforrmation of that external file.
# fix the errors of this exercises.

import random
import json
import requests

url = "https://python.techtalents.cloud/exercises/7"
response = requests.get(url)
if response.status_code == 200:
    diction = response.text
else:
  exit()


conversion = json.loads(diction)

mayor = 0
menor = 100

for x in conversion:
	if conversion[x]>mayor:
		mayor = conversion[x]
		oldest = x
	if conversion[x]<menor:
		menor = conversion[x]
		youngest = x
	

print(oldest,"es la persona más mayor. Tiene",conversion[oldest],"años")

print(youngest,"es la persona más joven. Tiene",conversion[youngest],"años")