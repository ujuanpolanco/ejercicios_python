contraseña = "pan"
llave = input("cual es la contraseña? ")

while llave != contraseña:
   llave = input("parece que es incorrecto, intente nuevamente: ")
   
if llave == "pan":
    print("correcto")
