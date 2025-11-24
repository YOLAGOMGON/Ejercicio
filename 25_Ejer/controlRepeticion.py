# 2. Gimnasio “Level Up” – Control de repeticiones
# Como deportista, quiero ingresar un número de repeticiones y usar un for para imprimir “Repetición X completada”.
# Si X es divisible por 3, mostrar además “¡Excelente ritmo!”

ahorromen = int(input("numero de repeticones por serie : "))

for x in range (ahorromen):
    print(f"llevas {x} repiticones hechas")
    x +=1 

    if x % 3 == 0 :
        print("llevas buen ritmo")
    