'''
Crea un programa que solicite al usuario una contraseña y verifique si es correcta (define una contraseña fija en el código).
'''

CONTRASENA = "123"

intentos = 0

contrasena_usuario = ""

while intentos < 3 and CONTRASENA != contrasena_usuario:
    contrasena_usuario = input("Ingresa la contraseña: ")
    if CONTRASENA == contrasena_usuario:
        print("Contraseña Correcta")
    else: 
        intentos += 1
        print("Contraseña Incorrecta")
        print("Intentos:", intentos)
        if intentos == 3:
            print("No tiene más intentos")

