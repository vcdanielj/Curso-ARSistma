"""
Simulación de dados: Lanza dos dados hasta que la suma sea un número primo. Muestra cuántos lanzamientos tomó.
"""

import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

verificar = dado1 + dado2
bandera = verificar - 1

while(bandera != 1):
    residuo = verificar % bandera
    bandera -= 1
    if (residuo == 0):
        print(verificar, "No es primo")
        quit()

print(verificar, "Es primo")
