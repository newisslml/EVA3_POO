class Proveedor():
    def __init__(self, nombre: str, categoria: str):
        self.nombre = nombre
        self.categoria = categoria

    def mostrar_proveedor(self):
        return "\nProovedor: "+self.nombre +\
               "\nCategoria: "+self.categoria

    def agregar_proveedor(self):
        nombre = input("Nombre proovedor: ")
        categoria = input("Categoria: ")
        p = Proveedor(nombre, categoria)
        return p
