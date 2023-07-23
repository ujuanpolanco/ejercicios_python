puntuacion = float(input("cual es su puntuación? "))
if puntuacion == 0.0:
    resultado = 2400 * 0.0
    print("su rendimiento es inaceptable, recibira", resultado, "euros")
elif puntuacion == 0.4:
    resultado = 2400 * 0.4
    print("su rendimiento es aceptable, recibira", resultado, "euros")
elif puntuacion >= 0.6:
    resultado = 2400 * puntuacion
    print("su rendimiento es meritorio, recibira", resultado, "euros")