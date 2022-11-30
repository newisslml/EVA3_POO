from producto import Producto
class Precio(Producto):
    def __init__(self,id,nombre,stock,proovedor,idp,precioventa,preciolista):
        super().__init__(id,nombre,stock,proovedor)
        self.idp = idp
        self.precioventa = precioventa
        self.preciolista = preciolista

    def mostrarprecio(self):
        return Producto.mostrarproducto(self)+\
               "\nID Precio: "+str(self.idp)+\
               "\nPrecio de ventas: "+str(self.precioventa)+\
               "\nPrecio de lista: "+str(self.preciolista)

    def buscarproducto(self,lista,idbuscar):
        for q in lista:
            if q.id == idbuscar:
                return q
        return None
    
    def agregarproducto(self,lista,id):
        q = self.buscarproducto(lista,id) 
        if q == None:
            nombre = input("Ingrese nombre producto: ")
            stock = input("Stock del producto: ")
            idp = id
            preciolista = input("Precio lista: ")
            precioventa = input("Precio de venta: ")
            p = self.proovedor.agregarP()
            pr = Precio(id,nombre,stock,p,idp,precioventa,preciolista)
            lista.append(pr)
        else:
            print("El producto ya existe!")
        return lista
    
    def eliminarP(self,lista,id):
        q = self.buscarproducto(lista,id) 
        if q != None:
            print("ya existe")
      




            