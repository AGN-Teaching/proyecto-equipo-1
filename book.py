import random


# Creamos la clase 'Book' para los libros en catálogo.
class Book:
    def __init__(self, title, autor, ejemplares_disponibles, lugar_edicion, anno_edicion, editorial, numero_paginas):
        self.__title = title.upper()  # Almacena el título del libro en mayúsculas.
        self.__autor = autor.upper()  # Almacena el nombre del autor del libro en mayúsculas.
        self.__lugar_edicion = lugar_edicion  # Almacena el lugar de edición.
        self.__editorial = editorial  # Almacena la editorial.
        self.__anno_edicion = str(anno_edicion)  # Almacena el año de edición del libro.
        self.__numero_paginas = str(numero_paginas)  # Almacena el número de páginas.
        self.__ejemplares_disponibles = ejemplares_disponibles  # Almacena el número de ejemplares disponibles.
        self.__ID = self.__title[:2] + self.__autor[:2] + str(random.randint(0, 500))

    def get_title(self):
        return self.__title

    def get_ejemplares(self):
        return self.__ejemplares_disponibles

    def get_id(self):
        return self.__ID

    def disponibilidad(self, answer):
        if answer:
            self.__ejemplares_disponibles += 1
            print('Se devolvió con éxito.')
        else:
            self.__ejemplares_disponibles -= 1
            print('Se rentó con éxito.')

    def cadena(self):
        return {'ID: ': self.__ID, 'Autor: ': self.__autor, 'Lugar de edición: ': self.__lugar_edicion,
                'Editorial: ': self.__editorial, 'Año de edición: ': self.__anno_edicion,
                'No. páginas: ': self.__numero_paginas, 'Ejemplares disponibles: ': self.__ejemplares_disponibles}
        # Regresamos los datos que se recolectaron sobre el libro.
