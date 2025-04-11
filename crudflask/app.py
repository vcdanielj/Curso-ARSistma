from flask import Flask, render_template, request
import sqlite3

#Iniciar Aplicación Flask
app = Flask(__name__)

#Conectarnos a la Base de Datos
bd = sqlite3.connect("bd_productos.sqlite3")
cursor = bd.cursor()

#Configuración de los Endpoints y Rutas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crear', methods=["GET", "POST"])
def crear():
    if request.method == "GET":
        return render_template('crear.html')
    elif request.method == "POST":
        print(request.form)

@app.route('/editar', methods=["GET", "UPDATE"])
def editar():
    return "editar"

@app.route('/eliminar', methods=["GET", "DELETE"])
def eliminar():
    return "eliminar"


#Correr el servicio
if __name__ == '__main__':
    app.run(debug=True)