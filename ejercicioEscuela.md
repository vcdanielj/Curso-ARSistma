# Ejercicio: Programa CRUD para una Escuela

## Objetivo
Crear un programa que permita gestionar estudiantes en una escuela. El programa debe tener un menú interactivo que permita realizar las siguientes operaciones:

- **Agregar estudiantes**: Debe solicitar el nombre, edad y curso del estudiante.
- **Listar estudiantes**: Muestra todos los estudiantes registrados.
- **Buscar estudiante**: Busca un estudiante por su nombre.
- **Actualizar datos de un estudiante**: Permite cambiar el nombre, edad o curso de un estudiante existente.
- **Eliminar estudiante**: Elimina un estudiante de la base de datos.

## Indicaciones para la Implementación

### 1. Diseño de la Base de Datos
- **Tabla**: `estudiantes`
  - **Columnas**:
    - `id`: Identificador único para cada estudiante (clave primaria).
    - `nombre`: Nombre del estudiante.
    - `edad`: Edad del estudiante.
    - `curso`: Curso al que pertenece el estudiante.

### 2. Creación de la Base de Datos
- Utiliza SQLite para crear la base de datos y la tabla `estudiantes`.
- Asegúrate de que la tabla tenga los campos necesarios (`id`, `nombre`, `edad`, `curso`).

### 3. Implementación del Menú
- Crea un bucle que muestre el menú y espere la entrada del usuario.
- Utiliza condicionales (`if`, `elif`, `else`) para ejecutar la acción correspondiente según la opción elegida.

### 4. Funcionalidades CRUD
- **Agregar estudiante**:
  - Pide al usuario que ingrese el nombre, edad y curso del estudiante.
  - Utiliza una consulta SQL `INSERT INTO` para agregar el nuevo estudiante a la base de datos.
- **Listar estudiantes**:
  - Utiliza una consulta SQL `SELECT * FROM estudiantes` para obtener todos los registros.
  - Muestra los resultados en pantalla.
- **Buscar estudiante**:
  - Pide al usuario que ingrese el nombre del estudiante a buscar.
  - Utiliza una consulta SQL `SELECT * FROM estudiantes WHERE nombre = ?` para buscar el estudiante.
  - Muestra los resultados si se encuentra el estudiante.
- **Actualizar datos de un estudiante**:
  - Pide al usuario que ingrese el nombre del estudiante a actualizar.
  - Busca el estudiante usando una consulta SQL similar a la de búsqueda.
  - Si se encuentra, pide al usuario que ingrese los nuevos datos (nombre, edad, curso).
  - Utiliza una consulta SQL `UPDATE` para actualizar los datos del estudiante.
- **Eliminar estudiante**:
  - Pide al usuario que ingrese el nombre del estudiante a eliminar.
  - Busca el estudiante usando una consulta SQL similar a la de búsqueda.
  - Si se encuentra, utiliza una consulta SQL `DELETE FROM` para eliminar el estudiante.
