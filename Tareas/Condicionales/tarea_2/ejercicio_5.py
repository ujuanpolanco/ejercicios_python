edad = int(input("cuantos años tienes? "))
ingresos = int(input("cuales son tus ingreso mensuales? "))
if edad >= 16 and ingresos >= 1000:
    print("tienes que tributar")
else:
    print("no tienes que tributar")