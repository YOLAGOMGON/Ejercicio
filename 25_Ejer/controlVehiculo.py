# 13. Parqueadero “AutoLoop” – Control de vehículos
# Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
# Si entra un número par, mostrar “Vehículo par registrado”.
# Si el total llega a 20, mostrar “Capacidad completa”.

i = 0
while True:

    i +=1
    print(f" han entrado {i} vehiculos al parqueadero")
    if i % 2 ==0 :
        print(f"vehiculo {i}  es par y fue registrado")
        
    if i == 20:
        print("Capacidad maxima mijo pa afuera")
        break