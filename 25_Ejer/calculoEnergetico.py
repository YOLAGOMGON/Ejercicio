# 22. Gimnasio “StrongFit” – Cálculo de energía
# Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

# Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
# Si son 5 o más → “¡Buen trabajo!”.

def CalcularEnergia(repet):
    
    for i in range(repet):
        if i <= 5:
            print("Necesitas mas esfuerzo")
        if i >5:
            print("buen Trabajo")
            break

repet = int(input("escribeme el numero de repeticiones"))

CalcularEnergia(repet)
    