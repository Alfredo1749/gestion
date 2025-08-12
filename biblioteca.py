# Clase base Libro
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        # Validación de datos
        if not titulo or not autor:
            raise ValueError("El título y el autor no pueden estar vacíos.")
        if not str(anio_publicacion).isdigit():
            raise ValueError("El año de publicación debe ser un número entero.")

        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = int(anio_publicacion)

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")


# Clase LibroDigital que hereda de Libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio_publicacion, formato):
        # Usamos super() para inicializar los atributos de la clase padre
        super().__init__(titulo, autor, anio_publicacion)
        if not formato:
            raise ValueError("El formato no puede estar vacío.")
        self.formato = formato

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Formato: {self.formato}")


# Clase LibroFisico que hereda de Libro
class LibroFisico(Libro):
    def __init__(self, titulo, autor, anio_publicacion, num_paginas):
        # Inicializamos atributos de la clase base con super()
        super().__init__(titulo, autor, anio_publicacion)
        if not str(num_paginas).isdigit() or int(num_paginas) <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo.")
        self.num_paginas = int(num_paginas)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de páginas: {self.num_paginas}")


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = [] 

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("Solo se pueden agregar objetos de tipo Libro.")
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente.")

    def mostrar_todos(self):
        if not self.libros:
            print("La biblioteca está vacía.")
            return
        for libro in self.libros:
            libro.mostrar_info()
            print("-" * 40)

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if not encontrados:
            print(f"No se encontraron libros del autor '{autor}'.")
        else:
            for libro in encontrados:
                libro.mostrar_info()
                print("-" * 40)

biblioteca = Biblioteca()

try:
    libro1 = LibroFisico("Cien años de soledad", "Gabriel García Márquez", 1967, 417)
    libro2 = LibroDigital("El Principito", "Antoine de Saint-Exupéry", 1943, "PDF")
    libro3 = LibroFisico("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 863)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

except ValueError as e:
    print(f"Error: {e}")

print("\nTodos los libros en la biblioteca:")
biblioteca.mostrar_todos()

print("\nBuscando libros de 'Gabriel García Márquez':")
biblioteca.buscar_por_autor("Gabriel García Márquez")
