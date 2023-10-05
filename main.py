from Usuarios import Usuario_Bi  # Importamos la clase 'Usuario_Bi' del módulo 'Usuarios'.
from library_prin import Library  # Importamos la clase 'Library' del módulo 'Library_prin'
import os
import time


# Función para validar si una cadena contiene solo dígitos y convertirla a entero.
def isdigit(argumento):
    while True:
        if argumento.isdigit():
            argumento = int(argumento)
            break
        else:

            print('No es valido.')
            continue
    return argumento

# Función para mostrar el menú principal y obtener la opción del usuario.
def mostrar_menu():
    while True:
        os.system('cls')
        print("MENU:".capitalize())
        print("1. Agregar nuevo usuario.")
        print("2. Agregar nueva biblioteca en convenio.")
        print("3. Dar de alta un libro en el catálogo.")
        print("4. Dar de baja un libro del catálogo.")
        print("5. Registrar préstamo de un ejemplar a un usuario.")
        print("6. Registrar préstamo de un ejemplar a una biblioteca en convenio.")
        print("7. Recibir libro devuelto de un usuario.")
        print("8. Recibir libro devuelto de una biblioteca en convenio.")
        print("9. Consultar catálogo.")
        print("0. Salir.")
        answer_ = input("Seleccione una opción: ")
        if answer_.isdigit() and 0 <= int(answer_) <= 9:
            break
        else:
            print('No es una opción valida.')
            continue
    return answer_

# Inicialización de la biblioteca y usuario principal.
if __name__ == "__main__":
    main_libray = Library()
    user_prin = Usuario_Bi('', '', '', '')
    main_libray.agregar_libro('Angeles caídos', 'Susan Lee', 20, 'España', '2014', 'Océano', '365')
    main_libray.agregar_usuario('Joshua', 'Soria', 23, '16 de Diciembre')
    # main_libray.agregar_libreria('Vasconcelos', 'Eje 1 Norte, Buenavista')

    while True:
        option = mostrar_menu()
        # Bloque para agregar un nuevo usuario.
        if option == "1":
            os.system('cls')
            user_name, user_last_name, user_edge, user_address = user_prin.preguntas_agre()
            user_id = main_libray.agregar_usuario(user_name, user_last_name, user_edge, user_address)
            print(f"Usuario {user_name} agregado correctamente.")
            print('Tu ID es: ' + user_id)
            time.sleep(3)

        # Bloque para agregar una nueva biblioteca en convenio.
        elif option == "2":
            os.system('cls')
            print('Agregar Libreria.'.capitalize())
            library_name = input("Ingrese el nombre de la biblioteca en convenio: \n")
            library_address = input('Ingresa la dirección de la biblioteca: \n')
            library_id = main_libray.agregar_libreria(library_name, library_address)
            print(f"Biblioteca en convenio {library_name} agregada correctamente.")
            print('Tu ID es: ' + library_id)
            time.sleep(3)

        # Bloque para agregar un libro al catálogo.
        elif option == "3":
            os.system('cls')
            print('Agregar libro al catálogo.'.capitalize())
            book_name = input('Ingresa el nombre del libro:\n')
            book_author = input('Ingresa el autor del libro:\n')
            book_available = input('Ingresa el número de copias disponibles:\n')
            book_available = isdigit(book_available)
            book_place = input('Ingresa el lugar de edición del libro:\n')
            book_editorial = input('Ingresa el nombre de la editorial del libro:\n')
            book_year = input('Ingresa el año de edición del libro:\n')
            book_year = isdigit(book_year)
            book_pages = input('Ingresa el No. de páginas del libro:\n')
            book_pages = isdigit(book_pages)
            main_libray.agregar_libro(book_name, book_author, book_available, book_place, book_year, book_editorial,
                                      book_pages)
            print(f"El libro {book_name} agregado correctamente.")
            pass

        # Bloque para dar de baja un libro del catálogo.
        elif option == "4":
            os.system('cls')
            print('Dar de baja un libro.'.capitalize())
            book_name_id = input('Ingresa el nombre del libro o el ID:\n')
            answer, book_name = main_libray.buscar_libro(book_name_id)
            main_libray.eliminar_libro(book_name, answer)
            pass

        # Bloque para registrar el préstamo de un libro a un usuario.
        elif option == "5":
            os.system('cls')
            print('Préstamo de libro.'.capitalize())
            user = input('Ingresa tu nombre o tu ID:\n')
            answer, user = main_libray.buscar_usuario(user)
            if answer:
                book = input('Ingresa el nombre del libro a rentar o su ID:\n')
                main_libray.prestar_libro_a_usuario(book, user)
                time.sleep(3)
            else:
                print('No se encontró usuario.')

        # Bloque para registrar el préstamo de un libro a una biblioteca en convenio.
        elif option == "6":
            os.system('cls')
            print('Préstamo de libro'.capitalize())
            library = input('Ingresa el nombre de la biblioteca o su ID:\n')
            answer, library = main_libray.buscar_biblioteca(library)
            if answer:
                book = input('Ingresa el nombre del libro a rentar o su ID:\n')
                main_libray.prestar_libro_a_biblioteca(book, library)
                time.sleep(3)
            else:
                print('No se encontró usuario.')

        # Bloque para recibir un libro devuelto de un usuario.
        elif option == "7":
            os.system('cls')
            print('Retorno de libro.'.capitalize())
            user = input('Ingresa tu nombre o tu ID:\n')
            answer, user = main_libray.buscar_usuario(user)
            if answer:
                book = input('Ingresa el nombre del libro a devolver o su ID:\n')
                main_libray.regresar_libro_usuario(book, user)
                time.sleep(3)
            else:
                print('No se encontró usuario.')

        # Bloque para recibir un libro devuelto de una biblioteca en convenio.
        elif option == "8":
            os.system('cls')
            print('Retorno de Libro.'.capitalize())
            library = input('Ingresa el nombre de la biblioteca o su ID:\n')
            answer, library = main_libray.buscar_biblioteca(library)
            if answer:
                book = input('Ingresa el nombre del libro a devolver o su ID:\n')
                main_libray.regresar_libro_biblioteca(book, library)
                time.sleep(3)
            else:
                print('No se encontró la biblioteca.')

        # Bloque para consultar el catálogo.
        elif option == "9":
            os.system('cls')
            print("CATÁLOGO:".capitalize())
            main_libray.get_catalogo()
            time.sleep(8)

        else:
            print("¡Hasta luego! :)")
            break
