# Biblioteca Fire and Blood
### Desarrollado por Sofia Ferrari

## Descripción General
Biblioteca Fire and Blood es una aplicación desarrollada en Python que permite administrar una biblioteca mediante una interfaz de consola. El sistema gestiona materiales bibliográficos, socios y préstamos.
La información inicial de la biblioteca se carga desde un archivo JSON que contiene los libros, mangas y socios registrados en el sistema.

## Ejecución
Para ejecutar la aplicación:
`python main.py`

## Funcionalidades

#### Gestión de materiales
- Registro de nuevos libros.
-	Registro de nuevos mangas.
-	Asignación automática de ID para cada material.
-	Consulta de materiales disponibles.
-	Búsqueda de materiales por título o autor.
-	Visualización del estado de disponibilidad.

#### Gestión de socios
- Registro de nuevos socios.
-	Asignación automática de ID para cada socio.
-	Consulta de información mediante DNI.
-	Listado de socios habilitados.

#### Gestión de préstamos
-	Registro de préstamos de materiales.
-	Registro de devoluciones.
-	Generación automática de fecha de devolución (30 días).
-	Consulta de préstamos activos.
-	Consulta de préstamos vencidos.

#### Estructura del proyecto
-	`main.py:` menú principal e interacción con el usuario.
-	`BIBLIOTECA.py:` administración general de la biblioteca y registro de materiales.
-	`MATERIAL.py:` definición de las clases `Material`, `Libro` y `Manga`.
-	`SOCIOS.py:` definición de la clase `Socio` y registro de socios.
-	`PRESTAMO.py:` definición de la clase `Prestamo` y gestión de préstamos y devoluciones.
-	`datos.json:` almacenamiento de los datos iniciales de materiales y socios.
