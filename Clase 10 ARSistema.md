## Clase 10: Curso ARSistema Flask Python - CRUD Básico con SQLite

En esta clase aprenderemos a implementar las operaciones básicas CRUD (Create, Read, Update, Delete) utilizando Flask y SQLite sin usar un ORM como SQLAlchemy. SQLite es una base de datos ligera que se integra perfectamente con Flask para aplicaciones pequeñas y medianas.

---

## **Estructura del Proyecto**

```plaintext
crud_flask/
│
├── static/
│   └── estilos.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── agregar.html
│   ├── editar.html
│   └── eliminar.html
├── database.py
└── app.py
```

---

## **Configuración Inicial**

### **1. Crear la Base de Datos (`database.py`)**

```python
import sqlite3

def crear_tabla():
    conexion = sqlite3.connect('productos.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL
    )
    ''')
    
    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    crear_tabla()
```

### **2. Configuración Básica de Flask (`app.py`)**

```python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta a la base de datos
DATABASE = 'productos.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn
```

---

## **Operaciones CRUD**

### **1. Create (Crear)**

#### Plantilla (`templates/agregar.html`):

```html
{% extends "base.html" %}

{% block content %}
<h2>Agregar Producto</h2>
<form method="POST" action="{{ url_for('agregar') }}">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" required>
    
    <label for="precio">Precio:</label>
    <input type="number" step="0.01" id="precio" name="precio" required>
    
    <label for="cantidad">Cantidad:</label>
    <input type="number" id="cantidad" name="cantidad" required>
    
    <button type="submit">Guardar</button>
</form>
{% endblock %}
```

#### Ruta en `app.py`:

```python
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        
        conn = get_db_connection()
        conn.execute('INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)',
                     (nombre, precio, cantidad))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('agregar.html')
```

---

### **2. Read (Leer)**

#### Plantilla (`templates/index.html`):

```html
{% extends "base.html" %}

{% block content %}
<h1>Lista de Productos</h1>
<a href="{{ url_for('agregar') }}">Agregar Nuevo</a>
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Cantidad</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for producto in productos %}
        <tr>
            <td>{{ producto['id'] }}</td>
            <td>{{ producto['nombre'] }}</td>
            <td>${{ "%.2f"|format(producto['precio']) }}</td>
            <td>{{ producto['cantidad'] }}</td>
            <td>
                <a href="{{ url_for('editar', id=producto['id']) }}">Editar</a>
                <a href="{{ url_for('eliminar', id=producto['id']) }}" onclick="return confirm('¿Estás seguro?')">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

#### Ruta en `app.py`:

```python
@app.route('/')
def index():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM productos').fetchall()
    conn.close()
    return render_template('index.html', productos=productos)
```

---

### **3. Update (Actualizar)**

#### Plantilla (`templates/editar.html`):

```html
{% extends "base.html" %}

{% block content %}
<h2>Editar Producto</h2>
<form method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" value="{{ producto['nombre'] }}" required>

    <label for="precio">Precio:</label>
    <input type="number" step="0.01" id="precio" name="precio" value="{{ producto['precio'] }}" required>

    <label for="cantidad">Cantidad:</label>
    <input type="number" id="cantidad" name="cantidad" value="{{ producto['cantidad'] }}" required>

    <button type="submit">Actualizar</button>
</form>
{% endblock %}
```

#### Ruta en `app.py`:

```python
@app.route('/editar/', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        
        conn.execute('UPDATE productos SET nombre = ?, precio = ?, cantidad = ? WHERE id = ?',
                     (nombre, precio, cantidad, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if producto is None:
        return redirect(url_for('index'))
    
    return render_template('editar.html', producto=producto)
```

---

### **4. Delete (Eliminar)**

#### Plantilla (`templates/eliminar.html`):

```html
{% extends "base.html" %}

{% block content %}
<h2>Eliminar Producto</h2>
<p>¿Estás seguro de que deseas eliminar "{{ producto['nombre'] }}"?</p>
<form method="POST">
    <button type="submit">Confirmar Eliminación</button>
    <a href="{{ url_for('index') }}">Cancelar</a>
</form>
{% endblock %}
```

#### Ruta en `app.py`:

```python
@app.route('/eliminar/', methods=['GET', 'POST'])
def eliminar(id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        conn.execute('DELETE FROM productos WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if producto is None:
        return redirect(url_for('index'))
    
    return render_template('eliminar.html', producto=producto)
```

---

## **Plantilla Base (`templates/base.html`)**

```html

<!DOCTYPE html>
<html lang="es">
<head>
    <title>CRUD Flask-SQLite</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='estilos.css') }}">
</head>
<body>
<div class="container">
    {% block content %}{% endblock %}
</div>
</body>
</html>

```

---

## **Ejecutar la Aplicación**

1. Crear la base de datos ejecutando `database.py`:

```bash
python database.py
```

2. Iniciar la aplicación Flask:

```bash
python app.py
```