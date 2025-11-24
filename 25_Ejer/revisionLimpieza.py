# 7. Restaurante “Buen Sabor” – Revisión de limpieza
# Como jefe de cocina, quiero usar un for para repetir 3 veces el mensaje “Limpia tu estación”.
# Si es la última vez, mostrar “¡Revisión completada!”.


for i in range(3):
    print("LIMPIAA TU ESTACIOOON")
    i += 1
    if i == 3:
        print("Revision Completada")
        break
