from src.crud.crud_producto import listar_precios, listar_menor_precio
from src.utils.load_data import load_data

listado = load_data()


def spaces_menus():
    print("\n")
    print("·····································")


def not_option():
    print("No existe esa opcion, intente nuevamente...")


def menu_principal():
    spaces_menus()
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Listar Productos")
    option = int(input("Ingrese su Opcion de (1-5): "))
    return option


def algo():
    print("haciendo algo")


    # Loop infinito hasta que el usuario decida Salir = break
while True:
    option = menu_principal()
    match option:
        case 1:
            algo()
        case 2:
            algo()
        case 3:
            listar_menor_precio(listado)
        case _:
            not_option()
