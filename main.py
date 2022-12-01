from src.crud.crud_producto import listar_menor_stock
from src.crud.crud_proveedor import listar_proveedores
from src.utils.load_data import load_data
from src.crud.crud_producto import agregar_producto
from src.utils.autoincrement import increment_id_producto
from src.utils.reporte import reporte_total

listado = load_data()

reporte_total(listado)

def spaces_menus():
    print("\n")
    print("·····································")


def not_option():
    print("No existe esa opcion, intente nuevamente...")


def menu_principal():
    spaces_menus()
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Listar Productos con menor Stock")
    print("4. Listar Proveedores")
    print("5. Reporte")
    option = int(input("Ingrese su Opcion de (1-5): "))
    return option


def algo():
    print("haciendo algo")


    # Loop infinito hasta que el usuario decida Salir = break
while True:
    option = menu_principal()
    match option:
        case 1:
            agregar_producto(listado)
        case 2:
            algo()
        case 3:
            listar_menor_stock(listado)
        case 4:
            listar_proveedores(listado)
        case 5: 
            reporte_total(listado)
        case _:
            not_option()
