tipos_de_moneda = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("dame una divisa: ")
if moneda.title() in tipos_de_moneda:
    print(tipos_de_moneda[moneda.title()])
else:
    print("La divisa no está.")
