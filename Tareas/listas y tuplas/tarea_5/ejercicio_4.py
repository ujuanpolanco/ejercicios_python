numeros_ganadores =[]
print("a continuacion tendras que dar 6 numeros ganadores")
for i in range(6):
    numeros_ganadores.append(int(input("Introduce un número ganador: ")))
numeros_ganadores.sort()
print(f"Los números ganadores son {numeros_ganadores}")
