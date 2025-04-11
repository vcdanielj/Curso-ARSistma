"""
Multiplicación selectiva: Pide un número y muestra su tabla del 2 al 5 y del 8 al 10. Usa continue.
"""

numero = int(input("Ingresa un numero: "))
bandera = 2

while bandera <= 10:
    if (bandera == 6 or bandera == 7 ):
        bandera += 1
        continue

    print(bandera, "*", numero,"=", bandera * numero)
    bandera += 1

print("Finalizado")