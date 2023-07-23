genero = input("eres hombre o mujer? ")
nombre = input("cual es tú nombre? ")
if genero == "mujer":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
elif genero =="hombre":
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("tu grupo es el", grupo)