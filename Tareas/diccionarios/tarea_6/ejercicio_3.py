frutas = {
    "Platano" : 1.35,
    "Manzana" : 0.80, 
    "Pera" : 0.85, 
    "Naranja" : 0.70
    }

fruta = input("que fruta deseas? ")
fruta = fruta.title()

if fruta in frutas:

    kilos = float(input("cuantos kilos desea? "))
    print(f"el valor de {fruta} es de {round(frutas[fruta] * kilos, 2)}")

else:

    print("la fruta que ha seleccionado no se encuentra en nuestro catalogo")
    