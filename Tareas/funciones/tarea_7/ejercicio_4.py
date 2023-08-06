factura = 100000
iva = 0.21

def factura_con_iva(factura, iva):
    resultado = factura * iva
    valor_final = resultado + factura
    print(f" el iva es de {resultado}")
    print(f" el total es de {valor_final}")
factura_con_iva(factura, iva)