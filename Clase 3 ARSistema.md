# Clase 3 Curso ARSistema

## Repaso de Ciclos while
Los ciclos while permiten repetir un bloque de código mientras una condición sea verdadera.

```python
contador = 1
while contador <= 5:
    print("Iteración número", contador)
    contador += 1  # Incremento para evitar ciclo infinito
```
### Uso de break y continue

break: Termina el ciclo inmediatamente.

continue: Salta a la siguiente iteración del ciclo.

```python
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue  # Salta la iteración cuando contador es 5
    if contador == 8:
        break  # Termina el ciclo cuando contador es 8
    print(contador)
```

## Funciones Incorporadas en Python

Algunas Funciones Incorporadas

- len(): retorna el numero de caracteres en un string
```python

print(len("Hola"))  # 4
```
- abs(): Retorna el valor absoluto de un número.
```python

print(abs(-10))  # 10
```
- round(): Redondea un número a un número específico de decimales.

```python

print(round(3.14159, 2))  # 3.14
```
- eval(): Evalúa una expresión escrita como cadena.

```python

resultado = eval("10 + 5 * 2")
print(resultado)  # 20
```
- type(): Retorna el tipo de dato de un objeto.

```python

print(type(numeros))  # <class 'list'>
```

[Link a Documentación de Python con lista de Funciones Incorporadas](https://docs.python.org/es/3.13/library/functions.html)

## Introducción a Funciones
Las funciones son bloques de código reutilizables que realizan una tarea específica. Se definen usando la palabra clave def.

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")  # Llamada a la función
```

## Parámetros y Argumentos
Los parámetros son variables que se definen en la función, mientras que los argumentos son los valores que se pasan a la función cuando se llama.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)  # 3 y 5 son argumentos
print(resultado)  # 8
```

## Ejercicios

1. Suma condicionada: Pide números al usuario hasta que la suma de los pares sea mayor que 100. Muestra la suma al final.

2. Multiplicación selectiva: Pide un número y muestra su tabla del 2 al 5 y del 8 al 10. Usa continue.

3. Simulación de dados: Lanza dos dados hasta que la suma sea un número primo. Muestra cuántos lanzamientos tomó.

4. Cajero simplificado: Saldo inicial 100. Opciones: retirar (mínimo 10), depositar (máximo 500). Repite hasta que el saldo sea 0 o el usuario elija salir.

5. Juego de cartas: Simula robar cartas de una baraja hasta que la suma de los valores supere 21.

6. Conversión a binario: Pide un número y conviértelo a binario usando divisiones sucesivas (bucle while).

7. Análisis de texto: Pide un texto. Cuenta palabras, letras, vocales. Muestra resultados.