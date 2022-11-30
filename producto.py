class Producto():
    def __init__(self,id,nombre,stock,proovedor):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.proovedor = proovedor
    
    def mostrarproducto(self):
        return "\nID: "+str(self.id)+\
               "\nProducto: "+self.nombre+\
               "\nStock: "+str(self.stock)+\
               self.proovedor.mostrarP()