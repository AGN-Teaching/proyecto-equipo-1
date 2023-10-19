import datetime
import random


# Clase 'Library_aux' para representar a bibliotecas en convenio.
class Library_aux:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre.upper()  # Almacena el nombre de la biblioteca auxiliar en mayúsculas.
        self.__direccion = direccion  # Almacena la dirección de la biblioteca auxiliar.
        self.__identificador = 'BI' + self.__nombre[:2] + str(random.randint(0, 500))  # Crea un identificador único.
        self.__rentados = {}  # Diccionario para almacenar los libros rentados por la biblioteca.

    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__identificador

    def get_rentas(self):
        titulos = []
        for keys in self.__rentados:
            titulos.append(keys)
        return ','.join(titulos)  # Devuelve los títulos de los libros rentados como una cadena.

# Agrega un libro rentado a la biblioteca auxiliar con una fecha de devolución en dos meses.
    def agregar_rentas(self, nombre):
        fecha_actual = datetime.date.today()
        print('Tienes dos meses para devolverlo.\n')
        self.__rentados[nombre] = ('Rentado: ' + str(fecha_actual), 'Devolver: ' + str(fecha_actual +
                                                                                       datetime.timedelta(weeks=8)))

# Eliminar un libro de la lista de libros rentados por la biblioteca auxiliar.
    def regresar_rentas(self, nombre):
        self.__rentados.pop(nombre)

    def mostrar_datos_biblioteca(self):
        titulos = []
        for keys in self.__rentados:
            titulos.append(keys)
        cadena = ('Biblioteca: ' + self.__nombre + '\n' + 'Dirección: ' + self.__direccion + '\n' + 'ID: ' +
                  self.__identificador + '\n' + 'Libros rentados:' + ','.join(titulos))
        print(cadena)
        # Genera una cadena con información sobre la biblioteca auxiliar y los libros rentados por esta.
