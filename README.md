# Sistema de Biblioteca

## Descripción del funcionamiento

El programa está compuesto por varias clases:

- **Libro**: Clase base que contiene atributos comunes como título, autor y año de publicación, además de un método `mostrar_info()` que muestra esta información.
- **LibroDigital**: Hereda de `Libro` y añade el atributo `formato`. Sobrescribe `mostrar_info()` utilizando `super()` para mostrar la información del libro y luego el formato.
- **LibroFisico**: Hereda de `Libro` y añade el atributo `num_paginas`. También sobrescribe `mostrar_info()` utilizando `super()` para mostrar la información común y luego el número de páginas.
- **Biblioteca**: Administra una lista de libros. Permite:
  - Agregar libros a la colección (`agregar_libro`).
  - Mostrar todos los libros (`mostrar_todos`).
  - Buscar libros por autor (`buscar_por_autor`).

El código incluye validaciones para asegurar que los datos ingresados sean correctos (por ejemplo, que el año sea un número y que el número de páginas sea positivo).

## Ejecución

Al ejecutar `biblioteca.py`, el programa:
1. Crea una biblioteca.
2. Agrega ejemplos de libros físicos y digitales.
3. Muestra todos los libros registrados.
4. Realiza una búsqueda de libros por autor y muestra los resultados.
