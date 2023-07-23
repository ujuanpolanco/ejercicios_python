cuanto = float(input("cuanto va a invertir? "))
interes = float(input("cual es el interés porcentual anual? "))
años = int(input("por cuantos años? "))
for i in range(años):
    cuanto *= 1 + interes / 100 
    print (f"Capital tras {(i+1)}  años: {(round(cuanto, 2))}")
