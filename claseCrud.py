import json
from claseLibro import Libro  # Importa la clase Libro desde el archivo claseLibro.py
from claseValidacion import Validacion  # Importa la clase Validacion desde el archivo claseValidacion.py

# Crea una instancia de la clase Validacion para validar entradas de usuario
validacionInstancia = Validacion()

# Función para cargar datos desde un archivo JSON al inicio del programa
def cargarDatos():
    try:
        with open("stockLibros.json", "r") as archivoJson:
            data = json.load(archivoJson)
            for libroJson in data:
                # Crea instancias de la clase Libro a partir de los datos del archivo JSON
                libro = Libro(libroJson["nombre"], libroJson["apellido"],
                              libroJson["edicion"], libroJson["titulo"], libroJson["isbn"])
    except FileNotFoundError:
        # Si el archivo no existe, se creará una lista vacía.
        pass

# Inicializa la lista de libros al inicio del programa
cargarDatos()

# Clase para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la biblioteca
class Crud:
    def __init__(self, variableTxt='', variableNumero=1):
        self.__variableTxt = variableTxt
        self.__variableNumero = variableNumero

    # Métodos Get
    def getVariableTxt(self):
        return self.__variableTxt

    def getVariableNumero(self):
        return self.__variableNumero

    # Métodos Set
    def setVariableTxt(self, variableTxt):
        self.__variableTxt = variableTxt

    def setVariableNumero(self, variableNumero):
        self.__variableNumero = variableNumero

    # Función para pedir datos de un nuevo libro
    def pedirDatosLibro(self):
        # Utiliza la instancia de Validacion para obtener datos validados
        variableTxt = Validacion('el título')
        titulo = variableTxt.pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        variableTxt.setTexto('nombre del autor')
        nombre = variableTxt.pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        variableTxt.setTexto('apellido del autor')
        apellido = variableTxt.pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        variableTxt.setTexto('edición')
        edicion = variableTxt.pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        while True:
            variableNumero = Validacion('ISBN')
            isbn = variableNumero.pedirNumeroEntero()
            isbn = variableNumero.verNumero(isbn)

            isbnExistente = False
            for libro in Libro.listaLibro:
                if libro.getISBN() == isbn:
                    isbnExistente = True
                    break

            if isbnExistente:
                validacionInstancia.semiEstetico(
                    'Ya existe un libro con ese ISBN. Debe ser otro.')
            else:
                return titulo, nombre, apellido, edicion, isbn

    # Función para guardar los datos de libros en un archivo JSON
    def guardarDatos(self):
        data = []
        for libro in Libro.listaLibro:
            data.append({
                "nombre": libro.getNombre(),
                "apellido": libro.getApellido(),
                "edicion": libro.getEdicion(),
                "titulo": libro.getTitulo(),
                "isbn": libro.getISBN()
            })

        with open("stockLibros.json", "w") as archivoJson:
            # Escribe los datos en el archivo JSON con una sangría de 4 espacios
            json.dump(data, archivoJson, indent=4)

    # Función para crear un nuevo libro
    def crearLibro(self):
        titulo, nombre, apellido, edicion, isbn = self.pedirDatosLibro()

        # Crea una instancia de la clase Libro con los datos proporcionados
        libroNuevo = Libro(nombre, apellido, edicion, titulo, isbn)
        self.guardarDatos()  # Guarda los datos en el archivo JSON
        validacionInstancia.semiEstetico('Libro creado con éxito.')

    # Función para buscar un libro por el número de ISBN
    def buscarLibro(self, pISBN):
        for libro in Libro.listaLibro:
            if libro.getISBN() == pISBN:
                return libro
        return None

    # Función para pedir el número de ISBN y buscar un libro
    def pedirISBNYBuscar(self):
        variableTxt = Validacion('el número de ISBN del libro')
        isbn = variableTxt.pedirNumeroEntero()
        return self.buscarLibro(isbn)

    # Función para mostrar datos de libros (en específico o todos los existentes)
    def mostrarLibros(self):
        print('Desea 1. Buscar libro en específico. 2. Listar todo.')
        variableTxt = Validacion('una opción')
        op = variableTxt.pedirNumeroEntero()
        op = variableTxt.opcionBooleano(op)
        if op:
            libro = self.pedirISBNYBuscar()
            if libro:
                libro.mostrar()
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            else:
                validacionInstancia.semiEstetico('Libro no encontrado.')
        else:
            if len(Libro.listaLibro) == 0:
                validacionInstancia.semiEstetico('No hay libros.')
            else:
                print('Libros:\n')
                for libro in Libro.listaLibro:
                    libro.mostrar()
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

    # Función para eliminar un libro
    def eliminarLibro(self):
        validacionInstancia = Validacion()
        print('Según el ISBN, elimine un libro')
        libro = self.pedirISBNYBuscar()
        if libro:
            Libro.listaLibro.remove(libro)
            validacionInstancia.semiEstetico('Libro eliminado con éxito.')
            self.guardarDatos()  # Guarda los datos actualizados en el archivo JSON
        else:
            validacionInstancia.semiEstetico('Libro no encontrado.')

    # Función para actualizar los datos de un libro
    def actualizarLibro(self):
        print('Según el ISBN, modifique stock de un libro')
        libro = self.pedirISBNYBuscar()
        if libro:
            print('¿Faltan libros? 1. Si 2. No')
            variableNumero = Validacion('una opción')
            op = variableNumero.pedirNumeroEntero()
            op = variableNumero.opcionBooleano(op)
            if op:
                validacionInstancia.semiEstetico('Pedido realizado con éxito.')
            else:
                validacionInstancia.semiEstetico('Stock actualizado.')
            self.guardarDatos()  # Guarda los datos actualizados en el archivo JSON
        else:
            validacionInstancia.semiEstetico('Libro no encontrado.')
