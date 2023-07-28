palabra = input("Introduce una palabra: ")
palabra_al_reves = palabra
palabra = list(palabra)
palabra_al_reves = list(palabra_al_reves)
palabra_al_reves.reverse()
if palabra == palabra_al_reves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")