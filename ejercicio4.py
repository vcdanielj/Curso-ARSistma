'''
Realiza un programa que solicite tres números y calcule su promedio.
'''

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
num3 = int(input("Ingresa otro número: "))

promedio = (num1 + num2 + num3) / 3

print("El promedio es: ", round(promedio, 2))