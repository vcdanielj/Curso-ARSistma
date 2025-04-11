from bs4 import BeautifulSoup
import requests

# Hacer una solicitud HTTP
url = "https://www.bancoexterior.com/tasas-bcv/"
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar elementos
etiquetas = soup.find_all("li")

""" for index, valor in enumerate(etiquetas):
    print(index, " -> ", valor) """

# print(etiquetas[90].text)
precio = 90
tasa= float(etiquetas[90].text[8:].replace(",", "."))
precio_bs = precio * tasa
print("El precio en bs es: ", precio_bs)

# print(etiquetas[90].text[8:])
# print(etiquetas[89].text[9:])

