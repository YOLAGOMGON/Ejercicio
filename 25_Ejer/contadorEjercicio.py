# 15. Academia “CodeStart” – Contador de ejercicios completados
# Como estudiante, quiero usar un for del 1 al número que indique.
# Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
# Si no, solo mostrar “Ejercicio X completado”.

rango = int(input("Digite el rango"))

for i in range(rango):
    i += 1
    if i % 5 ==0 :
        print("Gran avance ")
        continue
    else :
        print(f"El ejercicio {i} esta completado")