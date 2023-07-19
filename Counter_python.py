"""nombre=input("Ingrese su nombre: ")
print(f"Decime {nombre}¿Qué paso con todo el código?")"""


from collections import Counter

def crear_cliente():
    cliente={}
    cliente['nombre']=input("Ingrese su nombre: ")
    cliente['apellido']=input("Ingrese su apellido: ")
    cliente['domicilio']=input("Ingrese su domiclio: ")
    return cliente

def mostrar_clientes(cliente):
    return f"{cliente['nombre']} {cliente['apellido']} {cliente['domicilio']}"
#Estamos probando el paquete de modulos de Counter
"""myList=[1,1,2,3,4,5,3,2,3,4,1,2,3]
print(Counter(myList)) 

x=input().split(" ")
print(x) """

cli=crear_cliente()
print(mostrar_clientes (cli))

