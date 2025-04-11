'''
Crea un programa que solicite el radio de un círculo y muestre su área 
(π * r^2).
'''

import math

PI = math.pi
radio = float(input("Ingresa el radio del cìrculo: "))

area = PI * (radio ** 2)

area = round(area, 2)

print("El area del circulo es:", area)