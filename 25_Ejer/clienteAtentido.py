# 4. Tienda “Descuento Express” – Clientes atendidos
# Como cajero, quiero usar un for que muestre “Atendiendo cliente número X” del 1 al 8. Si el cliente es el número 8, mostrar “Último cliente del día”.

for i in range (1,8):
    print("eres el cliente numero",i)
    i +=1
    if i == 8:
        print("Eres mi Ultimo cliente del dia")
