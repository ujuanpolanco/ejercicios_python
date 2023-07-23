fecha = input("cual es tu fecha de nacimiento en formato xx/xx/xxxx ? ")
print(f"dia: {fecha[0: -8]} , mes: {fecha[3: -5]} , año: {fecha[6:]}")