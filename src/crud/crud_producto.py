from src.entities.precio import Precio
import operator


def listar_precios(listaPrecios: list[Precio]):
    for precio in listaPrecios:
        print("Producto: ", precio.nombre)
        print("Precio Lista: ", precio.precioLista)
        print("Precio Venta: ", precio.precioVenta)
        print(">>>>>>>>>>>>>>>>>>>>")


def listar_menor_precio(listaPrecios: list[Precio]):
    listaPrecios.sort(key=operator.attrgetter('stock'))
    for precio in listaPrecios:
        print("Producto: ", precio.nombre)
        print("Stock: ", precio.stock)
        print(">>>>>>>>>>>>>>>>>>>>")
