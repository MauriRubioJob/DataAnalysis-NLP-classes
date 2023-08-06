import requests


url = "https://python.techtalents.cloud/people.csv"
response = requests.get(url)
if response.status_code == 200:
    rows = response.text.splitlines()
    # For each row in the table:
    processed = []
    for row in rows:
        processed.append(row.split(","))
else:
    print("Error when downloading.")


# Find the person with the greatest net_worth, who has
# green eyes, and a last name at least 6 letters long.

processed.pop(0)
greatest = 0     # Assume the greatest net_worth is 0
result = None
for row in processed:
    first = row[0]
    last = row[1]
    age = row[2]
    net_worth = int(row[3])
    eye_colour = row[4]
    
    if eye_colour == "green":
        if len(last) >= 6:
            if net_worth > greatest:
                greatest = net_worth
                # Don't return or print, but save the result
                result = first, last, net_worth

# Print the result once everything has finished
print(result)
