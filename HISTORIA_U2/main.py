lista_Inventario =[ ]

while True:

    print("Elija del menú la opción que desee o DIJITE #4 PARA SALIR")

    print("(1) Agregar producto")
    print("(2) Mostras Inventario")
    print("(3) calcular estadistica")
    print("(4) SALIR")

    opcion= int(input("Elija la opción que desea "))

    if opcion == 4 :
        break
    
    if opcion <=0  and opcion >=5:
        print("Opción invalidad")

    if opcion ==1:
        producto= {
            "Nombre" : input("Ingrese nombre del producto"), 
            "Precio": float(input("Ingrese precio del producto")), 
            "Cantidad": int(input("Ingrese cantidad"))
        }

        lista_Inventario.append(producto)

    if opcion ==2:
        if len(lista_Inventario) ==0:
            print ("Sin información")

        else:        
            for i in lista_Inventario: 
                print (f"Inventario {i} ")


    if opcion ==3:
        total=0
        conteoproductos=0
        for i in lista_Inventario:
            conteoproductos+=1


            total+=i["Precio"]*i["Cantidad"]
        print ("Total Inventario",total )
        print ("Total de productos", conteoproductos)
            

