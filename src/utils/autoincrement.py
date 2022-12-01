
from src.entities.precio import Precio
import operator


def increment_id_precio(listado: list[Precio]):
    item = max(listado, key=operator.attrgetter('idPrecio'))
    return item + 1


def increment_id_producto(listado: list[Precio]):
    item = max(listado, key=operator.attrgetter('idProducto'))
    return item + 1
