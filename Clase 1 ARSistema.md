# Clase 1 Curso ARSistema

## 1. Algoritmos y Pseudocódigo

### Características de un Algoritmo

Un algoritmo es una secuencia de pasos lógicos y finitos para resolver un problema. Sus características principales son:

- **Precisión**: Cada paso debe estar bien definido.
- **Orden**: Deben ejecutarse en una secuencia específica.
- **Finitud**: Debe terminar después de un número definido de pasos.
- **Entrada y salida**: Recibe datos y devuelve resultados.

### Entorno de Desarrollo: VS Code y Consola de Comandos

- **VS Code**: Editor de código que permite escribir, depurar y ejecutar programas en Python.

- **Extensiones en VS Code**:

  - **Python**: Proporciona resaltado de sintaxis, autocompletado y herramientas de depuración.
  - **GitHub Copilot**: Asistente de programación que sugiere líneas de código y funciones completas basadas en el contexto del archivo.
  - **Codeium**: Asistente de programación que sugiere líneas de código y funciones completas basadas en el contexto del archivo.
  - **Material Icon Theme**: Proporciona un conjunto de íconos para archivos y carpetas en VS Code, mejorando la visualización del proyecto.
  - **Prettier**: Formateador de código que asegura un estilo consistente.
  - **Code Spell Checker**: Verifica la ortografía en el código y comentarios.
  - **Live Share**: Facilita la colaboración en tiempo real con otros desarrolladores.
  - **Spanish Language Kit**: Editor de Còdigo paquete de español

- **Consola de Comandos**:

Se utiliza para ejecutar scripts de Python con el comando `python nombre_del_archivo.py`.

- **Atajos Útiles en VS Code**:

  - `Ctrl + Ñ`: Abrir/Cerrar la terminal integrada.
  - `Ctrl + Shift + P`: Abrir la paleta de comandos.
  - `Ctrl + /`: Comentar o descomentar líneas de código.
  - `Alt + ↑ / ↓`: Mover líneas de código arriba o abajo.

- **Temas de Colores**:

  - VS Code permite personalizar el esquema de colores desde `Archivo > Preferencias > Tema de Color`.
  - Algunos temas populares incluyen: **Dark+, Light+, Monokai, Dracula, Solarized**.

- **Señalización de Errores en Código**:

  - La extensión **Python** en VS Code resalta errores de sintaxis y proporciona sugerencias de corrección.
  - Los errores comunes incluyen nombres de variables no definidas, errores de indentación y problemas con tipos de datos.
  - Se pueden ver detalles de los errores pasando el cursor sobre las líneas subrayadas en rojo.

---

## 2. Python

### Fundamentos del Lenguaje

Python es un lenguaje de programación interpretado, de alto nivel y multiparadigma.

### Características

- Sintaxis sencilla y fácil de leer.
- Gestión automática de memoria.
- Amplia comunidad y bibliotecas disponibles.

### Ventajas y Usos

- Desarrollo web.
- Análisis de datos y machine learning.
- Scripting y automatización.
- Aplicaciones científicas y académicas.

---

## 3. Entrada y Salida de Datos

### Funciones `input` y `print`

- `input()`: Captura datos del usuario.
- `print()`: Muestra datos en la consola.

```python
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)
```

### Conceptos Básicos de Programación

#### Variables

Las variables son espacios en la memoria que almacenan valores. En Python, no requieren declaración explícita de tipo de dato.

```python
edad = 25
nombre = "Ana"
altura = 1.75
es_estudiante = True
```

- **Reglas para nombrar variables**:

  - Deben comenzar con una letra o guion bajo (`_`).
  - No pueden contener espacios ni caracteres especiales.
  - Son sensibles a mayúsculas y minúsculas (`edad` y `Edad` son diferentes).

- **Reasignación de valores**:

  - Se puede cambiar el valor de una variable en cualquier momento:

  ```python
  contador = 10
  contador = contador + 1
  print(contador)  # Imprimirá 11
  ```

#### Operaciones

Python admite operaciones matemáticas y lógicas:

```python
suma = 5 + 3
producto = 4 * 2
es_mayor = 10 > 5
```

#### Tipos de Datos

- `int`: Enteros (`10`, `-5`)
- `float`: Decimales (`3.14`, `-2.7`)
- `str`: Cadenas de texto (`"Hola"`)
- `bool`: Booleanos (`True`, `False`)

#### Operadores 

- **Aritméticos**: `+`, `-`, `*`, `/`, `%`, `**`, `//`
  - `+`: Suma
  - `-`: Resta
  - `*`: Multiplicación
  - `/`: División
  - `%`: Módulo (resto de la división)
  - `**`: Exponenciación
  - `//`: División entera

- **Comparación**: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - `==`: Igual a
  - `!=`: Diferente a
  - `>`: Mayor que
  - `<`: Menor que
  - `>=`: Mayor o igual que
  - `<=`: Menor o igual que

- **Lógicos**: `and`, `or`, `not`
  - `and`: Verdadero si ambas condiciones son verdaderas
  - `or`: Verdadero si al menos una condición es verdadera
  - `not`: Invierte el valor de verdad


#### Condicionales

Permiten ejecutar diferentes bloques de código según una condición:

```python
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

## Ejercicios

1. Escribe un programa que pida al usuario su nombre y edad, y luego imprima un mensaje que diga: "Hola [nombre], tienes [edad] años."

2. Modifica el programa anterior para convertir la edad ingresada en años a meses.

3. Crea un programa que pida dos números al usuario y muestre la suma, resta, multiplicación y división de ambos.

4. Realiza un programa que solicite tres números y calcule su promedio.

5. Crea un programa que solicite el radio de un círculo y muestre su área `(π * r^2)`.

6. Escribe un programa que convierta grados Celsius a Fahrenheit con la fórmula: `F=(C×9/5)+32`

7. Declara variables de tipo int, float, str, y bool, asigna valores y muestra sus tipos con la función type().

8. Crea un programa que solicite al usuario una contraseña y verifique si es correcta (define una contraseña fija en el código).

9. Escribe un programa que pregunte al usuario su edad y determine si puede votar (mayor o igual a 18 años).

