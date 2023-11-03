import requests

def callapi():
    url = "http://localhost:8000/api/products-by-category?category=7&page=1"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

for i in range(0,100):
    callapi()

