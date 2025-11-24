# 5. Escuela “Aprende Más” – Registro de tareas entregadas
# Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10, mostrar “¡Todas las tareas recibidas!”. Si aún no llega, mostrar cuántas faltan.

contador = 10
i = 0 
while True :
    print(f"he recibido {i} tareas , aun me faltan {contador}")
    i = i + 1
    contador = contador - 1

    if i == 10 :
        print("Ya tengo todas las tareas")
        break
