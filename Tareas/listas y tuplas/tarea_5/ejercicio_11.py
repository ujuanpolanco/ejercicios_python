numeros_1 = (1, 2, 3)
numeros_2 = (-1, 0, 2)
producto = 0
for i in range(len(numeros_1)):
    producto = producto + numeros_1[i]*numeros_2[i]
print(f"El producto de los vectores {numeros_1} y {numeros_2} es {producto}")
