# 20. Aplicación “Inicio Seguro” – Intentos de inicio de sesión
# Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
# Si acierto, mostrar “Acceso permitido”.
# Si agoto los intentos, mostrar “Acceso denegado”.

conteo = 0
contra = "123"
while True :
    contraseña = input("Digite una contraseña")
    conteo += 1
    if conteo == 3:
        print("Tus intentos han terminado")
        break
    if contraseña != contra :
        print("contraseña incorrecta")
        continue
    else:
        print("acceso permitido")
        break
    
