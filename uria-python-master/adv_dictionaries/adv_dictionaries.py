
hair_colours = {
    "Arthur": "ginger",
    "Bill": "ginger",
    "Charlie": "ginger",
    "Draco": "blond",
    "Errol": "feathers",
    "Fred": "ginger",
    "George": "ginger",
    "Harry": "black"
}

# Accessing items that may not exist
print(hair_colours.get("Lucius", "Hair colour not found."))

# keys, values, items
print(hair_colours.keys())
print(hair_colours.values())
print(hair_colours.items())

for name, colour in hair_colours.items():
    print(name + " has " + colour + " hair.")




from collections import defaultdict

letters = "TXkOcdCuAaBayuYYPvroKvmYcDCnbYYzugdElReslpflGYEdgAqCWuDsBMQpdjSBUVoVFFJdkJbOrUlKYcROxyDzkDTmmbHYdVXxDcifsoUcoKrgtuwMjXAjIABbOHcL"

times_appeared = defaultdict(int)

for letter in letters:
    times_appeared[letter] = times_appeared[letter] + 1

print(times_appeared)
