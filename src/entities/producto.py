from src.entities.proveedor import Proveedor


class Producto():
    def __init__(self,
                 id: int,
                 nombre: str,
                 stock: int,
                 proovedor: Proveedor):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.proovedor = proovedor

    def mostrarproducto(self):
        return "\nID: "+str(self.id) +\
               "\nProducto: "+self.nombre +\
               "\nStock: "+str(self.stock) +\
               self.proovedor.mostrarP()
