# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos temporal para ejemplo
usuarios = [
    {'id': 1, 'nombre': 'Ana', 'email': 'ana@example.com'},
    {'id': 2, 'nombre': 'Carlos', 'email': 'carlos@example.com'},
    {'id': 3, 'nombre': 'Juan', 'email': 'juan@example.com'},
    {'id': 4, 'nombre': 'Luis', 'email': 'luis@example.com'},
]

# Endpoint principal
@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

# Endpoint con parámetro dinámico
@app.route('/usuario/<usuario_id>')
def ver_usuario(usuario_id):
    usuario = usuarios[int(usuario_id)-1]
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