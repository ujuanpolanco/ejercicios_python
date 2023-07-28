vocales = ["a", "e", "i", "o", "u"]
palabra = input("dame una plabra: ")
for vocal in palabra:
    if vocal in vocales:
        numero_de_vocal = palabra.count(vocal)
        print(f"hay {numero_de_vocal} {vocal}")

