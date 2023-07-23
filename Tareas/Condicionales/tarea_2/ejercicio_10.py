tipo_de_pizza = input("desa pizza normal o vegetariana? ")
if tipo_de_pizza == "vegetariana":
    ingrediente = input("que ingrediente desea?(Pimiento o tofu) ")
    print ("su pizza es vegetarian y tendra", ingrediente, "como ingrediente")
elif tipo_de_pizza == "normal":
    ingrediente = input("que ingrediente desea?(Peperoni, Jamón o Salmón) ")
    print ("su pizza es normal y tendra", ingrediente, "como ingrediente")