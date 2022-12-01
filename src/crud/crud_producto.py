from src.entities.precio import Precio
from src.entities.producto import Producto
from src.entities.proveedor import Proveedor
from src.utils.autoincrement import increment_id_producto, increment_id_precio
import operator


def listar_menor_stock(listaPrecios: list[Precio]):
    listaPrecios.sort(key=operator.attrgetter('stock'))
    for precio in listaPrecios:
        print("Producto: ", precio.nombre)
        print("Stock: ", precio.stock)
        print(">>>>>>>>>>>>>>>>>>>>")


def agregar_producto(listado: list[Precio]):
    print(">>> Debemos agregar los datos del proveedor")
    nombreProveedor = input("Proveedor: ")
    categoria = input("Categoria: ")

    nuevoProveedor = Proveedor(nombreProveedor, categoria)

    print(">>> Agregue los datos del producto")
    idproducto = increment_id_producto(listado)
    nombre = input("Nombre producto: ")
    stock = int(input("Stock: "))

    nuevoProducto = Producto(idproducto, nombre, stock, nuevoProveedor)

    print(">>> Debemos agregar el precio")
    idPrecio = increment_id_precio(listado)
    precioLista = int(input("Precio de Lista: "))
    precioVenta = int(input("Precio de Venta: "))
    nuevoPrecio = Precio(nuevoProducto,
                         idPrecio, precioVenta, precioLista)

    listado.append(nuevoPrecio)
