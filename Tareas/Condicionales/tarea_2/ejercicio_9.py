edad = int(input("cual es tú erdad? "))
if edad < 4:
    print("puedes entrar gratis")
elif edad > 4 and edad <= 18:
    print("debes pagar 5 euros para entrar")
elif edad > 18:
    print("debes pagar 10 euros para entrar")