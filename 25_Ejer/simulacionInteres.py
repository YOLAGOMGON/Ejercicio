# 23. Banco “LoopBank” – Simulación de intereses
# Como analista financiero, quiero una función calcularInteres() que reciba un monto y una tasa (porcentaje) y retorne el valor final después de aplicar el interés una vez.
# El programa principal debe pedir los datos y mostrar el resultado.

def calcularInteres(monto , interes):
    calcu = monto + (monto * (interes / 100))
    return calcu

interes = float(input("Digiteme el porcentaje de interes"))
    
monto = int(input("Digite el monto a prestar"))
print("su valor total es de ",calcularInteres(monto,interes))

