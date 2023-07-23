frase = input("deme una frase: ")
letra = input("deme una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador = contador + 1
print(f"la letra {letra} esta {contador} veces en la frase: {frase}")