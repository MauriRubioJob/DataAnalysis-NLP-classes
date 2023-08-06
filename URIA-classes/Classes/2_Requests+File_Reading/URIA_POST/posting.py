import requests
import json

# Declaration of location and data
url = "https://httpbin.org/post"
data = {
    "name": "nico",
    "age": 99,
    "colour": "cyan"
}

# Make the connection
response = requests.post(url, data)

# Check the connection
if response.status_code == 200:
    converted = json.loads(response.text)
    import pprint
    pprint.pprint(converted)
else:
    print("Something went terribly wrong.")
