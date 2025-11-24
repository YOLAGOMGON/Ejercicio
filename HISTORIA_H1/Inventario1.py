#Se realiza un contador con while 
while True :
#Se declaran las variables con input para que la persona ingrese lo que se le pregunte tambien lalmado como cadena de valores
    Nombre = str(input("Ingrese nombre producto " ))
    Precio = float ( input("Ingrese precio producto ") )
    Cantidad=int(input("Ingrese cantidad " ))
#Se realiza un if para que se rompa el ciclo
    if Nombre == "":
        
        break

#Se realiza la validación de la variable precio igual 0 como valor invalido y se solicita ingresar un valor valido
    if Precio<=0:
        print("ERROR Ingrese un valor valido")
#Se realiza la validación de la variable cantidad es igual a 0 como valor invalio y se solicita ingresar un valor valido
    if Cantidad <=0:
        print("ERROR Ingrese valor valido")
  
#Se realiiza un else si no son las opciones anteriores es esto
    else:

#Se define la variable Costo_Total don sse multiplica precio por la cantidad y se imprime el resultado       
        Costo_Total= Precio*Cantidad
        print  ("Valor costo total",Costo_Total)
#Se realoiza un print donde muestra detalladamente los productos con cantidad, precio precio y el total
        print ("Nombre del producto", Nombre, "Precio Unitario", Precio, "Cantidad",Cantidad, "Total",Costo_Total)

# Se realiza un inventario para llevar el control de las cantidades que se han ingresado, las cantidades y el precio por unidad, ademas totaliza los costos
