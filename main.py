from claseCrud import Crud  # Importa la clase Crud desde el archivo claseCrud.py
from claseLibro import Libro  # Importa la clase Libro desde el archivo claseLibro.py
# Importa la clase Validacion desde el archivo claseValidacion.py
from claseValidacion import Validacion

# Crea una instancia de la clase Crud para gestionar las operaciones CRUD en la biblioteca
crud = Crud()

print(' \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
    print('1. Crear libro')
    print('2. Leer libro(s)')
    print('3. Actualizar libro')
    print('4. Eliminar libro')
    print('5. Salir')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n')

    texto1 = Validacion('una opción')
    op = texto1.pedirNumeroEntero()

    if op == 1:
        crud.crearLibro()  # Llama a la función para crear un libro
    elif op == 2:
        crud.mostrarLibros()  # Llama a la función para leer libros
    elif op == 3:
        crud.actualizarLibro()  # Llama a la función para actualizar un libro
    elif op == 4:
        crud.eliminarLibro()  # Llama a la función para eliminar un libro
    elif op == 5:
        texto1.semiEstetico('''Profesor: 
            Lic. Plazas, Ricardo Gastón      
    Estudiante:
            Maidana Corti, Victoria Valentina ''')  # Imprime información del estudiante
        break
    else:
        texto1.semiEstetico('Opción no válida. Intente de nuevo.')
