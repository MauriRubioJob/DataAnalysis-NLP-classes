import requests
import json

url = "https://python.techtalents.cloud/chat"
sending_url = "https://python.techtalents.cloud/chat/send"


def download():
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Download failed.")


def upload():
    data 
    response = requests.post(sending_url)
    if response.status_code == 200:
        return response.text
    else:
        print("Download failed.")


def display_messages():
    downloaded = download()
    converted = json.loads(downloaded)
    for x in converted:
        print(x["author"], x["message"])


# print(upload())
# print(download())
display_messages()
