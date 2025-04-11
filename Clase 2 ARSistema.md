#  Clase 2 Curso ARSistema

## Repaso de Variables

Las variables son contenedores para almacenar datos en la memoria del computador. En Python, una variable se declara asignando un valor con =.
```python
nombre = "Juan"
edad = 30
altura = 1.75
es_estudiante = True
```

### Convenciones de Nombramiento de Variables

- Usar nombres descriptivos y en minúsculas.

- Separar palabras con guiones bajos (snake_case).

- Evitar palabras reservadas de Python (como print, if, while).

- Sensible a mayúsculas y minúsculas (nombre y Nombre son diferentes).

- Usar nombres significativos (precio_total en lugar de p).

## Espaciado y Estilo de Código (PEP 8)

- Usar 4 espacios por nivel de indentación.

- Dejar espacios alrededor de operadores (a = b + c).

- Limitar líneas a 79 caracteres.

- Agregar una línea en blanco entre definiciones de funciones.

- Los comentarios deben ser claros y concisos.

## Operaciones

Python permite realizar operaciones matemáticas y lógicas con diferentes tipos de datos.

### Operadores Aritméticos

```python
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5  # Resultado en float
modulo = 10 % 3  # Resto de la división
exponente = 2 ** 3  # 2 elevado a la 3
```

### Operadores de Comparación

```python
mayor_o_igual = 10 >= 10  # True
menor_o_igual = 5 <= 10  # True
mayor = 10 > 10  # Falso
menor = 5 < 10  # True
menor = 5 < 10  # True
igual = 5 == 5  # True
diferente = "d" != "r"  # True
```

### Operadores Lógicos

```python
es_mayor = (10 > 5) and (5 > 2)  # True
es_menor = (10 < 5) or (5 > 2)  # True
es_negado = not (10 > 5)  # False
```
## Tipos de Datos

Python maneja diversos tipos de datos:

```python
numero_entero = 10  # int
numero_decimal = 3.14  # float
texto = "Hola"  # str
valor_booleano = True  # bool
```

Se puede verificar el tipo de una variable con type():

```python
print(type(numero_entero))  # <class 'int'>
print(type(numero_decimal))  # <class 'float'>
print(type(texto))  # <class 'str'>
print(type(valor_booleano))  # <class 'bool'>
```

## Condicionales

Las estructuras condicionales permiten ejecutar diferentes bloques de código según una condición.

```python
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")
else:
    print("Eres menor de edad.")
```

## Introducción a Ciclos con while

Los ciclos permiten repetir un bloque de código mientras una condición se cumpla.

```python
contador = 1
while contador <= 5:
    print("Iteración número", contador)
    contador += 1  # Incremento para evitar ciclo infinito
```

## Ejercicios de Repaso

1. Declara variables de tipo int, float, str y bool. Imprime sus valores y tipos.

2. Solicita al usuario un número y muestra si es positivo, negativo o cero.

3. Crea un programa que solicite tres números y determine cuál es el mayor.

4. Escribe un programa que convierta kilómetros a millas usando la fórmula: millas = km * 0.621371.

5. Escribe un programa que pida un número y determine si es par o impar.

6. Realiza un programa que solicite un número y muestre su tabla de multiplicar del 1 al 10 usando un ciclo while.

7. Crea un programa que solicite una contraseña y permita tres intentos antes de bloquear el acceso.

8. Escribe un programa que cuente del 1 al 10 usando un ciclo while y muestre cada número en pantalla.