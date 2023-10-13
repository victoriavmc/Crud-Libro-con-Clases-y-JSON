# Importa la clase Autor desde un módulo llamado claseAutor
from claseAutor import Autor

# Define la clase Libro, que hereda de Autor
class Libro(Autor):
    # Lista para almacenar todas las instancias de libros
    listaLibro = []

    # Constructor de la clase Libro
    def __init__(self, nombre, apellido, edicion, titulo, ISBN):
        # Llama al constructor de la clase base Autor
        super().__init__(nombre, apellido)
        
        # Inicializa atributos específicos de Libro
        self.__edicion = edicion
        self.__titulo = titulo
        self.__ISBN = ISBN

        # Agrega la instancia actual a la lista de libros
        Libro.listaLibro.append(self)

    # Métodos Get
    def getEdicion(self):
        return self.__edicion

    def getTitulo(self):
        return self.__titulo

    def getISBN(self):
        return self.__ISBN

    # Métodos Set
    def setEdicion(self, edicion):
        self.__edicion = edicion

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setISBN(self, ISBN):
        self.__ISBN = ISBN

    # Método de Polimorfismo
    def mostrar(self):
        # Muestra información sobre el autor y el libro
        print('El Título es:', self.getTitulo())
        super().mostrar()  # Llama al método mostrar de la clase Autor (clase base)
        print('La Edición:', self.getEdicion())
        print('Código ISBN:', self.getISBN())
