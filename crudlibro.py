import pprint
import pymongo

mongoHost = "localhost"
mongoPort = "27017"
mongoTimeout = 1000
mongoUrl = "mongodb://"+mongoHost+":"+mongoPort+"/"
mongo_db = "bdnr"
mongo_collection_libros = "libros"
client = pymongo.MongoClient(mongoUrl, serverSelectionTimeoutMS=mongoTimeout)
dataBase = client[mongo_db]
collection = dataBase[mongo_collection_libros]
id_user = ""


def agregarlibro():
    autores = []
    print("Agregar libro nuevo")
    print("===================")
    print()
    codigo = input("Ingrese código del libro: ")
    nombre = input("Ingrese nombre del libro: ")
    # Validacion de numero de autores, dato tipo entero.
    while True:
        try:
            num_autores = int(input("Ingrese el número de autores: "))
            if num_autores > 0:
                break
            else:
                print("\033[91m Error: Por favor, ingrese un número mayor a 0.\033[0m")

        except ValueError:
            print("\033[91m Error: Por favor, ingrese solo números enteros.\033[0m")
            
    for i in range(num_autores):
        autor = input(f"Ingrese el nombre del autor número {i+1}: ")
        autores.append(autor)

    genero = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial del libro: ")

    # Validacion de copias existenes, dato tipo entero.
    while True:
        try:
            copias = int(input("Ingrese el número de copias existentes: "))
            if copias > 0:
                break
            else:
                print("\033[91m Error: Por favor, ingrese un número mayor a 0.\033[0m")

        except ValueError:
            print("\033[91m Error: Por favor, ingrese solo números enteros.\033[0m")

    collection.insert_one({
        "codigo": codigo,
        "nombre": nombre,
        "autores": autores,
        "genero": genero,
        "editorial": editorial,
        "copias": copias
    })

    print()
    print("\033[92m¡Libro agregado correctamente!\033[0m")


def consultarlibro():
    print("Buscar libros")
    print("==============")
    print("1. Código")
    print("2. Nombre")
    print("3. Género")
    print("4. Autor")
    print("==============")

    while True:
        op = input("\nSeleccione un criterio de búsqueda: ")

        if op == "1":
            op = "código"
            criterio = "codigo"
            break

        elif op == "2":
            op = "nombre"
            criterio = "nombre"
            break

        elif op == "3":
            op = "género"
            criterio = "genero"
            break

        elif op == "4":
            op = "autor"
            criterio = "autores"
            break

        else:
            print("\033[91mOpción inválida. Intente nuevamente.\033[0m")
            continue

    print()
    busqueda = input(f"Ingrese el {op} del libro que está buscando: ")
    print()
    filtro = {criterio: busqueda}
    proyeccion = {'_id': 0, 'Código': '$codigo', 'Título': '$nombre',
                  'Autores': '$autores', 'Género': '$genero', 'Editorial': '$editorial', 'Copias totales': '$copias'}

    print("Resultados de busqueda")
    print("======================")
    print()
    resultados = collection.find(filtro, proyeccion)
    pp = pprint.PrettyPrinter(indent=4)
    found = False  # Variable para verificar si se encontraron resultados

    for documento in resultados:
        pp.pprint(documento)
        found = True  # Se encontró al menos un libro

    if not found:
        print("\033[91mNo se encontraron libros con los criterios de búsqueda especificados.\033[0m")


def modificarlibro():
    print("Modificar libro")
    print("==============")
    print("1. Código")
    print("2. Nombre")
    print("3. Género")
    print("4. Autor")
    print("==============")

    while True:
        op = input("\nSeleccione un criterio de búsqueda: ")

        if op == "1":
            op = "código"
            criterio = "codigo"
            break

        elif op == "2":
            op = "nombre"
            criterio = "nombre"
            break

        elif op == "3":
            op = "género"
            criterio = "genero"
            break

        elif op == "4":
            op = "autor"
            criterio = "autor"
            break

        else:
            print("\033[91mOpción inválida. Intente nuevamente.\033[0m")
            continue

    print()
    busqueda = input(f"Ingrese el {op} del libro que desea modificar: ")
    filtro = {criterio: busqueda}

    print()
    # Solicita los nuevos datos al usuario
    autores = []
    codigo = input("Ingrese el nuevo código del libro: ")
    nombre = input("Ingrese el nuevo nombre del libro: ")
    # Validacion de numero de autores, dato tipo entero.
    while True:
        try:
            num_autores = int(input("Ingrese el número de nuevos autores: "))
            if num_autores > 0:
                break
            else:
                print("\033[91m Error: Por favor, ingrese un número mayor a 0.\033[0m")

        except ValueError:
            print("\033[91m Error: Por favor, ingrese solo números enteros.\033[0m")
    for i in range(num_autores):
        autor = input(f"Ingrese el nombre del nuevo autor número {i + 1}: ")
        autores.append(autor)

    genero = input("Ingrese el nuevo género del libro: ")
    editorial = input("Ingrese la nueva editorial del libro: ")

    # Validacion de copias existenes, dato tipo entero.
    while True:
        try:
            copias = int(input("Ingrese el nuevo número de copias existentes: "))
            if copias > 0:
                break
            else:
                print("\033[91m Error: Por favor, ingrese un número mayor a 0.\033[0m")

        except ValueError:
            print("\033[91m Error: Por favor, ingrese solo números enteros.\033[0m")

    # Crea un diccionario con los nuevos datos
    datos_nuevos = {"codigo": codigo, "nombre": nombre, "genero": genero, "autores": autores,
                    "editorial": editorial, "copias": copias}

    # Modifica el documento en la colección
    collection.update_one(filtro, {"$set": datos_nuevos})
    print()
    print("\033[92m¡Libro modificado correctamente!\033[0m")


def borrarlibro():
    print()
    print("Borrar libro")
    print("=============")
    print("1. Código")
    print("2. Nombre")
    print("=============")

    while True:
        op = input("\nSeleccione un criterio de búsqueda: ")

        if op == "1":
            op = "código"
            criterio = "codigo"
            break

        elif op == "2":
            op = "nombre"
            criterio = "nombre"
            break

        elif op == "3":
            op = "género"
            criterio = "genero"
            break

        elif op == "4":
            op = "autor"
            criterio = "autor"
            break

        else:
            print("\033[91mOpción inválida. Intente nuevamente.\033[0m")
            continue

    print()
    busqueda = input(f"Ingrese el {op} del libro que desea borrar: ")
    print()
    filtro = {criterio: busqueda}

    print()
    collection.delete_one(filtro)

    print("\033[92m¡Libro eliminado correctamente!\033[0m")
