interes = 0.04
capital_inicial = float(input("cuanto capital va ingresar? "))
print("su capital al primer año seria: ",capital_inicial * (interes + 1), "pesos")
capital_dos = float(capital_inicial * (interes + 1))
print("su capital al segundo año seria: ",capital_dos * (interes + 1), "pesos")
capital_tres = float(capital_dos * (interes + 1))
print("su capital al tercer año seria: ",capital_tres * (interes + 1), "pesos")