# In the empty dictionary given, add the following data: 
#   name -> Chris
#   age -> 34
#   work -> Lawyer
# Then you must send the dictionary over the internet to the following page:
# https://python.techtalents.cloud/exercises/0
# And afterwards print the response

import requests

nombre = input("Introduce el nombre (Chris): ")
data = {
	"name": nombre,
    "age": 34,
    "work": "Lawyer"
}

url = "https://python.techtalents.cloud/exercises/0"
r = requests.post(url, data)

if r.status_code == 200:
    print(r.text)
else:
    print("Unsuccessful.")
