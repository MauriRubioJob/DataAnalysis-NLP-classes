# You have requested something over the internet and you have been given a text in the response... However it seems that python is having some problems working with that.
# find a way to proccess the string given thus making python able to consult the key "name" of the 3 element of the list.
# print the result

import json

respuesta_text = '[{"name": "Mauri", "age": 34, "work": "Teacher"}, {"name": "David", "age": 48, "work": "Engineer"}, {"name": "Mara", "age": 29, "work": "Teacher"}, {"name": "Belen", "age": 27, "work": "Lawyer"}, {"name": "Cristina", "age": 56, "work": "IoT"}]'

conversion = json.loads(respuesta_text)
print(conversion[2]["name"])
