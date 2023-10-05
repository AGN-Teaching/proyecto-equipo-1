[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12200178)
# Proyecto

![uamcua](https://github.com/AGN-Teaching/practica-2-relaciones-entre-clases-abi-sae/assets/125155934/babfcff5-709c-42d6-bd7f-15358aba6147)

# Universidad Autónoma Metropolitana

# Biblioteca.

Licenciatura: Ingeniería en computación. 

UEA: Programación Orientada a Objetos, (POO).

Equipo 1: 

     Sánchez López Abigail          2223068506
     
     Jacuinde Soria Joshua          2223028913

Profesor: Abel García Najera



# Antecedentes.

Una biblioteca requiere un sistema para administrar los préstamos de libros a sus usuarios y a otras bibliotecas. Este sistema debe permitir ingresar un nuevo usuario, una nueva biblioteca en convenio, dar de alta y de baja libros del catálogo, recibir y regresar libros en préstamos de otras bibliotecas, consultar el catálogo y registrar el préstamo de un ejemplar a un usuario o a una biblioteca.

Cada libro tiene asignado un identificador único y existen en la biblioteca cierto número de ejemplares por cada libro. Hay dos tipos de préstamo a usuarios de acuerdo con el periodo de préstamo: préstamo regular, que es por dos semanas, y préstamo rápido, que es por dos días. Los préstamos a otras bibliotecas en convenio son por dos meses.
Un usuario, además de su nombre, tiene un identificador único. Cada usuario puede tener hasta 5 ejemplares en préstamo simultáneamente.


# Informe

# Diseño UML.

# Documentación.

1. **book:**

    La clase 'Book' se utiliza para crear objetos que representan libros en el catálogo de la biblioteca. Cada libro tiene atributos que almacenan su información, y la clase proporciona métodos para obtener y actualizar esta información, así como para generar una representación detallada del libro. Se divide en lo siguiente:
   
   **a)** 'import random': En esta sección, se importa el módulo *'random'* que se utiliza posteriormente para generar identificadores únicos para cada libro.
   
   **b)** Constructor('__init__'): Se encarga de inicializar los atributos de un libro cuando se crea una instancia de la clase. Eestos atributos incluyen el título, autor, ejemplares disponible,s lugar de edición, año de edición, editorial, número de páginas y un identificador único (ID).
   
   **c)** Métodos:
   - 'get_title': Permite obtener el título del libro.
   - 'get_ejemplares': Permite obtener el número de ejemplares disponibles del libro.
   - 'disponibilidad': Se utiliza para actualizar el número de ejemplares disponibles de un libro cuando se presta o devuelve. Dependiendo del valor del argumento *'answer'*, se incrementa o decrementa la cantidad de ejemplares dispoibles y se muestra un mensaje apropiado.
   - 'cadena': Devuelve un diccionario que contiene información detallada sobre el libro, como su 'ID', autor, lugar de edición, editorial, año de edición, número de páginas y ejemplares disponibles. Se utiliza para obtener una representación en cadena de texto de un libro con todos sus detalles.
     
2. **Usuarios:**

    La clase 'Usuario_Bi' funciona para representar y gestionar los libros de una biblioteca. Proporciona una estructura para almacenar información sobre los usuarios, como su nombre, apellido, edad, dirección, identificador (ID) y los libros que han rentado.
   **a)** Constructor('__init__'): Inicializa los atributos del usuario, como su nombre, apellido, edad, dirección e identificador (ID).

   **b)** Métodos y atributos:
   - 'get_nombre', 'get_apellido' y 'get_id': son métodos para obtener el  nombre, apellido e identificador del usuario respectivamente.
   - 'get_rentas': devuelve una cadena que contiene los títulos de los libros que el usario ha rentado.
   - 'agregar_renta': se utiliza para agregar un libro a la lista de libros rentados por el usario. Toma el nombre del libro y un tipo (1. Para libros prestados por bibliotecas y 2. para libros prestador por otros usuarios). Este calcula las fechas de inicio y devolución y almacena esta información.
   - 'mostrar_datos_usuario': muestra información sobre el usuario, incluyendo su nombre, apellido, edad, dirección. identificador y libros que ha rentado.
   - 'preguntas_agre': solicita la información necesaria para agregar un usario, como nombre, apellido, edad y dirección. Luego, devuelve esta información como una tupla.

    Permiten administrar a los usuarios de la biblioteca, así como realizar un seguimiento de los libros que han rentado y sus fechas de devolución.

3. **library_aux**.

    Se utiiliza para representar bibliotecas en convenio y realizar operaciones relacionadas con ellas.
   
   **a)** Constructor('__init__'): Cuando creamos la instancia 'Library_aux' se tiene que proporcionar un nombre y una dirección. El constructor inicializa los atributos de la biblioteca, como el nombre(en mayúsculas), la dirección, un identificador (ID) generado automáticamente y un diccionario para rastrear los libros que la biblioteca en convenio(auxiliar) ha rentado.
   **b)** Métodos:
   - 'get_nombre' y 'get_id': permiten obtener el nombre y el identificador de la biblioteca en convenio, respectivamente.
   - 'get_rentas': devuelve una cadena que contiene los títulos de los libros que la biblioteca auxiliar ha rentado. Los títulos se obtienen del diccionario '__rentados'.
   - 'regresar_rentas': elimina un libro de la lista de libros rentados por la biblioteca en convenio. Se tiene que proporcionar el nombre del libro que se devolverá.
   - 'agregar_rentas': se utiliza para agregar un libro rentado a la biblioteca auxiliar. Se tiene que proporcionar el nombre del libro como argumento, y se registra la fecha actual y una fecha de devolución estimada (dos meses después) en el diccionario '__rentados'.
   - 'mostrar_datos_biblioteca': Genera una cadena que contiene información sobre la biblioteca en convenio, incluyendo su nombre, dirección, identificador único y los títulos de los libros que ha rentado. Esta cadena se imprime en la consola.

   En si, esta clase permite gestionar y llevar un registro de las operaciones de préstamo de libros realizadas por bibliotecas en convenio.


4. **library_prin**

   Este representa una biblioteca y tiene métodos para gestionar su catálogo de libros, usuarios y préstamos, así como 'library_aux' para representar las bibliotecas en convenio y la función 'buscar' para buscar elementos en una colección.
   
   **a)** Importación de módulos. 
