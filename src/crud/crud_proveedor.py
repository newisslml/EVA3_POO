
from src.entities.precio import Precio


def listar_proveedores(listado: list[Precio]):
    for precio in listado:
        print("Proveedor: ", precio.proovedor.nombre)
        print("Categoria: ", precio.proovedor.categoria)
