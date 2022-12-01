
from src.entities.precio import Precio


def reporte_total(listado: list[Precio]):

    totalVenta = 0
    totalLista = 0

    for precio in listado:
        totalLista = totalLista + precio.precioLista
        totalVenta = totalVenta + precio.precioVenta

    print(" >>>>> REPORTE SEGUN STOCK <<<<<< ")
    print("Total precio venta: ", totalVenta)
    print("Total precio lista: ", totalLista)
    print("Por vender: ", totalVenta - totalLista)
