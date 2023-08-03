info = {}
nombre = input("cual es tu nombre? ")
edad = input("cual es tu edad? ")
direccion = input("cual es tu direccion? ")
telefono = input("cual es tu numero de telefono? ")


persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])