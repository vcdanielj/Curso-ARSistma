import sqlite3

"""
Ejercicio 2: Simulación de Cajero Automático

Crea un programa que simule un cajero automático con las siguientes funcionalidades:

Consultar saldo: Muestra el saldo actual.

Depositar dinero: Pide una cantidad y la suma al saldo.

Retirar dinero: Pide una cantidad y la resta del saldo (si hay suficiente saldo).

Salir: Termina el programa.

El saldo inicial debe ser 1000. El programa debe validar que no se puedan retirar más fondos de los disponibles.
"""
# Conectar a la base de datos SQLite
conn = sqlite3.connect('cajero.db')
cursor = conn.cursor()


# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS cuenta (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    saldo INTEGER NOT NULL)''')

# Insertar saldo inicial si la tabla está vacía
cursor.execute('SELECT COUNT(*) FROM cuenta')
if cursor.fetchone()[0] == 0:
    cursor.execute('INSERT INTO cuenta (saldo) VALUES (1000)')
    conn.commit()

def obtener_saldo():
    cursor.execute('SELECT saldo FROM cuenta WHERE id = 1')
    return cursor.fetchone()[0]

def actualizar_saldo(nuevo_saldo):
    cursor.execute('UPDATE cuenta SET saldo = ? WHERE id = 1', (nuevo_saldo,))
    conn.commit()

while True:
    opcion = int(input("""
[1] Consultar Saldo
[2] Depositar 
[3] Retirar
[4] Salir
"""))
    if opcion == 1:
        saldo = obtener_saldo()
        print(f"Su saldo es: {saldo}")
    elif opcion == 2:
        deposito = int(input("Ingresa el monto del deposito: "))
        if deposito < 0:
            print("Deposito Invalido. Debe ser un monto mayor a 0")
        else:
            saldo = obtener_saldo()
            saldo += deposito
            actualizar_saldo(saldo)
            print(f"Monto depositado exitosamente")
            print(f"Saldo Actual: {saldo}")
    elif opcion == 3:
        retiro = int(input("Ingrese el monto del retiro: "))
        saldo = obtener_saldo()
        if retiro > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= retiro
            actualizar_saldo(saldo)
            print(f"Monto retirado exitosamente")
            print(f"Saldo Actual: {saldo}")
    elif opcion == 4:
        conn.close()
        quit()
    else:
        print("Opcion Invalida")