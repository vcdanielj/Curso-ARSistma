import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    print(datos)
else:
    print("Error en la solicitud")