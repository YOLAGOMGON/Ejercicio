# 14. Tienda “Ahorra Más” – Caja registradora básica
# Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
# Si la venta supera $100,000, mostrar “Venta destacada”.
# Al final, mostrar el total vendido.
# total =[]
# while True:
#     monto = int(input("digite el monto de la venda (OPRIMA 0 PARA PARAR)"))
#     if monto== 0 :
#         break
#     if monto > 0:
#         total.append(monto)
#         resul = sum(total)
#         if resul >= 100000:
#             print("Venta destacadaaaaa")
#         continue

i = 0 
while True:
    monto =int(input("Digite el monto "))
    i += monto
    if monto == 0:
        break
    
    if i >= 100000:
        print("la venta fue destacada")
        continue
    

print("estas fueron el monto total de las ventas $",i)
