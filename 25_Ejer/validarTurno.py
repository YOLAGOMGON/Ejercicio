# 25. Restaurante “BuenaFunción” – Verificación de turno
# Como gerente, quiero una función verificarTurno(hora) que determine:

# Si la hora es menor que 12 → “Turno de mañana”.
# Si está entre 12 y 18 → “Turno de tarde”.
# Si es mayor → “Turno de noche”.
# El programa principal debe pedir la hora e imprimir el resultado.

def validarTurno (hora):
    if hora <=0 :
        print("que turno es ese mijo")
    if hora <= 12 and hora >0 :
        print("estas en el turno de la mañan")
    elif hora > 12 and hora <= 18:
        print("Turno de la tardee")
    else: 
        print("turno de noche")
    if hora > 24 :
        print("Turnos dobles o q ")

hora = int(input("Digite que hora es "))
validarTurno(hora)