import pprint
import pymongo

mongoHost = "localhost"
mongoPort = "27017"
mongoTimeout = 1000
mongoUrl = "mongodb://"+mongoHost+":"+mongoPort+"/"
mongo_db = "bdnr"
mongo_collection_prestamos = "prestamos"
client = pymongo.MongoClient(mongoUrl, serverSelectionTimeoutMS=mongoTimeout)
dataBase = client[mongo_db]
collection = dataBase[mongo_collection_prestamos]
id_user = ""


def agregarprestamo():
    print("Agregar préstamo nuevo")
    print("===================")
    print()
    codigo = input("Ingrese código del préstamo: ")
    nombre = input("Ingrese nombre del solicitante: ")
    telefono = input("Ingrese el teléfono del solicitante: ")
    email = input("Ingrese el email del solicitante: ")
    cod_libro = input("Ingrese el código del libro prestado: ")
    prestamo_fech = input("Ingrese la fecha del préstamo del libro: ")
    devolucion_fech = input("Ingrese la fecha de la devolución del libro: ")

    collection.insert_one({
        "codigo": codigo,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "cod_libro": cod_libro,
        "prestamo_fech": prestamo_fech,
        "devolucion_fech": devolucion_fech
    })

    print()
    print("\033[92m¡Préstamo agregado correctamente!\033[0m")


def consultarpretamo():
    print("Buscar Préstamos")
    print("==============")
    print("1. Código del préstamo")
    print("2. Nombre del solicitante")
    print("==============")

    while True:
        op = input("\nSeleccione un criterio de búsqueda: ")

        if op == "1":
            op = "código de prestamo"
            criterio = "codigo"
            break

        elif op == "2":
            op = "nombre de solicitante"
            criterio = "nombre"
            break

        else:
            print("\033[91mOpción inválida. Intente nuevamente.\033[0m")
            continue

    print()
    busqueda = input(f"Ingrese el {op} del préstamo que está buscando: ")
    print()
    filtro = {criterio: busqueda}
    proyeccion = {'_id': 0, 'Préstamo': '$codigo', 'Solicitante': '$nombre',
                  'Código del libro': '$cod_libro', 'Email': '$email', 'Teléfono': '$telefono',
                  'Fecha del préstamo': '$prestamo_fech', 'Fecha de devolución': '$devolucion_fech'}

    print("Resultados de busqueda")
    print("======================")
    print()
    resultados = collection.find(filtro, proyeccion)
    pp = pprint.PrettyPrinter(indent=4)
    found = False  # Variable para verificar si se encontraron resultados

    for documento in resultados:
        pp.pprint(documento)
        found = True  # Se encontró al menos un préstamo

    if not found:
        print("\033[91mNo se encontraron préstamos con los criterios de búsqueda especificados.\033[0m")


def modificarprestamo():
    print("Prestamo modificado")


def borrarprestamo():
    print("Prestamo borrado")