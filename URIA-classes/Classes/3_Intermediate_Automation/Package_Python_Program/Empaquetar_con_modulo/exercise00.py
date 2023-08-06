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


print("Programa terminar")
input("Press enter to exit: ")