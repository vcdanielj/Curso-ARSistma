'''
Crea un programa que pida dos números al usuario y muestre la suma, resta, multiplicación y división, división entera, potenciacion y residuo de ambos.
'''

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

suma = num1 + num2
print("Suma: ", suma)

resta = num1 - num2
print("Resta: ", resta)

multiplicacion = num1 * num2
print("Multiplicación: ", multiplicacion)

division = num1 / num2
print("División: ", division)

potenciacion = num1 ** num2
print("Potenciación: ", potenciacion)

div_entera = num1 // num2
print("División Entera: ", div_entera)

residuo = num1 % num2
print("Residuo: ", residuo)