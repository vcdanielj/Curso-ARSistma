
```python
# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos temporal para ejemplo
usuarios = [
    {'id': 1, 'nombre': 'Ana', 'email': 'ana@example.com'},
    {'id': 2, 'nombre': 'Carlos', 'email': 'carlos@example.com'}
]

# Endpoint principal
@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

# Endpoint con parámetro dinámico
@app.route('/usuario/')
def ver_usuario(usuario_id):
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    return render_template('usuario.html', usuario=usuario)

# Endpoint para formulario (GET y POST)
@app.route('/registro', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        nuevo_usuario = {
            'id': len(usuarios) + 1,
            'nombre': request.form['nombre'],
            'email': request.form['email']
        }
        usuarios.append(nuevo_usuario)
        return redirect(url_for('index'))
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Estructura de archivos
```
proyecto/
├── templates/
│   ├── base.html        # Plantilla base
│   ├── index.html       # Lista de usuarios
│   ├── usuario.html     # Detalle de usuario
│   └── registro.html    # Formulario de registro
└── app.py
```

---

## Plantillas HTML (usando Jinja2)

**1. base.html (Plantilla base)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}App Flask{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>Aplicación de Usuarios</h1>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**2. index.html**
```html
{% extends 'base.html' %}

{% block title %}Inicio{% endblock %}

{% block content %}
    <h2>Lista de Usuarios</h2>
    <ul>
        {% for usuario in usuarios %}
            <li>
                <a href="{{ url_for('ver_usuario', usuario_id=usuario.id) }}">
                    {{ usuario.nombre }}
                </a>
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('registrar_usuario') }}" class="button">Nuevo Usuario</a>
{% endblock %}
```

**3. usuario.html**
```html
{% extends 'base.html' %}

{% block title %}Detalle de Usuario{% endblock %}

{% block content %}
    {% if usuario %}
        <h2>{{ usuario.nombre }}</h2>
        <p>Email: {{ usuario.email }}</p>
        <p>ID: {{ usuario.id }}</p>
    {% else %}
        <p>Usuario no encontrado</p>
    {% endif %}
    <a href="{{ url_for('index') }}">Volver al inicio</a>
{% endblock %}
```

**4. registro.html**
```html
{% extends 'base.html' %}

{% block title %}Registro{% endblock %}

{% block content %}
    <h2>Registrar Nuevo Usuario</h2>
    <form method="POST">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <button type="submit">Registrar</button>
    </form>
{% endblock %}
```

---

## Funcionamiento clave

1. **Routing Dinámico**:
   - `/` muestra lista de usuarios[1][6]
   - `/usuario/` muestra detalles específicos usando parámetros en URL[3][5]
   - `/registro` maneja GET (formulario) y POST (procesamiento)[3][6]

2. **Plantillas con Herencia**:
   - `base.html` define estructura común[4][5]
   - Otras plantillas extienden la base usando `{% extends %}`[1][4]

3. **Pasando Datos**:
   - Variables enviadas desde Python (`usuarios`, `usuario`)[1][5]
   - Uso de `url_for()` para generar URLs[6]

4. **Manejo de Formularios**:
   - `request.method` diferencia GET/POST[3][6]
   - `request.form` accede a datos enviados[3][6]

---
