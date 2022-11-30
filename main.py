from proovedor import Proovedor
from precio import Precio
lista = []
p = Proovedor("Guitierrez","Granos")
pr = Precio(1,"Arroz",10,p,1,1500,2500)
lista.append(pr)

p = Proovedor("Vera","Pastas")
pr = Precio(2,"Fideos",5,p,2,4500,1500)
lista.append(pr)

p = Proovedor("Guitierrez","Granos")
pr = Precio(3,"Arroz vegetal",20,p,3,5000,5500)
lista.append(pr)

idbuscar = input("Ingrese id a borrar: ")
lista = pr.agregarproducto(lista,idbuscar)

for q in lista:
    print(q.mostrarprecio())
