
person = {}
    "name": "Bob",
    "age": 42,
    "job": "Builder"
}

location = {
    "city": "Madrid",
    "country": "Spain",
    "language": "Spanish"
}

person["colour"] = "blue"

print(person)

for i in person:
    print(i)
    print(person[i])


person = ["Bob", 42, "Builder", "blue"]
for i in person:
    print(i)

