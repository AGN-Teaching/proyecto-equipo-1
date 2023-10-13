from Usuarios import Usuario_Bi
from library_prin import Library
import pickle
import os
import time



def isdigit(argumento):
    while True:
        if argumento.isdigit():
            argumento = int(argumento)
            break
        else:

            print('No es valido.')
            continue
    return argumento


def mostrar_menu():
    while True:
        os.system('cls')
        print("MENU:".capitalize())
        print("1. Agregar nuevo usuario")
        print("2. Agregar nueva biblioteca en convenio")
        print("3. Dar de alta un libro en el catálogo")
        print("4. Dar de baja un libro del catálogo")
        print("5. Registrar préstamo de un ejemplar a un usuario")
        print("6. Registrar préstamo de un ejemplar a una biblioteca en convenio")
        print("7. Recibir libro devuelto de un usuario")
        print("8. Recibir libro devuelto de una biblioteca en convenio")
        print("9. Consultar catálogo")
        print("0. Salir")
        anser_ = input("Seleccione una opción: ")
        if anser_.isdigit() and 0 <= int(anser_) <= 9:
            break
        else:
            print('No es una opcion valida.')
            continue
    return anser_


if __name__ == "__main__":
    main_libray = Library()
    user_prin = Usuario_Bi('', '', '', '')
    with open('Inventory.pickle', 'rb') as archivo:  # abrimos el archivo donde esta guardado el como se ve el catalogo
        catalogo = pickle.load(archivo)  # cargamos la informacion a la variable
    for libros in catalogo:  # ciclo para anexar datos
        main_libray.anexar_simple(libros)  # agregamos libros

    while True:
        option = mostrar_menu()
        if option == "1":
            os.system('cls')
            user_name, user_last_name, user_edge, user_adress = user_prin.preguntas_agre()
            user_id = main_libray.agregar_usuario(user_name, user_last_name, user_edge, user_adress)
            print(f"Usuario {user_name} agregado correctamente.")
            print('Tu ID es: ' + user_id)
            time.sleep(3)

        elif option == "2":
            os.system('cls')
            print('Agregar Libreria'.capitalize())
            library_name = input("Ingrese el nombre de la biblioteca en convenio: \n")
            library_adress = input('Ingresa la direccion de la biblioteca: \n')
            library_id = main_libray.agregar_libreria(library_name, library_adress)
            print(f"Biblioteca en convenio {library_name} agregada correctamente.")
            print('Tu ID es: ' + library_id)
            time.sleep(3)

        elif option == "3":
            os.system('cls')
            print('Agregar libro al catalogo'.capitalize())
            book_name = input('Ingresa el nombre del libro:\n')
            book_author = input('Ingresa el autor del libro:\n')
            book_available = input('Ingresa el numero de copias disponibles:\n')
            book_available = isdigit(book_available)
            book_place = input('Ingresa el lugar de edicion del libro:\n')
            book_edithorial = input('Ingresa el nombre de la editorial del libro:\n')
            book_year = input('Ingresa el año de edicion del libro:\n')
            book_year = isdigit(book_year)
            book_pages = input('Ingresa el No. de paginas del libro:\n')
            book_pages = isdigit(book_pages)
            main_libray.agregar_libro(book_name, book_author, book_available, book_place, book_year, book_edithorial,
                                      book_pages)
            print(f"El libro {book_name} agregado correctamente.")
            pass

        elif option == "4":
            os.system('cls')
            print('Dar de baja libro'.capitalize())
            book_name_id = input('Ingresa el nombre del libro o el ID:\n')
            anser, book_name = main_libray.buscar_libro(book_name_id)
            main_libray.eliminar_libro(book_name, anser)
            pass

        elif option == "5":
            os.system('cls')
            print('Prestamo de Libro'.capitalize())
            user = input('Ingresa tu nombre o tu ID:\n')
            anser, user = main_libray.buscar_usuario(user)
            if anser:
                book = input('Ingresa el nombre del libro a rentar o su ID:\n')
                main_libray.prestar_libro_a_usuario(book, user)
                time.sleep(3)
            else:
                print('No se encontro usuario.')

        elif option == "6":
            os.system('cls')
            print('Prestamo de Libro'.capitalize())
            library = input('Ingresa el nombre de la biblioteca o su ID:\n')
            anser, library = main_libray.buscar_biblioteca(library)
            if anser:
                book = input('Ingresa el nombre del libro a rentar o su ID:\n')
                main_libray.prestar_libro_a_biblioteca(book, library)
                time.sleep(3)
            else:
                print('No se encontro usuario.')

        elif option == "7":
            os.system('cls')
            print('Retorno de Libro'.capitalize())
            user = input('Ingresa tu nombre o tu ID:\n')
            anser, user = main_libray.buscar_usuario(user)
            if anser:
                book = input('Ingresa el nombre del libro a devolver o su ID:\n')
                main_libray.regresar_libro_usuario(book, user)
                time.sleep(3)
            else:
                print('No se encontro usuario.')

        elif option == "8":
            os.system('cls')
            print('Retorno de Libro'.capitalize())
            library = input('Ingresa el nombre de la biblioteca o su ID:\n')
            anser, library = main_libray.buscar_biblioteca(library)
            if anser:
                book = input('Ingresa el nombre del libro a devolver o su ID:\n')
                main_libray.regresar_libro_biblioteca(book, library)
                time.sleep(3)
            else:
                print('No se encontro la biblioteca.')

        elif option == "9":
            os.system('cls')
            print("CATÁLOGO:".capitalize())
            main_libray.get_catalogo()
            time.sleep(8)

        else:
            print("¡Hasta luego!")
            break
