'''
Escribe un programa que convierta grados Celsius a Fahrenheit con la fórmula: F=(C×9/5)+32
'''

celsius = float(input("Ingresar grados celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(celsius, "grados celsius, equivale a", fahrenheit, "grados fahrenheit")