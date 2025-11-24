# 1. Cafetería “Buen Café” – Control de tazas servidas
# Como barista, quiero usar un bucle for para mostrar cuántas tazas he servido del 1 al 10, pero si el número es 5, mostrar el mensaje “¡Mitad del turno completada!”.



for i in range(1,10):
    tazas = input("Soy el barista dese una taza de cafe ?")
    print(f"hasta el momento llevas {i} de tazas de cafe")

    i += 1
    if i == 5 :
        print(f"esta es la numero {i}  voy a mitad de mi turno :)")
        continue
    elif i == 10 :
        print(f"Esta es tu taza numero {i}  aun te quedan mas Pero mi turno termino")
        break
print("Fin del programa")