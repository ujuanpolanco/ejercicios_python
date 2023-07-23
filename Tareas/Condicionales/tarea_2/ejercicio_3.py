dividendo = int(input("deme un número para el dividendo "))
divisor = int(input("ahora un número para el divisor "))
if divisor != 0:
    resultado = dividendo / divisor
    print ("el resultado de su operación es", resultado)
elif divisor == 0:
    print ("Error")