from src.entities.proveedor import Proveedor


class Producto():
    def __init__(self,
                 idProducto: int,
                 nombre: str,
                 stock: int,
                 proovedor: Proveedor):
        self.idProducto = idProducto
        self.nombre = nombre
        self.stock = stock
        self.proovedor = proovedor

    def mostrarproducto(self):
        return "\nID: "+str(self.idProducto) +\
               "\nProducto: "+self.nombre +\
               "\nStock: "+str(self.stock) +\
               self.proovedor.mostrarP()
