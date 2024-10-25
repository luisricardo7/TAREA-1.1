# Clase Libro

class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Numero de Paginas: {self.numero_paginas}")

libro = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967, 417)
libro.mostrar_informacion()
