class Autor:
    def __init__(self, nombre='', apellido=''):
        # Constructor de la clase Autor
        self.__nombre = nombre  # Inicializa el atributo privado nombre
        self.__apellido = apellido  # Inicializa el atributo privado apellido

    # Métodos Get
    def getNombre(self):
        # Devuelve el valor del atributo privado nombre
        return self.__nombre

    def getApellido(self):
        # Devuelve el valor del atributo privado apellido
        return self.__apellido

    # Métodos Set
    def setNombre(self, nombre):
        # Establece el valor del atributo privado nombre
        self.__nombre = nombre

    def setApellido(self, apellido):
        # Establece el valor del atributo privado apellido
        self.__apellido = apellido

    # Método de Polimorfismo
    def mostrar(self):
        # Muestra el nombre y el apellido del autor
        print(f'El Autor es: {self.getNombre()} {self.getApellido()}.')
