"""
Aplicacion de Cuentas Bancarias
"""

from sqlite3 import connect

# Conectar a la base de datos SQLite
conn = connect('cuentas.db')
cursor = conn.cursor()

#Creacion de las Tablas
cursor.execute('''CREATE TABLE IF NOT EXISTS cuentas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL,
                    nro_cuenta INTEGER NOT NULL,
                    saldo INTEGER NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    clave TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS transacciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_origen INTEGER NOT NULL,
                    id_destino INTEGER NOT NULL,
                    monto INTEGER NOT NULL)''')
conn.commit()

def crearCuenta(nombre_usuario):
    cursor.execute("SELECT id, clave FROM usuarios WHERE nombre = ?", (nombre_usuario,))
    usuario = cursor.fetchone()
    id_usuario = usuario[0]
    clave = usuario[1]
    deposito_inicial = int(input("Ingresa el monto inicial de tu cuenta: "))
    numero_cuenta = int(input("Ingresar numero de cuenta: "))
    cursor.execute("INSERT INTO cuentas (id_usuario, nro_cuenta, saldo) VALUES (?, ?, ?)", (id_usuario, numero_cuenta, deposito_inicial))
    conn.commit()
    print("Cuenta creada exitosamente")

def crearUsuario():
    nombre_usuario = input("Ingresa el nombre de usuario: ")
    clave = input("Ingresa tu clave: ")
    confirmacion = input("Confirma tu clave: ")
    while clave != confirmacion:
        print("Las claves no coinciden")
        clave = input("Ingresa tu clave: ")
        confirmacion = input("Confirma tu clave: ")

    cursor.execute("INSERT INTO usuarios (nombre, clave) VALUES (?, ?)", (nombre_usuario, clave))
    conn.commit()
    print("Usuario Registrado Exitosamente")
    crearCuenta(nombre_usuario)

while True:
    opcion = int(input('''                       
[1] Registrarme 
[2] Iniciar Sesión
[3] Salir
'''))
    if opcion == 1:
        crearUsuario()
    elif opcion == 3:
        conn.close()
        quit()