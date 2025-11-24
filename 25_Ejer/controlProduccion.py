# 6. Fábrica “LoopTech” – Control de producción
# Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
# Si el número es par, mostrar “Producto verificado”.
# Si es impar, mostrar “Producto pendiente”.

cantidas = int(input("digite la cantidas del rango que desee"))

for i in range(cantidas):
    i += 1
    if i % 2 != 0 :
        print(i," Producto pendiente")
    else:
        print(i," Producto verificado")
