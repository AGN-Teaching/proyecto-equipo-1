    def __init__(self):
        self.__catalogue = {}   # Diccionario para almacenar información sobre libros.
        self.__users = {}   # Diccionario para almacenar información sobre usuarios.
        self.__convenience_library = {}   # Diccionario para almacenar información sobre bibliotecas auxiliares.

# Función para buscar un libro en el catálogo de la biblioteca.
    def buscar_libro(self, book):
        answer, book = buscar(book, self.__catalogue)
        return answer, book

# Función para agregar un nuevo libro al catálogo de la biblioteca.
    def agregar_libro(self, book_name, book_author, book_available, book_place, book_year, book_editorial, book_pages):
        self.__catalogue[book_name] = Book(book_name, book_author, book_available, book_place, book_year,
                                           book_editorial, book_pages)

# Administra el catálogo (objetos).
    def anexar_simple(self, objeto):
        nombre_archivo = objeto.get_title()
        self.__catalogue[nombre_archivo] = objeto

# Función para eliminar un libro del catálogo de la biblioteca.
    def eliminar_libro(self, book, answer):
        if answer:
            self.__catalogue.pop(book)
            print(book + ' se ha eliminado correctamente.')
        else:
            print(book + ' no se ha podido eliminar')

# Función para mostrar el catálogo de libros.
    def get_catalogo(self):
        for titulos, book in self.__catalogue.items():
            print(titulos)
            atributos = book.cadena()
            for key, valor in atributos.items():
                print(f'{key} {valor}')
            print('')

# Función para agregar un usuario en el catálogo de usuarios.
    def agregar_usuario(self, user_name, user_last_name, user_edge, user_address):
        self.__users[user_name] = Usuario_Bi(user_name, user_last_name, user_edge, user_address)
        return self.__users[user_name].get_id()

# Función para buscar un usuario en el catálogo de usuarios.
    def buscar_usuario(self, user):
        answer, user = buscar(user, self.__users)
        return answer, user

# Función para hacer un préstamo a un usuario.
    def prestar_libro_a_usuario(self, book, user):
        answer, book = buscar(book, self.__catalogue)
        if answer:
            while True:
                # Tiempos disponibles para el préstamo.
                type_ = input('1.Regular (2 semanas).\n2.Rápido (2 días).\nSelecciona un tipo (por número):\n')
                if type_.isdigit():
                    type_ = int(type_)
                    self.__catalogue[book].disponibilidad(False)
                    self.__users[user].agregar_renta(book, type_)
                    break
                else:
                    print('No es valido.')
                    continue
        else:
            print('No se encontró el libro.')

# Función para regresar un libro en préstamo de parte de un usuario.
    def regresar_libro_usuario(self, book, user):
        answer, book = buscar(book, self.__catalogue)
        if answer:
            self.__catalogue[book].disponibilidad(True)
            self.__users[user].regresar_renta(book)

# Función para prestar un libro a una biblioteca en convenio.
    def prestar_libro_a_biblioteca(self, book, library):
        answer, book = buscar(book, self.__catalogue)
        if answer:
            self.__catalogue[book].disponibilidad(False)
            self.__convenience_library[library].agregar_rentas(book)
        else:
            print('No se encontró el libro.')

# Función para buscar una biblioteca en el catálogo de bibliotecas.
    def buscar_biblioteca(self, library):
        answer, library = buscar(library, self.__convenience_library)
        return answer, library

# Función para agregar una biblioteca en el catálogo.
    def agregar_libreria(self, library_name, library_address):
        self.__convenience_library[library_name] = Library_aux(library_name, library_address)
        return self.__convenience_library[library_name].get_id()

# Función para regresar un libro en préstamo de parte de una biblioteca.
    def regresar_libro_biblioteca(self, book, library):
        answer, book = buscar(book, self.__catalogue)
        if answer:
            self.__catalogue[book].disponibilidad(True)
            self.__convenience_library[library].regresar_rentas(book)
