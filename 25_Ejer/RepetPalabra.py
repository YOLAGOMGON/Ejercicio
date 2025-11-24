
# 18. Academia de inglés – Repetición de palabras
# Como estudiante, quiero ingresar una palabra y usar un for para repetirla 5 veces.
# Si el contador es impar, mostrar la palabra en minúsculas.
# Si es par, mostrarla en mayúsculas.

palabra = input("Digite una palabra")

for i in range(1,6):
    i +=1
    if i % 2 == 0:
        print(palabra.upper())
    else :
        print(palabra.lower())