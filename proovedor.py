class Proovedor():
    def __init__(self,nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria
    
    def mostrarP(self):
        return "\nProovedor: "+self.nombre+\
               "\nCategoria: "+self.categoria
    def agregarP(self):
        nombre = input("Nombre proovedor: ")
        categoria = input("Categoria: ")
        p = Proovedor(nombre,categoria)
        return p