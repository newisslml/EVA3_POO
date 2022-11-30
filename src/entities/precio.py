from src.entities.producto import Producto
from src.entities.proveedor import Proveedor


class Precio(Producto):
    def __init__(self,
                 producto: Producto,
                 proveedor: Proveedor,
                 idPrecio: int,
                 precioVenta: int,
                 precioLista: int):
        super().__init__(producto.id, producto.nombre, producto.stock, proveedor)
        self.idPrecio = idPrecio
        self.precioVenta = precioVenta
        self.precioLista = precioLista

    def mostrar_precio(self):
        return Producto.mostrarproducto(self) +\
            "\nID Precio: "+str(self.idPrecio) +\
            "\nPrecio de ventas: "+str(self.precioVenta) +\
            "\nPrecio de lista: "+str(self.precioLista)

    def buscar_producto(self, lista, idbuscar):
        for q in lista:
            if q.id == idbuscar:
                return q
        return None

    def agregar_producto(self, lista, id):
        q = self.buscarproducto(lista, id)
        if q == None:
            nombre = input("Ingrese nombre producto: ")
            stock = input("Stock del producto: ")
            idp = id
            preciolista = input("Precio lista: ")
            precioventa = input("Precio de venta: ")
            p = self.proovedor.agregarP()
            pr = Precio(id, nombre, stock, p, idp, precioventa, preciolista)
            lista.append(pr)
        else:
            print("El producto ya existe!")
        return lista

    def eliminar_producto(self, lista, id):
        q = self.buscarproducto(lista, id)
        if q != None:
            print("ya existe")
