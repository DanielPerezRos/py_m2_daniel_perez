laptops = []  # Lista

def create_laptop():
    laptop = dict()
    laptop["id"] = int(input("Introduce el id: "))
    for laptop in laptops:
        if laptop["id"] is not None:
            print("Ese id ya existe")
            laptop["id"] = int(input("Introduce el id: "))

    laptop["fabricante"] = input("Introduce el fabricante: ")
    laptop["modelo"] = input("Introduce el modelo: ")
    laptop["precio"] = int(input("Introduce el precio(€): "))
    laptop["ram"] = int(input("Introduce la RAM(Gb): "))
    laptop["peso"] = float(input("Introduce el peso(Kg.): "))

    laptops.append(laptop)
    print("Ordenador registrado")

def find_laptop(id_laptop):
    for laptop in laptops:
        if laptop["id"] == id_laptop:
            return laptop

while True:
    print("""
    Menú de opciones: 
    1 - Consultar ordenadores
    2 - Consultar un ordenador
    3 - Crear un ordenador
    4 - Editar
    5 - borrar
    6 - Salir
    """)
    option = int(input("Selecciona una opción: "))
    if option == 1:
        if len(laptops) == 0:
            print("No hay ordenadores disponibles")
        else:
            print(laptops)
    elif option == 2:
        if len(laptops) == 0:
            print("No hay ordenadores disponibles")
            continue

        id_laptop = int(input("introduce el id "))

        laptop = find_laptop(id_laptop)
        if laptop is not None:
            print(laptop)
        else:
            print("No encontrado")


    elif option == 3:
        create_laptop()
    elif option == 4:
        print("Has elegido 4")
    elif option == 5:
        print("Has elegido 5")
    elif option == 6:
        break

print("fin")