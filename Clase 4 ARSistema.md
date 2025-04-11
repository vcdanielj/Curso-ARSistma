# Clase 4 Curso ARSistema
## Uso de Parámetros en Funciones y Valores por Defecto
En Python, las funciones pueden tener parámetros con valores por defecto. Esto significa que si no se proporciona un argumento para ese parámetro al llamar a la función, se usará el valor por defecto.

```python
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}!")

saludar()  # Usará el valor por defecto "Usuario"
saludar("Ana")  # Usará el argumento proporcionado "Ana"
```

## Uso del return
La palabra clave return se utiliza para devolver un valor desde una función. Una vez que se ejecuta return, la función termina y devuelve el valor especificado.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)  # 8
```
## Introducción a los Tipos de Datos de Colección
Python tiene varios tipos de datos de colección que permiten almacenar múltiples valores en una sola variable. Los más comunes son:

- Listas: Colecciones ordenadas y mutables.

- Tuplas: Colecciones ordenadas e inmutables.

- Conjuntos: Colecciones no ordenadas y sin elementos duplicados.

- Diccionarios: Colecciones no ordenadas de pares clave-valor.

### Listas
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # 1
```
### Tuplas
```python
coordenadas = (10, 20)
print(coordenadas[1])  # 20
```
### Conjuntos
```python
frutas = {"manzana", "banana", "cereza"}
print("banana" in frutas)  # True
```
### Diccionarios
```python
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana
```

## Introducción al Ciclo for
El ciclo for se utiliza para iterar sobre una secuencia (como una lista, tupla, conjunto, diccionario, o incluso un string).

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```
### Uso de range()
La función range() genera una secuencia de números que se puede usar en un ciclo for.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

## Ejercicios
1. Función con parámetros por defecto: Crea una función que tome un nombre y un saludo por defecto. Si no se proporciona un saludo, usa "Hola".

2. Devolver múltiples valores: Crea una función que tome dos números y devuelva su suma, resta, multiplicación y división.

3. Lista de números pares: Usa un ciclo for para crear una lista de los primeros 10 números pares.

4. Diccionario de contactos: Crea un diccionario con nombres y números de teléfono. Luego, itera sobre el diccionario y muestra cada contacto.

5. Conteo de vocales: Pide un texto al usuario y cuenta cuántas vocales tiene usando un ciclo for.

6. Tabla de multiplicar: Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 usando un ciclo for.

7. Filtrar números: Crea una lista de números y usa un ciclo for para filtrar y mostrar solo los números mayores que 10.

8. Suma de elementos: Crea una función que tome una lista de números y devuelva la suma de todos los elementos.

9. Búsqueda en lista: Crea una función que tome una lista y un valor, y devuelva True si el valor está en la lista, de lo contrario False.

10. Inversión de cadena: Pide un texto al usuario y usa un ciclo for para invertir la cadena y mostrarla.

## Ejercicios Avanzados

1. Ejercicio 1: Menú Interactivo
- Crea un programa que muestre un menú con las siguientes opciones:

- Sumar dos números: Pide dos números al usuario y muestra el resultado de la suma.

- Contar vocales en un texto: Pide un texto al usuario y cuenta cuántas vocales tiene.

- Generar tabla de multiplicar: Pide un número al usuario y genera su tabla de multiplicar del 1 al 10.

- Salir: Termina el programa.

- El programa debe seguir mostrando el menú hasta que el usuario elija la opción de salir.

2. Ejercicio 2: Simulación de Cajero Automático
- Crea un programa que simule un cajero automático con las siguientes funcionalidades:

- Consultar saldo: Muestra el saldo actual.

- Depositar dinero: Pide una cantidad y la suma al saldo.

- Retirar dinero: Pide una cantidad y la resta del saldo (si hay suficiente saldo).

- Salir: Termina el programa.

- El saldo inicial debe ser 1000. El programa debe validar que no se puedan retirar más fondos de los disponibles.

## Recursos Adicionales

Documentación oficial de Python sobre funciones: [Definiendo funciones](https://docs.python.org/es/3.13/tutorial/controlflow.html#defining-functions)

Documentación oficial de Python sobre tipos de datos de colección: [Tipos de datos de colección](https://docs.python.org/es/3.13/tutorial/datastructures.html)

Documentación oficial de Python sobre el ciclo for: [Ciclo for](https://docs.python.org/es/3.13/tutorial/controlflow.html#for-statements)