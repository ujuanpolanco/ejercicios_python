compras = {}

compra_1 = input("cual es el primer articulo? ")
precio_1 = int(input("que precio tiene? "))

compras ["compra 1"] = compra_1

compra_2 = input("cual es el segundo articulo? ")
precio_2 = int(input("que precio tiene? "))

compras ["compra 2"] = compra_2

compra_3 = input("cual es el tercer articulo? ")
precio_3 = int(input("que precio tiene? "))

compras ["compra 3"] = compra_3


for i in compras:
    print (compras[i])

valor = precio_1 + precio_2 + precio_3

print (f"estos articulos tienen un valor total de {valor} pesos")
