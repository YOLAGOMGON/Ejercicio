# 11. Aerolínea “FlyLoop” – Cálculo de millas acumuladas
# Como viajero frecuente, quiero una función calcular_millas(viajes) que reciba el número de viajes realizados y sume millas según la distancia:

# Viaje corto (< 1000 km): 500 millas
# Medio (1000–3000 km): 1000 millas
# Largo (> 3000 km): 2000 millas
# Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado.

# def calcularMillas(km):
#     millas = 0

#     if km < 1000:
#         millas = 500
#     elif km > 1000 and km < 3000:
#         millas = 1000
#     elif km >= 3000:
#         millas = 2000
#     print(f"estas son las millas en tu viaje{millas}")
#     return  millas
    
# totalMilla = 0

# while True:
#     viajes = input("digite el recorrido del viaje el km (si quieres finalizar copia fin)")
#     if viajes.lower() == "fin":
#         break
#     km = float(viajes)

#     totalMilla += calcularMillas(km)
# print("tu total de millas es de ",totalMilla)





# 12. Hospital “Salud Total” – Evaluador de signos vitales
# Como médico, quiero una función evaluar_paciente() que reciba frecuencia cardiaca y temperatura corporal.
# Si ambos valores están fuera del rango normal (FC > 100 o Temp > 38), mostrar “Paciente en observación”.
# Repetir el proceso con varios pacientes en un bucle while.

# def evaluarPaciente():
#     if fc >= 100 and temp >= 38:
#         print("Paciente en observacion")
#     elif fc >0 and temp > 0:
#         print("Paciente estable")
#     else :
#         print("muerto")

# contador = 0 
# while True:
#     fc = int(input("deme su frecuencia cardiaca (Oprima 0 para romper)"))
#     if fc == 0 :
#         break
#     temp = int(input("Digite su temperatura corporal"))
    
#     evaluarPaciente()
#     print("este fue el paciente numero",contador)

#     contador = contador +1


# 13. Tienda Online “ShopMaster” – Carrito de compras con validaciones
# Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:

# Si el precio es negativo, mostrar error y pedir otro valor.
# Si el precio es mayor a 100.000, aplicar un 20% de descuento.
# Usar while y if dentro de la función hasta ingresar 0 para finalizar.

# def funcion_carrito():
#     if precio <0:
#         print ("Error")
#     elif precio >=100000:
#         Des= precio-(precio*0.20)
#         print("Valor total menos descuento", Des)

# while True:
#     precio= int(input("Ingrese precio del producto  Oprima 0 salir"))
#     if precio ==0:
#         break


#     funcion_carrito()



# 14. Academia “DevLoop” – Calculadora de factoriales
# Como estudiante de programación, quiero una función calcular_factorial(numero) que use un bucle for para calcular el factorial del número.
# Si el número ingresado es negativo, mostrar “Número inválido”.
# De lo contrario, mostrar el resultado.

# def calculadora_de_factoriales():
#     factorial = 1
#     for i in range(1, numero + 1):
#         factorial *= i 
#         if numero < 0 :
#             print("eorr")
#     print(f"el factorial de numero {numero} es de {factorial}")
    

# numero = int(input("digite un numero"))
# calculadora_de_factoriales()


# 15. Empresa “TechManager” – Simulador de rendimiento laboral
# Como jefe de equipo, quiero una función evaluar_empleado(nombre, horas) que:

# Use un bucle for para simular las horas trabajadas (de 1 hasta horas).
# Si la hora es mayor de 8, contar como hora extra.
# Al final, calcular el total de horas normales y extras.
# Mostrar un resumen del empleado.


def Evaluador_empleado():
    extra = 0
    for i in range (1, horas):
        if horas ==24 :
            print("eso es otro dia ")
        if i >= 8 :
            extra += 1
    print(f"{nombre} sus horas laborales normales son de 8  sus horas extras hechas hoy son de {extra} horas extras")


nombre = input("ponga su nombre")
horas = int(input("ponga sus horas trabajadas en el turno de hoy"))
Evaluador_empleado()
