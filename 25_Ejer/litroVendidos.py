# 16. Gasolinera “LoopFuel” – Control de litros vendidos
# Como operador, quiero usar un while que sume litros hasta superar 100.
# Cada vez que se venda una cantidad, verificar:

# Si el total aún es menor que 100 → mostrar “Sigue vendiendo”.
# Si llega o supera 100 → mostrar “Meta diaria alcanzada”.

Lit = 0

while True:
    venta = int(input("cuantos galones desea comprar"))
    Lit += venta
    print(f"se vendio {Lit} litros")
    
    if Lit <= 100:
        print("sigamos vendinedo aun faltan")
        continue
    if Lit >= 100 :
        print(f"estos fueron los litro vendidos {Lit}")
        break
        
