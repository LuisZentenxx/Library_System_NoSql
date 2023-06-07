import crudlibro
import crudprestamo

# Functions


def libros():
    print("Gestión de Libros")
    print("=================")
    print("1. Agregar un libro nuevo")
    print("2. Modificar un libro existente")
    print("3. Borrar un libro existente")
    print("4. Consultar un libro")
    print()

    op = input("Selecciona una opción: ")
    print()

    if op == "1":
        crudlibro.agregarlibro()
        print()

    elif op == "2":
        crudlibro.modificarlibro()
        print()

    elif op == "3":
        crudlibro.borrarlibro()

        print()

    elif op == "4":
        crudlibro.consultarlibro()
        print()

    elif op == "0":
        print("Volviendo al Menú Principal...")
        return

    else:
        print("\033[91mOpción inválida. Por favor, seleccione una opción válida.\033[0m")


def prestamos():
    print("Gestión de Préstamos")
    print("====================")
    print("1. Agregar un préstamo nuevo")
    print("2. Modificar un préstamo existente")
    print("3. Borrar un préstamo")
    print("4. Consultar un préstamo")
    print()
    op = input("Selecciona una opción: ")
    if op == "1":
        crudprestamo.agregarprestamo()
        print("")
    elif op == "2":
        crudprestamo.modificarprestamo()
        print("")
    elif op == "3":
        crudprestamo.borrarprestamo()
        print("")
    elif op == "4":
        crudprestamo.consultarpretamo()
        print("")
    elif op == "0":
        print("Volviendo al Menú Principal...")
        return
    else:
        print("\033[91mOpción inválida. Por favor, seleccione una opción válida.\033[0m")


# Main
while True:
    print()
    print("Sistema de Biblioteca")
    print("=====================")
    print("---Menú---")
    print("1. Gestión de Libros")
    print("2. Gestión de Préstamos")
    print("0. Salir del Sistema")
    print()
    op = input("Ingrese una opción: ")
    print()
    if op == "1":
        libros()
    elif op == "2":
        prestamos()
    elif op == "0":
        print("Gracias por usar el sistema de biblioteca")
        break
    else:
        print("\033[91mOpción inválida. Por favor, seleccione una opción válida.\033[0m")
