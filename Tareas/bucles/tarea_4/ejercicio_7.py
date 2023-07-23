valor = int(input("te dare la tabla del 1 hasta el 10 del númer entero que quieras, cual número vas a usar? "))
for numero in range(1, 11):
     resultado = valor * numero
     print(f"{valor} * {numero} = {resultado}")
