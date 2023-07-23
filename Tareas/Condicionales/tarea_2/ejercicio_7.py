renta = int(input("cual es su renta anual? "))
if renta >= 0 and renta < 10000:
    print("su impositivo es del 5%")
elif renta >= 10000 and renta < 20000:
    print("su impositivo es del 15%")
elif renta >= 20000 and renta < 35000:
    print("su impositivo es del 20%")
elif renta >= 35000 and renta < 60000:
    print("su impositivo es del 30%")
elif renta >= 60000:
    print("su impositivo es del 45%")