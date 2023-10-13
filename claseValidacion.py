class Validacion:
    def __init__(self, texto=''):
        self.__texto = texto

    # GET: Permite obtener el valor del atributo privado
    def getTexto(self):
        return self.__texto

    # SET: Permite establecer el valor del atributo privado
    def setTexto(self, pTexto):
        self.__texto = pTexto

    # Función para imprimir una línea decorativa
    def estetico(self, pParametro):
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(pParametro)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    # Función para imprimir una línea decorativa después de un texto
    def semiEstetico(self, pParametro):
        print(pParametro)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    # Función para pedir un número entero positivo
    def pedirNumeroEntero(self):
        while True:
            try:
                numero = int(input(f'Ingrese {self.getTexto()}: '))
                if numero >= 1:
                    return numero
                else:
                    self.estetico(
                        'Debe ingresar números enteros positivos. \nIntente nuevamente!')
            except ValueError:
                self.estetico(
                    'Debe ingresar números enteros. \nIntente nuevamente!')

    # Función para pedir una cadena de texto sin caracteres especiales
    def pedirStringMayMas(self):
        while True:
            caracter = input(f'Ingrese {self.getTexto()}: ')
            if caracter.isalpha() and not any(c in ',<.>/?:;[{]}=+-_)(*&^%$#@!`~¨¡¿?-/`1~|' for c in caracter):
                return caracter.title()
            else:
                self.estetico(
                    'Debe ingresar caracteres válidos. \nIntente nuevamente!')

    # Función para hacer que la opción 1 sea Verdadero y la opción 2 sea Falso
    def opcionBooleano(self, pOpcion):
        while pOpcion not in (1, 2):
            self.estetico(
                'No cumples con los requisitos. \nIntente nuevamente!')
            pOpcion = self.pedirNumeroEntero()
        return pOpcion == 1

    # Función para verificar que el número de ISBN tiene 13 dígitos
    def verNumero(self, pNumero):
        while len(str(pNumero)) != 13 or not str(pNumero).isdigit():
            self.estetico(
                'No cumples con los requisitos. Ingrese un número correspondiente a 13 dígitos.')
            pNumero = self.pedirNumeroEntero()
        return pNumero
