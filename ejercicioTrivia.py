import random

print("""JUEGO DE TRIVIA
Intenta adivinar un numero del 1 al 100
""")

numero_adivinanza = random.randint(1,100)
intentos = 0
adivinanza_usuario = -1

while intentos < 10 and adivinanza_usuario != numero_adivinanza:
    intentos += 1
    adivinanza_usuario = int(input("Ingresa tu numero del 1 al 100: "))

    if numero_adivinanza < adivinanza_usuario:
        print("El numero que intentas adivinar es menor")

    elif numero_adivinanza > adivinanza_usuario:
        print("El numero que intentas adivinar es mayor")

    elif numero_adivinanza == adivinanza_usuario:
        print("Felicidades Adivinaste el numero en", intentos, "intentos")

    if intentos >= 10:
        print("Llegaste a 10 intentos, Has perdido :c")
        print("El numero que intentabas adivinar es", numero_adivinanza)