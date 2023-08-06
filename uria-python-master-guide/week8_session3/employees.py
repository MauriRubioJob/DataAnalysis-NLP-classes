import requests
import json

def get_all_info(company_name):
    url = "https://librebor.me/borme/api/v1/empresa/xxx-xxx-xxx/".replace("xxx-xxx-xxx", company_name)
    response = requests.get(url)
    if response.status_code == 200:
        converted = json.loads(response.text)
        return converted


def search_company(name):
    url = "https://libreborme.net/borme/api/v1/empresa/search/?q=xxx&page=1".replace("xxx", name)
    response = requests.get(url)
    if response.status_code == 200:
        converted = json.loads(response.text)
        return converted


print("Enter name to search for:")
name = input()
companies = search_company(name)
objects = companies["objects"]

if len(objects) == 0:
    print("No results found.")
else:
    company = objects[0]

    company_name = company["slug"]
    company_info = get_all_info(company_name)
    
    employees = company_info["cargos_actuales_p"]
    print("Number of employees is", len(employees))
