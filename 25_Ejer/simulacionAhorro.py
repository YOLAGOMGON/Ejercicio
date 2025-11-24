# 11. Banco “PythonBank” – Simulación de ahorro mensual
# Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
# Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
# Al final, mostrar el total acumulado.

ahorromen = float(input("cual es tu ahorro mensual : "))
meta = 1000000
for x in range (1,6):
    print("su ahorro mensual ha sido de $",ahorromen)
    ahorromen += ahorromen


    print("hasta el momento llevas ahorrado $",ahorromen)
    lleva = ahorromen
    if ahorromen== meta :
        print ("hemos llegado a la meta $",meta)
        