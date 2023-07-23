cantidad = float(input ("Hola, cuanto desea invertir? "))
interes = float(input ("cual es el interes anual? "))
años = int(input ("por cuantos años? "))
print("su capital final seria: ",cantidad * (interes / 100 + 1)**años, "pesos")