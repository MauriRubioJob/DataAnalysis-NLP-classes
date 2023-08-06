
people = [
    { "name": "Arthur", "number": "4716 6950 9279 5206", "ccv": "518" },
    { "name": "Bill", "number": "4716 3002 1499 2654", "ccv": "911" },
    { "name": "Charlie", "number": "4929 6067 1966 9933", "ccv": "691" },
    { "name": "Draco", "number": "4916 8472 9465 0063", "ccv": "754" },
    { "name": "Errol", "number": "4539 6055 5986 0844", "ccv": "259" },
    { "name": "Fred", "number": "4335 6009 6417 7955", "ccv": "724" },
    { "name": "George", "number": "4539 7648 3591 6431", "ccv": "594" },
    { "name": "Harry", "number": "4556 5311 0778 9962", "ccv": "572" }
]

def print_data(person, string=None):
    print(string, person["name"], string, person["number"], string, person["ccv"], string)


def find_person(people, name):
    found_person = None
    for person in people:
        if person["name"] == name:
            found_person = person
    if found_person:
        return found_person



found = find_person(people, "Harry")
if found:
    print_data(found)


