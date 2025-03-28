# Clase 9 Curso ARSistema Flask Python

## Introducción a Flask

Flask es un microframework de Python para desarrollar aplicaciones web. Es ligero, flexible y fácil de usar, lo que lo convierte en una excelente opción para crear aplicaciones web rápidas y escalables. Flask sigue el principio de "no imponer restricciones", permitiendo a los desarrolladores elegir cómo estructurar su aplicación.

### Instalación

Para instalar Flask, utiliza `pip`, el gestor de paquetes de Python:

```bash
pip install flask
```

Verifica la instalación comprobando la versión:

```bash
python -m flask --version
```

## Crear una Aplicación Básica con Flask

El siguiente ejemplo muestra cómo crear una aplicación básica en Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, mundo! Bienvenido a Flask."

if __name__ == "__main__":
    app.run(debug=True)
```

### Explicación del Código

1. **Importar Flask**: Se importa la clase `Flask` desde el paquete `flask`.
2. **Crear una instancia de Flask**: `app = Flask(__name__)` crea la aplicación.
3. **Definir rutas**: El decorador `@app.route("/")` define una ruta para la URL raíz (`/`).
4. **Iniciar el servidor**: `app.run(debug=True)` inicia el servidor en modo de depuración.

### Ejecutar la Aplicación

Guarda el archivo como `app.py` y ejecútalo:

```bash
python app.py
```

Accede a `http://127.0.0.1:5000/` en tu navegador para ver la aplicación.

---

## Rutas y Métodos HTTP

Las rutas son las URLs que definen cómo los usuarios interactúan con tu aplicación. Flask permite manejar diferentes métodos HTTP como `GET`, `POST`, `PUT`, y `DELETE`.

### Definir Rutas con Métodos HTTP

```python
@app.route("/saludo", methods=["GET", "POST"])
def saludo():
    if request.method == "POST":
        return "Recibí un POST"
    return "Recibí un GET"
```

### Parámetros en la URL

Puedes pasar parámetros en la URL utilizando ``.

```python
@app.route("/usuario/")
def usuario(nombre):
    return f"Hola, {nombre}!"
```

---

## Templates en Flask

Flask utiliza Jinja2 como motor de plantillas para generar contenido dinámico en HTML.

### Crear un Template HTML

Crea una carpeta llamada `templates` y dentro de ella un archivo llamado `index.html`:

```html

    Bienvenido


    ¡Hola, {{ nombre }}!


```

### Renderizar Templates

Usa la función `render_template()` para renderizar archivos HTML:

```python
from flask import render_template

@app.route("/bienvenida/")
def bienvenida(nombre):
    return render_template("index.html", nombre=nombre)
```

---

## Formularios y Datos del Usuario

Flask permite manejar datos enviados por formularios HTML usando el objeto `request`.

### Crear un Formulario HTML

Crea un archivo llamado `formulario.html` en la carpeta `templates`:

```html



    
    Formulario


    
        Nombre:
        
        Enviar
    


```

### Procesar Datos del Formulario

Usa el objeto `request` para acceder a los datos enviados por el formulario:

```python
from flask import request

@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = request.form["nombre"]
    return f"¡Hola, {nombre}!"
```

---

## Manejo de Archivos Estáticos

Los archivos estáticos (CSS, JavaScript, imágenes) deben colocarse en una carpeta llamada `static`.

### Estructura del Proyecto

```
mi_app/
│
├── static/
│   ├── estilos.css
│   ├── script.js
│   └── imagen.jpg
├── templates/
│   ├── index.html
│   └── formulario.html
├── app.py
```

### Usar Archivos Estáticos en Templates

Puedes referenciar archivos estáticos usando la función `url_for()`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='estilos.css') }}">
<img src="{{ url_for('static', filename='imagen.jpg') }}" alt="Imagen">

```

---

## Manejo de Errores Personalizados

Flask permite manejar errores como el 404 (Página no encontrada) o 500 (Error interno).

### Crear Páginas de Error Personalizadas

Define un manejador para errores específicos usando decoradores:

```python
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "Página no encontrada", 404
```


## Cómo hacer un POST y obtener el contenido del POST en Flask

En Flask, el método HTTP `POST` se utiliza para enviar datos al servidor. Estos datos pueden ser procesados y almacenados según las necesidades de la aplicación. A continuación, se explica cómo crear un endpoint para manejar solicitudes `POST` y cómo obtener el contenido enviado.

---

### Crear un Endpoint con POST

1. **Definir la ruta**: Usa el decorador `@app.route` para especificar la URL del endpoint y el método `POST`.
2. **Obtener datos del POST**: Utiliza `request.get_json()` para acceder a los datos enviados en formato JSON.

**Ejemplo básico**:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    # Obtener datos enviados en el cuerpo de la solicitud
    datos = request.get_json()
    
    # Validar que los datos contengan cierta información
    if 'nombre' not in datos or 'edad' not in datos:
        return jsonify({'error': 'Datos incompletos'}), 400
    
    # Procesar los datos
    nombre = datos['nombre']
    edad = datos['edad']
    
    return jsonify({'mensaje': f'Usuario {nombre} de {edad} años creado exitosamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Ejercicios Prácticos

1. **Hola Mundo Dinámico**: Crea una ruta que reciba un nombre como parámetro y lo muestre en pantalla.
   
2. **Formulario Simple**: Diseña un formulario que solicite el nombre del usuario y muestre un saludo personalizado.

3. **Conversor de Monedas**: Crea una aplicación que convierta dólares a euros usando un formulario.

4. **Contador de Visitas**: Implementa un contador que registre cuántas veces se accede a una ruta específica.

5. **Gestión de Errores**: Personaliza las páginas de error 404 y 500 con mensajes amigables.

6. **Galería de Imágenes**: Crea una galería que muestre imágenes almacenadas en la carpeta estática.

7. **Lista de Tareas**: Diseña una aplicación que permita agregar tareas a una lista y mostrarlas dinámicamente.

8. **Autenticación Básica**: Implementa un sistema básico de inicio de sesión con usuario y contraseña.

9. **API RESTful**: Diseña una API que permita realizar operaciones CRUD sobre una lista de productos.

10. **Blog Simple**: Crea un blog donde los usuarios puedan publicar artículos y verlos en una lista dinámica.

---