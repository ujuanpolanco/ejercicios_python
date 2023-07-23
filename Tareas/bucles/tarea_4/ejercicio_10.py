numero = int(input("dame un numero entero: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
