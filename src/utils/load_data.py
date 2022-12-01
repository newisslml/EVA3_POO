from src.entities.precio import Precio
from src.entities.proveedor import Proveedor
from src.entities.producto import Producto

def load_data():

    lista = []

    proveedor = Proveedor("Guitierrez", "Granos")
    producto = Producto(1, "Arroz", 4, proveedor)
    precio = Precio(producto, 1, 3500, 3000)
    lista.append(precio)


    proveedor = Proveedor("Vera", "Pastas")
    producto = Producto(2, "Fideos", 3, proveedor)
    precio = Precio(producto, 2, 1500, 1000)
    lista.append(precio)


    proveedor = Proveedor("Apablaza", "Abarrotes")
    producto = Producto(3, "Lentejas", 555, proveedor)
    precio = Precio(producto, 3, 5000, 5500)
    lista.append(precio)


    proveedor = Proveedor("Julio", "Art. Aseo")
    producto = Producto(4, "Lavalozas", 2, proveedor)
    precio = Precio(producto, 4, 4360, 4100)
    lista.append(precio)


    proveedor = Proveedor("Candia", "Electrodomesticos")
    producto = Producto(5, "Televisores", 1, proveedor)
    precio = Precio(producto, 5, 450000, 359000)
    lista.append(precio)

    return lista
