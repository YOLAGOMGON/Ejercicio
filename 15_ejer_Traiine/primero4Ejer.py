# 2. Gimnasio “Level Up” – Control de repeticiones
# Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las repeticiones del 1 al número indicado.
# Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”.

#-------------------------------------------------
# def repeticion(n):
#     for repet in range (n):
#         print("este es tu repeticon numero",repet)
#         if repet % 2 == 0:
#             print(repet,"Repeticion Par")
#         else :
#             print(repet,"repeticion impar")

# n = int(input("digite cuantas series va a hacer"))
# repeticion(n)




# 3. Tienda “LoopShop” – Descuentos acumulados
# Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
# Si el precio supera 50.000, aplicar 10% de descuento.
# Al final, mostrar la suma total de las compras con descuento.

#---------------------------------------------------
# def aplicarDescuento():
#     contador = 0
#     while True:
#         precio = int(input("digite el valor (OPRIMA 0 PARA SALIR)"))
#         contador += precio
#         descuento = 0.10
#         if precio == 0 :
#             print(contador, "este es el precio a pagar")
#             break
            
#         if contador >= 50000:
#             des = contador-(contador * descuento)
#             print("este es el precio con descuento $",des)
#         else:
#             print("este es el valor a pagar $",contador)


# aplicarDescuento()



# 4. Banco “PythonBank” – Evaluador de crédito
# Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:

# Apruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.
# Si no cumple, mostrar “Crédito rechazado”.
# Usar condicionales dentro de la función.

def evaluarCredito():

    edad = int(input("Digite su edad"))
    if edad < 18 :
        print("menor de edad ")
    elif edad >= 18  and edad <= 60:
        ingreso = int(input("cual es su ingreso anual $"))

        if ingreso >= 2000000 :
            print("Credito aprobado")
        else:
            print("Ni lo sueñes")


evaluarCredito()