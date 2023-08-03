creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

for i in creditos:
    print(f"{i} tiene {creditos[i]} creditos")

print(f"hay un total de " + str(creditos['Matemáticas'] + creditos['Física'] + creditos['Química']) , "creditos")
