descuento = 0.60
precio = 3.49
pan_vendido = int(input ("cuantas barras de pan que no son del día va a comprar? "))
print ("el precio habitual de una barra de pan es de 3.49 euros, pero por no ser del día se le hace 60% de descuento")
precio_descuento = precio * descuento
valor = precio_descuento * pan_vendido
print("el valor final sera de",round(valor, 2),"euros")