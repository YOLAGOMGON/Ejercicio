# 10. Taller “Mecánica Pro” – Revisiones del día
# Como mecánico, quiero usar un for que muestre “Revisión X”.
# Si X es igual a 3, mostrar “Revisión especial de motor”.

s = int(input("digite numero de reviciones diarias"))
for x in range(s):
    print("esta es la revision ",x)
    if x == 3:
        print(f"Revision {x} especial de motor")
        break