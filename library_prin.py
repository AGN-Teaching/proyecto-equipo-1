from book import Book
from Usuarios import Usuario_Bi
from library_aux import Library_aux


def buscar(argument, where):
    anser = False
    for titulo in where:
        if titulo == argument:
            argument = titulo
            anser = True
            break
        else:
            anser = False
    if not anser:
        for titulo in where:
            datos = where[titulo].get_id()
            if argument == datos:
                anser = True
                argument = titulo
                break
            else:
                anser = False
    return anser, argument


class Library:
    def __init__(self):
        self.__catalogue = {}
        self.__users = {}
        self.__convenience_library = {}

    def buscar_libro(self, book):
        anser, book = buscar(book, self.__catalogue)
        return anser, book

    def agregar_libro(self, book_name, book_author, book_available, book_place, book_year, book_edithorial, book_pages):
        self.__catalogue[book_name] = Book(book_name, book_author, book_available, book_place, book_year,
                                           book_edithorial, book_pages)

    def anexar_simple(self, objeto):
        nombre_archivo = objeto.get_title()
        self.__catalogue[nombre_archivo] = objeto

    def eliminar_libro(self, book, anser):
        if anser:
            self.__catalogue.pop(book)
            print(book + ' se ah eliminado correctamente.')
        else:
            print(book + ' no se ah podido eliminar')

    def get_catalogo(self):
        for titulos, book in self.__catalogue.items():
            print(titulos)
            atributos = book.cadena()
            for key, valor in atributos.items():
                print(f'{key} {valor}')
            print('')

    def agregar_usuario(self, user_name, user_last_name, user_edge, user_adress):
        self.__users[user_name] = Usuario_Bi(user_name, user_last_name, user_edge, user_adress)
        return self.__users[user_name].get_id()

    def buscar_usuario(self, user):
        anser, user = buscar(user, self.__users)
        return anser, user

    def prestar_libro_a_usuario(self, book, user):
        anser, book = buscar(book, self.__catalogue)
        if anser:
            while True:
                type_ = input('1.Regular (2 semanas)\n2.Rapido (2 dias)\nSelecciona un tipo (por numero):\n')
                if type_.isdigit():
                    type_ = int(type_)
                    self.__catalogue[book].disponibilidad(False)
                    self.__users[user].agregar_renta(book, type_)
                    break
                else:
                    print('No es valido.')
                    continue
        else:
            print('No se encontro libro.')

    def regresar_libro_usuario(self, book, user):
        anser, book = buscar(book, self.__catalogue)
        if anser:
            self.__catalogue[book].disponibilidad(True)
            self.__users[user].regresar_renta(book)

    def prestar_libro_a_biblioteca(self, book, library):
        anser, book = buscar(book, self.__catalogue)
        if anser:
            self.__catalogue[book].disponibilidad(False)
            self.__convenience_library[library].agregar_rentas(book)
        else:
            print('No se encontro libro.')

    def buscar_biblioteca(self, library):
        anser, library = buscar(library, self.__convenience_library)
        return anser, library

    def agregar_libreria(self, library_name, library_adrees):
        self.__convenience_library[library_name] = Library_aux(library_name, library_adrees)
        return self.__convenience_library[library_name].get_id()

    def regresar_libro_biblioteca(self, book, library):
        anser, book = buscar(book, self.__catalogue)
        if anser:
            self.__catalogue[book].disponibilidad(True)
            self.__convenience_library[library].regresar_rentas(book)
