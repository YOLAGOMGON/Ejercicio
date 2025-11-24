# 9. Concurso “Adivina el número secreto”
# Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
# Si acierto, mostrar “¡Correcto!”.
# Si no, mostrar “Intenta otra vez” y seguir hasta acertar.

n = 4
while True:
    numero = int(input("Digite un numero"))
    if numero != n :
        continue
    else: 
        print("Numero correcto")
        break