laptops = []  # Lista
laptop_properties = ["id", "fabricante", "modelo", "precio", "ram", "peso"]

def create_laptop():
    laptop = dict()
    laptop["id"] = int(input("Introduce el id numérico: "))
    """
    for laptop in laptops:
        if laptop["id"] is not None:
            print("Ese id ya existe")
            laptop["id"] = int(input("Introduce el id: "))
    """
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
def edit_laptop():

    product_index = int(input("Introduzca el índice del ordenador que desea editar de 1 a {}: ".format(len(laptops))))

    property_edit = ''
    while property_edit not in laptop_properties:
        property_edit = str(input("Introduzca la propiedad que desea editar: "
                                  "\"id\", "
                                  "\"fabricante\", "
                                  "\"modelo\", "
                                  "\"precio\", "
                                  "\"RAM\", "
                                  "\"peso\": "))
        if property_edit not in laptop_properties:
            continue

        if property_edit == "id":
            laptops[product_index - 1]["id"] = int(
                input("Introduzca el nuevo id del ordenador {}: ".format(product_index)))
        elif property_edit == "fabricante":
            laptops[product_index - 1]["fabricante"] = str(
                input("Introduzca el nuevo fabricante del ordenador {}: ".format(product_index)))
        elif property_edit == "modelo":
            laptops[product_index - 1]["modelo"] = str(
                input("Introduzca el nuevo modelo del ordenador {}: ".format(product_index)))
        elif property_edit == "precio":
            laptops[product_index - 1]["precio"] = int(
                input("Introduzca el nuevo precio del ordenador {}: ".format(product_index)))
        elif property_edit == "RAM":
            laptops[product_index - 1]["RAM"] = int(
                input("Introduzca la nueva RAM del ordenador {}: ".format(product_index)))
        elif property_edit == "peso":
            laptops[product_index - 1]["peso"] = float(
                input("Introduzca el nuevo peso del ordenador {}: ".format(product_index)))

        print("Ordenador {} modificado correctamente."
              .format(laptops[product_index - 1]["fabricante"])
              )

def del_laptop(index_laptop):
    pass
while True:
    print("""
    Menú de opciones: 
    1 - Consultar ordenadores
    2 - Consultar un ordenador
    3 - Crear un ordenador
    4 - Editar un ordenador
    5 - Borrar un ordenador
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
        edit_laptop()
    elif option == 5:
        index_laptop = int(input("introduce el índice del ordenador a borrar de 1 a {}: ".format(len(laptops))))
        for laptop in laptops:
            if laptops[index_laptop -1] is not None:
                laptops.pop(index_laptop -1)
                print("Ordenador borrado")
            else:
                print("El ordenador no existe")

    elif option == 6:
        break

print("fin")