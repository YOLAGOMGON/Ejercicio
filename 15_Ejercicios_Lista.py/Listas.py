# Todos los ejercicios deben:

# Implementar al menos una función.
# Usar validaciones y/o bucles.
# Manipular listas con métodos de listas.
# 1) Restaurante “Menú Dinámico” — Agregar plato del día
# Como chef, quiero una función agregar_plato(menu, plato) que valide que plato no esté vacío y lo agregue a la lista menu.

# Si el plato ya existe, mostrar “plato duplicado”.
# Recorre el menú al final para imprimirlo numerado.
# Sugerencia: usa list.append().

# def agregarPlato():
#     if plato == "":
#         print("esto no puede estar vacio")
#     if plato in mennu:
#         print("plato duplicado")
#         return
#     mennu.append(plato)
    
#     print(f"el plato {plato} fue agregado al mennu")
# mennu = []
# while True:
#     plato = input("digite un plato // oprima fin para salir  :")
#     if plato.lower() == "fin":
#         break
#     agregarPlato()




# 2) Teatro “Butacas VIP” — Insertar reserva en posición
# Como encargado de reservas, quiero una función insertar_reserva(butacas, nombre, posicion) que valide que posicion esté en rango y ubique la reserva en esa posición.

# Si la posición no es válida, no inserta y muestra error.
# Luego, recorre la lista para confirmar el orden.
# Sugerencia: usa list.insert().

# def insertReserva(butacas,nombre,posicion):
#     if posicion < 0 or posicion > len(butacas):
#         print("Posicion - asiento invalido")
#     else:
#         butacas.insert(posicion,nombre)
#         for i,nombre in enumerate(butacas,start=1):
#             print(f"butaca {i} : {nombre}")
# butacas = ['esteban','diego']

# while True:
#     nombre = input("Digite su nombre")
#     posicion = int(input("Digite el numero del asiento en que desea sentarse"))
#     if nombre.lower() == "fin":
#         break

#     insertReserva(butacas,nombre,posicion)





# 3) Tienda “Combo Pack” — Extender inventario
# Como supervisor, quiero una función extender_inventario(actual, nuevos) que valide que nuevos no esté vacío y una ambas listas.

# Muestra el tamaño total al final.
# Recorre la lista para destacar los recién agregados.
# Sugerencia: usa list.extend().

# def extenderInventario():
#     if not nuevo:
#         print("No se agregaron productos, la lista está vacía.")
#         return

#     #recorre la lista de nuevo
#     for producto in nuevo:
#         # si producto tambien se encunetra en antiguo entonces esta repetido
#         if producto in antiguo:
#             print(f"{producto}' ya está en el inventario, no se agrega.")
#         else:
#             antiguo.append(producto)
#             print(f"{producto} agregado al inventario.")

#     print(f"Inventario total: {len(antiguo)} productos")
#     print("Listado completo del inventario:", antiguo)
    
    
# antiguo = ["esteban", "yolanda", "sebastian"]
# nuevo = []
# while True:
#     pernuevo = input("digite la nueva lista  // ponga fin para cerrar  ")

#     if pernuevo.lower() == "fin":
#         break
    
#     nuevo.append(pernuevo)

#     extenderInventario()
# print(f"inventario extendido {antiguo}")




# 4) Biblioteca “Depuración de catálogo” — Eliminar libro específico
# Como bibliotecario, quiero una función eliminar_libro(catalogo, titulo) que verifique si el título está y lo quite.

# Si no existe, mostrar “no encontrado”.
# Imprimir los libros restantes con un bucle.
# Sugerencia: usa list.remove().

# def eliminarLibro():
#     if len(catalogo) >= 4 :
#         print("estos son los libros disponibles ",catalogo)

#         titulo = input("diga el libro que quieres eliminar")
#         for titu in catalogo:
#             if titulo in catalogo:
#                 catalogo.remove(titulo)
#                 print("usted elimino el libro",titulo)
# catalogo =[]
# while True:
#     libro = input("digite los libros que se encuntran disponible  // oprime fin para ver libors restante  :")
#     if libro.lower() == "fin":
#         break
#     catalogo.append(libro)
#     eliminarLibro()

    
# print("Este es el catalogo de libros aun disponible",catalogo)


# 5) Cine “Liberar última silla” — Quitar el final
# Como administrador de sala, quiero una función liberar_ultima(butacas) que valide que hay elementos y quite el último asiento reservado; debe retornar el valor removido.

# Si no hay butacas, mostrar “sala vacía”.
# Imprimir el estado final.
# Sugerencia: usa list.pop() sin índice.

# def liberarUltima(butaca):
#     if butaca == []:
#         print("La sala esta vacia")
#     if len(butaca) >2 :
#         reserva = input("Tienes una reserva hecha?")
#         if reserva.lower() == "si":
#             ultimo = butaca.pop()
#             print("el asiento que se elimino fue",ultimo)
        
#         else:
#             print(f"en este momentos no tenemos butacas disponibles")  
            
    

# butaca = []
# while True:
#     numero = int(input("Ingrese el numero de butacas disponibles"))
#     if numero == 0:
#         print("sala vaciaa")
#         break
#     butaca.append(numero)
#     print(butaca)
    
#     liberarUltima(butaca)





# 6) Soporte “Búsqueda de ticket” — Encontrar primera coincidencia
# Como agente de soporte, quiero una función buscar_ticket(tickets, codigo) que valide si codigo está y devuelva su índice.

# Si no existe, retorna -1.
# Usa un bucle para confirmar si hay duplicados y contarlos.
# Sugerencia: usa list.index() (maneja excepciones) y/o list.count().

# def buscarTickes():
#     conteo = 0
#     i = 0
#     if numCodig not in codigo:
#         return-1
    
#     indice = codigo.index(numCodig)

#     duplicados = codigo.count(numCodig)
#     print(f"el codigo {numCodig} se encontro en el indice{indice}")

#     if duplicados > 1:
#         print(f"este codigo aparece {duplicados} veces")
#     else : 
#         print("codigo no duplicado")
#     return indice
# codigo = [123,654,989,000]
# numCodigo = []
# while True:
#     numCodig = int(input("digite el codigo que cree que es"))
#     if numCodig == 0 :
#         break
    

#     buscarTickes()

# def buscar_ticket(tickets, codigo):
#     # 1. Verificar si existe
#     if codigo not in tickets:
#         return -1

#     # 2. Obtener índice de la primera coincidencia
#     indice = tickets.index(codigo)

#     # 3. Contar duplicados
#     repetidos = tickets.count(codigo)

#     print(f"El código {codigo} está en el índice {indice}")

#     if repetidos > 1:
#         print(f"El código aparece {repetidos} veces (duplicado)")
#     else:
#         print("El código no está duplicado")

#     return indice


# # LISTA DE TICKETS
# tickets = [123, 654, 989, 123, 777, 123, 654]

# while True:
#     num = input("Digite un código para buscar (0 para salir): ")

#     if num == "0":
#         break

#     num = int(num)
#     resultado = buscar_ticket(tickets, num)

#     if resultado == -1:
#         print("El ticket NO existe")
#     else:
#         print("Búsqueda finalizada")



# 7) Deportes “Marcador frecuente” — Contar apariciones
# Como estadístico, quiero una función contar_marcador(marcadores, valor) que valide tipos y devuelva cuántas veces aparece valor.

# Si no aparece, retornar 0.
# Recorre la lista para imprimir posiciones donde aparece.
# Sugerencia: usa list.count().

# valor = [123, 876, 123, 98, 000, 876]
# while True:
#     marcador = int(input("digite el valor que se repite"))
#     if marcador == 0 :
#         break
#     if marcador not in valor:
#         print("0")
        
#     else :
#         indice = valor.index(marcador)
#         duplicado = valor.count(marcador)
#         print(f" su codigo {marcador} esta en el indice {indice}")
#         if duplicado > 1:
#             print(f"el codigo se repite #{duplicado}  veces")
#         else:
#             print("Codigo no duplicado")
            

