from src.entities.precio import Precio
from src.entities.proveedor import Proveedor
from src.entities.producto import Producto

def load_data():

    lista = []

    proveedor = Proveedor("Guitierrez", "Granos")
    producto = Producto(111, "Arroz", 4, proveedor)
    precio = Precio(producto, proveedor, 888, 2500, 3000)
    lista.append(precio)


    proveedor = Proveedor("Vera", "Pastas")
    producto = Producto(222, "Fideos", 3, proveedor)
    precio = Precio(producto, proveedor, 666, 4500, 1500)
    lista.append(precio)


    proveedor = Proveedor("Apablaza", "Abarrotes")
    producto = Producto(444, "Lentejas", 555, proveedor)
    precio = Precio(producto, proveedor, 1212, 5000, 5500)
    lista.append(precio)


    proveedor = Proveedor("Julio", "Art. Aseo")
    producto = Producto(3333, "Lavalozas", 2, proveedor)
    precio = Precio(producto, proveedor, 2121, 5000, 5500)
    lista.append(precio)


    proveedor = Proveedor("Candia", "Electrodomesticos")
    producto = Producto(2121, "Televisores", 1, proveedor)
    precio = Precio(producto, proveedor, 3131, 40000, 50000)
    lista.append(precio)

    return lista
