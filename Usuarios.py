import datetime


# La clase 'Usuario_Bi' para representar a los usuarios de la biblioteca.
class Usuario_Bi:
    def __init__(self, nombre, apellido, edad, direccion):
        self.__nombre = nombre.upper()  # Almacena el nombre del usuario en mayúsculas.
        self.__apellido = apellido.upper()  # Almacena el apellido del usuario en mayúsculas.
        self.__edad = edad  # Almacena la edad del usuario.
        self.__direccion = direccion
        self.__identificador = self.__nombre[:2] + self.__apellido[:2] + str(self.__edad)
        self.__rentados = {}  # Diccionario para almacenar los libros rentados (o préstamos) por el usuario.

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_id(self):
        return self.__identificador

    def get_rentas(self):
        titulos = []
        for keys in self.__rentados:
            titulos.append(keys)
        return ','.join(titulos)  # Devuelve los títulos rentados como una cadena.

    def agregar_renta(self, nombre, tipo):
        fecha_actual = datetime.date.today()
        if len(self.__rentados) <= 5:  # Evalúa si tiene 5 libros rentados o menos.
            if tipo == 1:
                print('Tienes dos semanas para devolverlo.\n')
                self.__rentados[nombre] = ('Rentado: ' + str(fecha_actual), 'Devolver: ' +
                                           str(fecha_actual + datetime.timedelta(weeks=2)))
            else:
                print('Tienes dos días para devolverlo.')
                self.__rentados[nombre] = (fecha_actual, fecha_actual + datetime.timedelta(days=2))
        else:
            print('Ya tiene 5 rentas, debe regresar alguna.'.capitalize())

    # Elimina un libro de la lista de libros rentados.
    def regresar_renta(self, nombre):
        self.__rentados.pop(nombre)

    def mostrar_datos_usuario(self):
        titulos = []
        for keys in self.__rentados:
            titulos.append(keys)
        cadena = (self.__nombre + ' ' + self.__apellido + '\n' + 'Edad: ' + str(self.__edad) + '\n' + 'Dirección: ' +
                  self.__direccion + '\n' + 'ID: ' + self.__identificador + '\n' + 'Libros rentados:'
                  + ','.join(titulos))  # Genera una cadena con información sobre usuario y sus libros rentados.
        print(cadena)

    # Datos que se requieren para agregar un usuario.
    def preguntas_agre(self):
        print('Agregar Usuario.'.capitalize())
        user_name = input("Ingrese el nombre del usuario: \n")
        user_last_name = input("Ingrese el apellido del usuario: \n")
        while True:
            user_edge = input("Ingrese la edad del usuario: \n")
            if user_edge.isdigit():
                break
            else:
                continue  # Solicita información sobre el usuario y la devuelve.
        user_address = input("Ingrese la dirección del usuario: \n")
        return user_name, user_last_name, user_edge, user_address  # Devuelve la información ingresada por el usuario.
