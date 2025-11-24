# 5. Escuela “Aprende Más” – Promedio de notas
# Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
# Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
# Debe repetirse para varios estudiantes usando un while.

# def promedioNota():
#     estudiantes = 0
#     while True:
#         print("Usted es el estudiante numero",estudiantes)
#         nota1 = float(input("Digite su primera nota en el area"))
#         nota2= float(input("Digite su segunda nota en el area"))
#         nota3 = float(input("Digite su tercera nota en el are"))
#         estudiantes += 1
#         calculo = (nota1+ nota2 +nota3)/3
#         if calculo < 3.0 :
#             print("reprobado promedio de ",calculo)
#         if calculo >= 3.0 and calculo <= 5.0:
#             print("Aprobado promedio de ",calculo)

#         if nota1 == 0:
#             break

# promedioNota()





# 6. Estación “LoopBus” – Simulador de pasajeros
# Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
# Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle.


# def simularViaje():
#     for i in range (pasajero):
#         print("este es el pasajero numero",i)
#         if i == 10 :
#             print(f"lo siento mijo ya vamos llenos los {i - pasajero} demas se quedan")
#             break
#         i += 1
# pasajero = int(input("Digite la cantidad de pasajeros que iran"))

# simularViaje()





# 7. Panadería “Don Pancho” – Control de producción diaria
# Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.
# Si el lote es divisible por 3, mostrar “Verificación de calidad”.
# Al final, mostrar “Producción terminada”.



# def hornear_pan():
    
#     for lote in range(panes):
#         print("este es el lote ",lote)
#         if lote %3 == 0 :
#             print(lote,"Control de calidad|")
        
# panes = int(input("Digite la cantidad de panes"))
# hornear_pan()
# print("Produccion terminada")





# 8. Cine “MovieLoop” – Calculadora de entradas
# Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
# Aplicar precio:

# Menores de 12 → $5.000
# De 12 a 59 → $8.000
# Mayores de 60 → $4.000
# Usar un while y condiciones.

# def calcularEntrada():
    
#     if edad <= 12 and edad > 0:
#         print("El valor de su voleta es de $5.000")
#     elif edad > 12 and edad <=59 :
#         print("El costo de su voleta sera $8.000")
#     else:
#         print("su voleta cuesta $4.000")

# while True:
#     edad = int(input("Digite su edad para entrar al parque"))
#     if edad <= 0:
#         print()
#         break
#     calcularEntrada()







# 9. Tienda “EnergyStore” – Simulador de puntos
# Como cliente, quiero una función calcular_puntos(compras) que use un for para recorrer la cantidad de compras (ingresada por el usuario).
# Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.
# Al final, mostrar los puntos totales.

# def calcularPuntos():
#     suma = 0
#     for compra in range(numeroCompra):

#         if compra %3 ==0 :
#             suma = suma + 10
#             print("se añadio 10 puntos a tu numero de compra ahora quedo de ",suma)
            

#         elif compra % 3 != 0:
#             suma = suma +5
#             print("se añadio 5 puntos a tu numero de compra ahora quedo de ",suma)
        
        

#     print("estos son sus puntos finales",suma)
        

# numeroCompra = int(input("Digite la cantidad de compras"))

# calcularPuntos()









# 10. Academia “CodeStart” – Tabla de multiplicar personalizada
# Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
# Si el resultado es mayor de 50, mostrar también “Resultado alto”.

def tablaMulti():
    for tabla in range(11):
        multi= numero * tabla
        if numero >= 50:
            print("Numero muy alto")
            break
        if numero > 0 :
            print(f"{tabla}x {numero} = {multi}")
        else:
            print("error")
        
        
numero = int(input("digite el numero para ver su tabla"))
tablaMulti()
    
