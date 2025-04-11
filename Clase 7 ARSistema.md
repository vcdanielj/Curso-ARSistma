# Clase 7 ARSistema
## Introducción a SQLite
SQLite es un sistema de gestión de bases de datos relacionales que es autónomo, servidorless, de código abierto y de uso gratuito. Es ideal para aplicaciones que requieren una base de datos ligera y fácil de implementar.

## Instalación y Configuración
Para usar SQLite en Python, necesitas importar el módulo `sqlite3`. No requiere instalación adicional ya que viene incluido en la biblioteca estándar de Python.

```python
import sqlite3
```

## Creación de una Base de Datos
Para crear una base de datos, simplemente debes conectar a una base de datos que no existe; SQLite la creará automáticamente.

```python
# Conectar a la base de datos
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Cerrar la conexión
conexion.close()
```

## Tipos de Datos en SQLite
SQLite tiene cuatro tipos de datos primitivos:

- **INTEGER**: Para valores numéricos enteros.
- **REAL**: Para valores numéricos con decimales.
- **TEXT**: Para cadenas de caracteres.
- **BLOB**: Para datos binarios.

Aunque SQLite tiene un sistema de tipos dinámicos, donde el tipo de un valor está asociado al propio valor y no a la columna, es común usar los nombres de tipo INTEGER, REAL, TEXT y BLOB para definir columnas. Otros tipos como `CHARACTER`, `VARCHAR`, `DECIMAL`, etc., se agrupan bajo estos cuatro tipos básicos debido a la afinidad de tipos[1][2][3].

## Consultas Básicas
Las consultas en SQLite se realizan mediante el lenguaje SQL. Aquí tienes algunos ejemplos básicos:

### Crear Tabla
```sql
CREATE TABLE usuarios IF NOT EXISTS (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER
);
```

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER
    );
''')
conexion.commit()
```

### Insertar Datos
```sql
INSERT INTO usuarios (nombre, edad) VALUES ('Ana', 25);
```

```python
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Ana', 25)")
conexion.commit()
```
```python
nombre = 'Ana'
edad = 25
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
conexion.commit()
```

### Seleccionar Datos
```sql
SELECT * FROM usuarios;
```

```python
cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()
for fila in filas:
    print(fila)
```

### Actualizar Datos
```sql
UPDATE usuarios SET edad = 26 WHERE nombre = 'Ana';
```

```python
cursor.execute("UPDATE usuarios SET edad = 26 WHERE nombre = 'Ana'")
conexion.commit()
```

### Eliminar Datos
```sql
DELETE FROM usuarios WHERE nombre = 'Ana';
```

```python
cursor.execute("DELETE FROM usuarios WHERE nombre = 'Ana'")
conexion.commit()
```

## Principales Cláusulas SQL
- **WHERE**: Se utiliza para filtrar registros.
- **ORDER BY**: Ordena los resultados en orden ascendente o descendente.
- **LIMIT**: Limita el número de filas devueltas.
- **JOIN**: Combina registros de dos o más tablas.

```sql
-- Ejemplo de WHERE
SELECT * FROM usuarios WHERE edad > 18;

-- Ejemplo de ORDER BY
SELECT * FROM usuarios ORDER BY edad DESC;

-- Ejemplo de LIMIT
SELECT * FROM usuarios LIMIT 5;

-- Ejemplo de JOIN (requiere dos tablas relacionadas)
SELECT * FROM usuarios
JOIN cursos ON usuarios.id = cursos.id_usuario;
```

## Ejercicios

### Ejercicio 1: Programa CRUD para una Escuela
Crea un programa que permita gestionar estudiantes en una escuela. Debe tener un menú interactivo para:
- Agregar estudiantes (nombre, edad, curso).
- Listar todos los estudiantes.
- Buscar un estudiante por nombre.
- Actualizar datos de un estudiante.
- Eliminar un estudiante.

### Ejercicio 2: Programa CRUD para una Aerolínea
Crea un programa que permita gestionar vuelos en una aerolínea. Debe tener un menú interactivo para:
- Agregar vuelos (número de vuelo, destino, fecha).
- Listar todos los vuelos.
- Buscar un vuelo por número de vuelo.
- Actualizar datos de un vuelo.
- Eliminar un vuelo.

## Recursos Adicionales

- Documentación oficial de SQLite: [SQLite Documentation](https://www.sqlite.org/docs.html)
- Documentación oficial de Python sobre sqlite3: [sqlite3 — SQLite Database](https://docs.python.org/3/library/sqlite3.html)

