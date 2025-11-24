# 19. Tienda de helados – Registro de clientes atendidos
# Como empleado, quiero usar un while que cuente clientes hasta que el número supere 15.
# Si el número es múltiplo de 5, mostrar “Pausa para limpieza”.
# Al final, mostrar “Turno finalizado”

cliente = 0

while True:
    print(f"Este es el cliente numero {cliente}")
    cliente += 1

    if cliente % 5 == 0:
        print(cliente,"Pausa para Limpieza")
    if cliente >= 15 :
        print("Turno finalizado")
        break