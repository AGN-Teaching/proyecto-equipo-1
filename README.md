[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12200178)
# Proyecto

<p align="center">
<img src="https://github.com/AGN-Teaching/practica-2-relaciones-entre-clases-abi-sae/assets/125155934/babfcff5-709c-42d6-bd7f-15358aba6147" #vitrinedev/>
</p>

# Universidad Autónoma Metropolitana

# Biblioteca.

Licenciatura: Ingeniería en computación. 

UEA: Programación Orientada a Objetos, (POO).

Equipo 1: 

- Sánchez López Abigail          2223068506
     
- Jacuinde Soria Joshua          2223028913

Profesor: Abel García Najera

<hr>

### Índice.

- [Antecedentes.](#Antecedentes)

- [Análsis del problema.](#Análisis-del-problema)
  
- [Diseño UML.](#Diseño-UML)
  
- [Documentación.](#Documentación)

- [Conlusión.](#Conclusión)




# Antecedentes.
<p align="justify">
Una biblioteca requiere un sistema para administrar los préstamos de libros a sus usuarios y a otras bibliotecas. Este sistema debe permitir ingresar un nuevo usuario, una nueva biblioteca en convenio, dar de alta y de baja libros del catálogo, recibir y regresar libros en préstamos de otras bibliotecas, consultar el catálogo y registrar el préstamo de un ejemplar a un usuario o a una biblioteca.
</p>

<p align="justify">
Cada libro tiene asignado un identificador único y existen en la biblioteca cierto número de ejemplares por cada libro. Hay dos tipos de préstamo a usuarios de acuerdo con el periodo de préstamo: préstamo regular, que es por dos semanas, y préstamo rápido, que es por dos días. Los préstamos a otras bibliotecas en convenio son por dos meses.
Un usuario, además de su nombre, tiene un identificador único. Cada usuario puede tener hasta 5 ejemplares en préstamo simultáneamente.
</p>


# Análisis del problema.

Este problema involucra múltiples entidades (usuarios, bibliotecas, libros) con atributos y comportamientos específicos. A continuación, se muestra el análisis del problema: 

#### Entidades Principales:

1. **Libro**:
   - Atributos: Título, autor, ejemplares disponibles, lugar de edición, año de edición, editorial, número de páginas, identificador único.
   - Comportamientos: 
     - Permitir la consulta de información sobre el libro.
     - Actualizar el número de ejemplares disponibles cuando se realiza un préstamo o devolución.

2. **Usuario**:
   - Atributos: Nombre, apellido, edad, dirección, identificador único, lista de libros en préstamo.
   - Comportamientos:
     - Realizar préstamos de libros.
     - Devolver libros en préstamo.
     - Consultar la lista de libros en préstamo.

3. **Biblioteca**:
   - Atributos: Nombre, dirección, identificador único, lista de libros en préstamo.
   - Comportamientos:
     - Realizar préstamos de libros.
     - Devolver libros en préstamo.
     - Consultar la lista de libros en préstamo.

#### Funcionalidades:

- **Agregar nuevo usuario**: Se debe permitir la creación de nuevos usuarios con información como nombre, apellido, edad y dirección. Cada usuario debe tener un identificador único.

- **Agregar nueva biblioteca en convenio**: Se debe permitir la creación de nuevas bibliotecas en convenio con información como nombre y dirección. Cada biblioteca en convenio debe tener un identificador único.

- **Dar de alta un libro en el catálogo**: Se deben poder agregar nuevos libros al catálogo de la biblioteca, especificando su título, autor, cantidad de ejemplares disponibles, lugar de edición, año de edición, editorial y número de páginas. Cada libro debe tener un identificador único.

- **Dar de baja un libro del catálogo**: Se debe permitir eliminar libros del catálogo cuando sea necesario.

- **Registrar préstamo de un ejemplar a un usuario**: Se debe permitir que los usuarios soliciten préstamos de libros. Los préstamos pueden ser regulares (por dos semanas) o rápidos (por dos días). Se debe llevar un registro de los libros prestados a cada usuario.

- **Registrar préstamo de un ejemplar a una biblioteca en convenio**: Se debe permitir que las bibliotecas en convenio soliciten préstamos de libros. Los préstamos a otras bibliotecas son por dos meses.

- **Recibir libro devuelto de un usuario**: Se debe permitir que los usuarios devuelvan los libros en préstamo, actualizando la disponibilidad de ejemplares.

- **Recibir libro devuelto de una biblioteca en convenio**: Se debe permitir que las bibliotecas en convenio devuelvan los libros en préstamo, actualizando la disponibilidad de ejemplares.

- **Consultar catálogo**: Se debe proporcionar una función para consultar el catálogo de libros disponibles en la biblioteca.

#### Consideraciones Adicionales:

- Control de disponibilidad: Es importante llevar un registro preciso del número de ejemplares disponibles para cada libro y aplicar reglas de disponibilidad al registrar préstamos.

- Límite de préstamos por usuario: Los usuarios no pueden tener más de 5 libros en préstamo simultáneamente.

- Identificadores únicos: Cada libro, usuario y biblioteca debe tener un identificador único para facilitar la gestión y búsqueda.

- Interfaz de usuario: Para interactuar con este sistema, se puede desarrollar una interfaz de usuario (IU) que presente las opciones mencionadas y permita a los usuarios y bibliotecarios realizar las operaciones de manera intuitiva.

En resumen, este problema se puede abordar eficazmente mediante programación orientada a objetos, creando clases para representar las entidades mencionadas y métodos para implementar las funcionalidades requeridas. La POO facilita la organización y reutilización del código, lo que lo hace más mantenible y escalable.


# Diseño UML.

<p align="center">
<img src="https://github.com/AGN-Teaching/proyecto-equipo-1/assets/125155934/429ed5b1-de8c-4368-8167-195344171b32"/>
</p>



# Documentación.

### **Book:**
<p align="justify">
La clase 'Book' se utiliza para crear objetos que representan libros en el catálogo de la biblioteca. Cada libro tiene atributos que almacenan su información, y la clase proporciona métodos para obtener y actualizar esta información, así como para generar una representación detallada del libro. Se divide en lo siguiente:
   
   - 'import random': En esta sección, se importa el módulo *'random'* que se utiliza posteriormente para generar identificadores únicos para cada libro.
   
   - Constructor('_ _ init _ _'): Se encarga de inicializar los atributos de un libro cuando se crea una instancia de la clase. Eestos atributos incluyen el título, autor, ejemplares disponible,s lugar de edición, año de edición, editorial, número de páginas y un identificador único (ID).
   
   - Métodos:
        - 'get_title': Permite obtener el título del libro.
        - 'get_ejemplares': Permite obtener el número de ejemplares disponibles del libro.
        - 'disponibilidad': Se utiliza para actualizar el número de ejemplares disponibles de un libro cuando se presta o devuelve. Dependiendo del valor del argumento *'answer'*, se incrementa o decrementa la cantidad de ejemplares dispoibles y se muestra un mensaje apropiado.
        - 'cadena': Devuelve un diccionario que contiene información detallada sobre el libro, como su 'ID', autor, lugar de edición, editorial, año de edición, número de páginas y ejemplares disponibles. Se utiliza para obtener una representación en cadena de texto de un libro con todos sus detalles.
</p>

<hr>

### **Usuarios:**
<p align="justify">
 La clase 'Usuario_Bi' funciona para representar y gestionar los libros de una biblioteca. Proporciona una estructura para almacenar información sobre los usuarios, como su nombre, apellido, edad, dirección, identificador (ID) y los libros que han rentado.
   - Constructor('_ _ init _ _'): Inicializa los atributos del usuario, como su nombre, apellido, edad, dirección e identificador (ID).

   - Métodos y atributos:
        - 'get_nombre', 'get_apellido' y 'get_id': son métodos para obtener el  nombre, apellido e identificador del usuario respectivamente.
        - 'get_rentas': devuelve una cadena que contiene los títulos de los libros que el usario ha rentado.
        - 'agregar_renta': se utiliza para agregar un libro a la lista de libros rentados por el usario. Toma el nombre del libro y un tipo (1. Para libros prestados por bibliotecas y 2. para libros prestador por otros usuarios). Este calcula las fechas de inicio y devolución y almacena esta información.
        - 'mostrar_datos_usuario': muestra información sobre el usuario, incluyendo su nombre, apellido, edad, dirección. identificador y libros que ha rentado.
        - 'preguntas_agre': solicita la información necesaria para agregar un usario, como nombre, apellido, edad y dirección. Luego, devuelve esta información como una tupla.

Permiten administrar a los usuarios de la biblioteca, así como realizar un seguimiento de los libros que han rentado y sus fechas de devolución.
</p>

<hr>

### **library_aux:**
<p align="justify">
 Se utiiliza para representar bibliotecas en convenio y realizar operaciones relacionadas con ellas.
   
   - Constructor('_ _ init _ _'): Cuando creamos la instancia 'Library_aux' se tiene que proporcionar un nombre y una dirección. El constructor inicializa los atributos de la biblioteca, como el nombre(en mayúsculas), la dirección, un identificador (ID) generado automáticamente y un diccionario para rastrear los libros que la biblioteca en convenio(auxiliar) ha rentado.
   - Métodos:
        - 'get_nombre' y 'get_id': permiten obtener el nombre y el identificador de la biblioteca en convenio, respectivamente.
        - 'get_rentas': devuelve una cadena que contiene los títulos de los libros que la biblioteca auxiliar ha rentado. Los títulos se obtienen del diccionario '__rentados'.
        - 'regresar_rentas': elimina un libro de la lista de libros rentados por la biblioteca en convenio. Se tiene que proporcionar el nombre del libro que se devolverá.
        - 'agregar_rentas': se utiliza para agregar un libro rentado a la biblioteca auxiliar. Se tiene que proporcionar el nombre del libro como argumento, y se registra la fecha actual y una fecha de devolución estimada (dos meses después) en el diccionario '__rentados'.
        - 'mostrar_datos_biblioteca': Genera una cadena que contiene información sobre la biblioteca en convenio, incluyendo su nombre, dirección, identificador único y los títulos de los libros que ha rentado. Esta cadena se imprime en la consola.

   En si, esta clase permite gestionar y llevar un registro de las operaciones de préstamo de libros realizadas por bibliotecas en convenio.
</p>

<hr>

### **library_prin:**
<p align="justify">
   Este representa una biblioteca y tiene métodos para gestionar su catálogo de libros, usuarios y préstamos, así como 'library_aux' para representar las bibliotecas en convenio y la función 'buscar' para buscar elementos en una colección.
   
   - Importación de módulos: Se importan las clases 'Book' y 'Ususario_Bi' de otros módulos, para el uso de esas clases en 'library'.

   - Función 'buscar': Esta función toma como argumento un elemento a buscar (*'argument'*) y una colección donde buscarlo (*'where'*). Utiliza un bucle para buscar el elemento en la colección y devuelve 'True' si lo encuentra, junto con e elemento encontrado (actualizado en caso de busqueda por ID). Si no lo encuentra, devuelve 'Falso'.

   - Métodos:
        - Constructor ('_ _ init _ _'): Inicializa tres diccionarios vacíos.
        - '_ _ catalogue': Para el catálogo de libros, '_ _users' para los usuarios y '_ _ convenience_library' para las bibliotecas en convenio.
        - 'buscar_libro': Busca un libro en el catálogo de la biblioteca utilizando la función 'buscar'.
        - 'agregar_libro': Agrega un nuevo libro al catálogo de la biblioteca.
        - 'eliminar_libro': Elimina un libro del catálogo de la biblioteca.
        - 'get_catalogo': Muestra el catálogo de libros.
        - 'agregar_usuario': Agrega un nuevo usuario al catáogo de usuarios.
        - 'buscar_usuarios': Busca un usuario en el catálogo de usuarios.
        - 'prestar_libro_a_usuario': Realiza un préstamo de un libro a un usuario.
        - 'regresar_libro_usuario': Registra la devolución de un libro por parte de un usuario.
        - 'prestar_libro_a_biblioteca': Relaiza un préstamos de un libro a una biblioteca en convenio.
        - 'buscar_biblioteca': Busca una biblioteca en el catálogo  de bibliotecas en convenio.
        - 'agregar_libreria': Agrega una biblioteca en convenio al catálogo de bibliotecas.
        - 'regresar_libro_biblioteca': Registra la devolución de un libro por parte de una biblioteca en convenio.
        - 'def anexar_simple(self, objeto): El método toma dos argumentos: self, que se refiere a la instancia de la clase en sí, y objeto, que es el objeto que se va a añadir al catálogo.

   En resumen, es una implementación básica de una biblioteca que permite agregar y eliminar libros, gestionar usuarios y realizar préstamos tanto a usuarios como a bibliotecas en convenio.
</p>

<hr>
### **construir_Archivo:**

1. *Importación de módulos y clases:*
   - Se importan las clases *Book* y *Library* desde los módulos correspondientes.
   - El módulo *pickle* también se importa para facilitar la serialización y deserialización de objetos.

2. **Instancia de la clase Library:**
   - Se crea una instancia de la clase *Library* y se asigna a la variable *main_library*.

3. *Función guardar_archivo():*
   - Esta función está diseñada para almacenar una lista de libros en un archivo.
   - Dentro de la función, se crean diez instancias de la clase *Book* con información específica.
   - Todos los objetos *Book* se almacenan en una lista llamada *diccionario*.
   - Se utiliza el módulo *pickle* para serializar la lista *diccionario* y escribirla en un archivo llamado 'Inventory.pickle' en modo de escritura binaria ('wb').
   - Un mensaje de confirmación se imprime para indicar que el catálogo se ha guardado en 'Inventory.pickle'.


En general,  se utiliza para demostrar cómo se pueden crear objetos de la clase *Book*, almacenarlos en una lista y luego guardar la lista en un archivo utilizando el módulo **pickle**.

<hr>
### **main:**


Este módulo se encarga de crear un menú de interfaz para que el usuario interactúe con el sistema de gestión de biblioteca.

Importación de módulos:

Se importan las clases *Usuario_Bi* y *Library* desde los módulos correspondientes (*Usuarios* y *Library*, respectivamente) para su uso en el programa principal.

Función **isdigit**:

Esta función verifica si una cadena contiene solo dígitos y la convierte en un entero. Se utiliza para garantizar la entrada de datos válidos.

Inicialización de la biblioteca y el usuario principal:

En esta sección, se crea una instancia de la clase *Library* llamada *main_library* para representar la biblioteca principal y otra instancia de la clase *Usuario_Bi* llamada *user_prin* para representar al usuario principal.

Bucle principal:

El programa entra en un bucle infinito (*while True*) que muestra el menú principal y espera la selección del usuario. Dependiendo de la opción elegida, se ejecutan distintos bloques de código que realizan acciones como agregar usuarios, bibliotecas en convenio, libros al catálogo, registrar préstamos, devoluciones y consultas en el catálogo, además de la opción para salir.

Cada opción del menú está acompañada de un bloque de código que realiza la acción correspondiente, como agregar un nuevo usuario, agregar una biblioteca en convenio, etc. Para las acciones de préstamo y devolución de libros, se solicita información adicional, como el nombre del usuario o el nombre del libro. El programa busca y valida esta información utilizando métodos de las clases importadas. El bucle continuará ejecutándose hasta que el usuario seleccione la opción "0", momento en el cual mostrará un mensaje de despedida y finalizará el programa.

En si, este programa permite gestionar una biblioteca a través de un menú de opciones, donde se pueden realizar diversas operaciones relacionadas con usuarios, bibliotecas en convenio, libros y préstamos. Además, al inicio del código se establece el cargar información de un archivo de catálogo preexistente y agregarla al catálogo principal de la biblioteca.
     
     


# Conclusión

### Abigail Sánchez:

<p align="justify">
El diseño basado en la programación orientada a objetos (POO) ha demostrado ser altamente beneficioso en la implementación del sistema de gestión de la biblioteca. Al modelar entidades clave, como libros, usuarios y bibliotecas, como clases con atributos y métodos específicos, se ha logrado una organización clara y modular del código. Esta estructura modular facilita significativamente el mantenimiento y la comprensión del código a medida que el proyecto continúa evolucionando.

La reutilización de código, lograda a través de la definición y creación de múltiples instancias de clases, ha sido esencial para la gestión eficiente de libros, usuarios y bibliotecas en el sistema. Al utilizar estas clases de manera efectiva, se ha mejorado la eficiencia en la gestión de datos y operaciones, lo que ha permitido una mayor consistencia en todo el sistema.

Además, la implementación de una validación básica de entradas ha fortalecido la integridad del sistema al prevenir errores comunes, como ingresos de datos incorrectos o inválidos. Esta validación garantiza que la información ingresada por los usuarios esté en el formato y rango esperados, lo que contribuye a la fiabilidad y estabilidad general del sistema de gestión de la biblioteca.

En resumen, la aplicación efectiva de los principios de la programación orientada a objetos ha sido fundamental para el desarrollo de un sistema de gestión de biblioteca completo y altamente funcional. La flexibilidad, la escalabilidad y la claridad estructural han garantizado un sistema sólido y adaptable, capaz de satisfacer las necesidades cambiantes de la biblioteca y de sus usuarios a lo largo del tiempo.
</p> 



### Joshua Soria:
<p align="justify">
Durante el proceso de desarrollo del sistema de administración de préstamos de libros para la biblioteca, la aplicación de los conceptos fundamentales de la programación orientada a objetos (POO) ha sido crucial para la estructura y funcionalidad del sistema. La creación de clases representativas, como Libro, Usuario y Biblioteca, con sus atributos y comportamientos específicos, ha sentado las bases para una implementación eficiente.

La utilización de la POO ha permitido la implementación de funcionalidades esenciales dentro del sistema, incluyendo la capacidad de agregar y gestionar usuarios, bibliotecas, así como el catálogo de libros. La flexibilidad proporcionada por la POO ha sido fundamental para permitir la escalabilidad y adaptabilidad del sistema a medida que las necesidades y requisitos de la biblioteca evolucionan con el tiempo.

Además, ha permitido una clara separación de preocupaciones en el sistema, lo que ha facilitado la comprensión de cada componente individual y su función en el contexto general del sistema de gestión de la biblioteca. Esta separación ha mejorado la mantenibilidad del sistema y la capacidad de realizar actualizaciones y modificaciones de manera eficiente.

En resumen, la adopción de principios de POO ha proporcionado una base sólida para el desarrollo de un sistema de gestión de biblioteca, al promover una organización clara del código, una reutilización efectiva de recursos y una validación precisa de entradas.

</p>
