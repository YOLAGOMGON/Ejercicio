# 24. Escuela “Aprende con Funciones” – Promedio de notas
# Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
# Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”.

def promedioNota(not1 , not2, not3):
    promedio = (not1 + not2 + not3) / 3
    print(promedio)
    if promedio <= 3.0 :
        print("Reprobado")
    else:
        print("Aprobado")

not1 = float(input("Digite su primer nota"))
not2 = float(input("Digite su segunda nota"))
not3 = float(input("Digite su tercer nota"))

promedioNota(not1,not2,not3)
