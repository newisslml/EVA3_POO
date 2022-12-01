from entities.precio import Precio


def listar_precios(listaPrecios: list[Precio]):
    for precio in listaPrecios:
        print("Producto: ", precio.nombre)
        print("Precio Lista: ", precio.precioLista)
        print("Precio Venta: ", precio.precioVenta)
        print(">>>>>>>>>>>>>>>>>>>>")
