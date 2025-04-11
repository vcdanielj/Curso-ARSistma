import requests

url = "https://pydolarve.org/api/v1/dollar?page=bcv"
response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    print(datos["monitors"]["usd"]["price"])
else:
    print("Error en la solicitud")