producto = input('Introduce el nombre del producto: ')
precio = float(input('Introduce el precio con decimales: '))
unidades = int(input('Introduce la cantidad que deseas: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
