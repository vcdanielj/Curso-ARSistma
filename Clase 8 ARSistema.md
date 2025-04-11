## Clase 8: Programación Orientada a Objetos, Web Scraping y Llamadas a APIs

### Introducción a la Programación Orientada a Objetos (POO)

La programación orientada a objetos es un paradigma de programación que se centra en la creación de objetos que tienen propiedades y métodos. Estos objetos pueden interactuar entre sí para lograr un comportamiento complejo.

#### Conceptos Básicos

- **Clases**: Son plantillas que definen las propiedades y comportamientos de un objeto.
- **Objetos**: Instancias de una clase, cada uno con sus propias características.
- **Herencia**: Permite que una clase herede propiedades y métodos de otra clase.
- **Polimorfismo**: La capacidad de un objeto para tomar muchas formas, dependiendo del contexto.
- **Encapsulación**: Ocultar la implementación interna de un objeto y solo exponer métodos públicos.

#### Ejemplo de Clase en Python

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear un objeto
persona = Persona("Juan", 30)
persona.saludar()
```

### Web Scraping con Beautiful Soup

Beautiful Soup es una biblioteca de Python utilizada para parsear y extraer datos de documentos HTML y XML.

#### Instalación

Para usar Beautiful Soup, necesitas instalarlo primero:

```bash
pip install beautifulsoup4
```

#### Ejemplo de Uso

```python
from bs4 import BeautifulSoup
import requests

# Hacer una solicitud HTTP
url = "https://www.example.com"
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar elementos
titulo = soup.find('title').text
print(titulo)
```
### Resumen de Métodos Comunes para Filtrar

| **Método**       | **Descripción**                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| `find(name)`      | Encuentra el primer elemento que coincide con el nombre de etiqueta dado.       |
| `find_all(name)`  | Encuentra todos los elementos que coinciden con el nombre de etiqueta dado.     |
| `select(css)`     | Encuentra elementos usando selectores CSS.                                      |
| `find(attrs={})`  | Encuentra elementos basándose en atributos específicos.                         |
### Llamadas a APIs

Las APIs (Interfaz de Programación de Aplicaciones) permiten a diferentes sistemas comunicarse entre sí. En Python, puedes usar la biblioteca `requests` para hacer llamadas a APIs.

#### Ejemplo de Llamada GET

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    print(datos)
else:
    print("Error en la solicitud")
```

### Principales Cláusulas y Conceptos

- **Métodos HTTP**: GET, POST, PUT, DELETE, etc.
- **Códigos de Estado HTTP**: 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.
- **JSON**: Formato común para intercambiar datos entre sistemas.

### Ejercicios

#### Ejercicio 1: Programa de Gestión de Libros

Crea un programa que permita gestionar libros en una biblioteca. Debe tener un menú interactivo para:
- Agregar libros (título, autor, año).
- Listar todos los libros.
- Buscar un libro por título.
- Actualizar datos de un libro.
- Eliminar un libro.

#### Ejercicio 2: Web Scraper para Noticias

Crea un programa que extraiga noticias de un sitio web utilizando Beautiful Soup. Debe permitir:
- Extraer títulos de noticias.
- Extraer enlaces a las noticias.
- Guardar los datos en un archivo CSV.

#### Ejercicio 3: API para el Clima

Crea un programa que use una API del clima para obtener el pronóstico actual de una ciudad dada. Debe permitir:
- Pedir el nombre de la ciudad al usuario.
- Mostrar el clima actual y el pronóstico para los próximos días.

## Recursos Adicionales

- Documentación oficial de Python sobre POO: [Python Documentation](https://docs.python.org/3/tutorial/classes.html)
- Documentación oficial de Beautiful Soup: [Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
- Documentación oficial de Requests: [Requests Documentation](https://requests.readthedocs.io/en/latest/)

