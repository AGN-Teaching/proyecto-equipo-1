from book import Book
from library_prin import Library
import pickle


main_libray = Library()


def guardar_archivo():  # metodo para guardar en un archivo
    libro1 = Book('Angeles caidos', 'Susan Lee', 20, 'España', '2014', 'Oceano', '365')
    libro2 = Book('El Jugador', 'Dostoyevski', 30, 'Madrid', '1980', 'Alianza', '191')
    libro3 = Book('La Campana de Cristal', 'Sylvia Plath', 30, 'Ingleterra', '1963', 'Heinemann', '272')
    libro4 = Book('Del arte de la Guerra', 'Niccoló Maqhiaveli', 50, 'Italalia', '1532', 'Oceano', '44')
    libro5 = Book('Diarios', 'Alejandra Pizarnik', 50, 'Paris', '1961', 'Lumen', '1104')
    libro6 = Book('La Metamorfosis', 'Franz Kafka', 30, 'España', '1915', 'Alianza', '128')
    libro7 = Book('Psicología Obscura', 'Steven Turner', 20, 'Manhatan', '2019', 'Oceano', '206')
    libro8 = Book('Metamorfosis en el Cielo', 'Mathias Malzieu', 50, 'España', '2011', 'Mondadori', '160')
    libro9 = Book('El Guardián entre el Centeno', 'J.D. Salinger', 25, 'Estados Unidos', '1951', 'Little Brown and Company', '234')
    libro10 = Book('El Diario de greg', 'Jeff Kiney', 20, 'Barcelona', '2007', 'Amulet Books', '224')
    diccionario = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]
    with open('Inventory.pickle', 'wb') as archivo:  # creamos un archivo que contendra el como se ve al mostrar
        pickle.dump(diccionario, archivo)
    print('El catalogo se a guardado en {Inventory.pickle}')
    # mostramos que ya se crearon los archivos



