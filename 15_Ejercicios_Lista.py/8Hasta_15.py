# 8) Academia “Registro ordenado” — Orden asc/desc configurable
# Como coordinador, quiero una función ordenar_registros(registros, descendente=False) que valide que todos los elementos sean comparables y ordene.

# Si descendente es True, ordenar en orden inverso.
# Recorre la lista para imprimir el TOP 3.

# def ordenar_registros():
#     registro = [2, 5, 1, 8, 323 ]



#     if descen.lower()  == "si":
#         registro.sort(reverse=True)
#         for i in registro[:3]:
#             print(i)
#     else :
#         for i in registro[:3]:
#             print(i)

# descen = input("quiere ordenar la lista :")

# ordenar_registros()




# 9) Música “Playlist Reversa” — Escucha en orden invertido
# Como DJ, quiero una función invertir_playlist(playlist) que valide que no esté vacía y la invierta en sitio.

# Luego, recorre la lista para reproducir las primeras 5 canciones (o menos si no hay suficientes).

# def invertir_playlist():
#     playlist = ["consejos de oror", "stunami", "de trote", "la caja negra", "rojo","mañana sera bonito", "perra", "noches frias"]

#     if not playlist:
#         print("playlist vacia")
#         return
#     else :
#         playlist.reverse()
#         if len(playlist) > 5:
#             print("5 canciones de la playlis")
#             for i in playlist[:5]:
#                 print(i)
#         else:
#             print("se repodrucen estas pocas")
#             for i in playlist:
#                 print(i)

# invertir_playlist()

# 10) Cursos “Duplicar plan de estudio” — Copia segura
# Como tutor, quiero una función clonar_plan(modulos) que cree una copia independiente de la lista original para probar cambios sin afectar la original.

# Verifica con un cambio en la copia que la original no se altere.
# Usa bucles para mostrar diferencias.

# def clonar_plan():
#     copia = listOrigi.copy()
#     for i in copia:
#         añadir = int(input("añade digitos a la lista ?"))
#         copia.append(añadir)
#         copia.reverse()
#         guardar = input("desea guardar cambios en la copia ?")
#         if guardar.lower() == "si":
#             break
#         elif guardar.lower() == "no":
#             continue
#     print(f"esta fue la lista modificada (Copia) {copia}")
#     print(f"este es tu lista original {listOrigi}")


# listOrigi=[222,33,11]

# print(listOrigi)
# clonar_plan()





# 11) Logística “Limpieza de ruta” — Vaciar lista al finalizar
# Como coordinador de ruta, quiero una función finalizar_ruta(paradas) que, tras recorrer y marcar cada parada como “visitada”, limpie la lista.

# Valida si ya está vacía antes de limpiar.
# Muestra un mensaje final de confirmación.

# def finalizar_ruta():
#     ruta=["maniantales","hacienda","occidente","sopetran","palmas","trompom"]
#     if not ruta:
#         return "vacia"
#     else:
#         for i in ruta:
#             numRuta = int(input("diga el numero de la ruta "))
#             print(f" {ruta[numRuta]} visitada")
#             borrar = input("desea guardar y borrar ?")
#             if borrar.lower() == "si":
#                 ruta.clear()
#                 print(ruta)
#                 break
#             elif borrar.lower() == "no":
#                 continue

# finalizar_ruta()    




# 13) E-commerce “Carrito flexible” — Agregar/Quitar según acción
# Como comprador, quiero una función actualizar_carrito(carrito, accion, item, posicion=None) que:

# Si accion es “agregar”, agregue item al final o en posicion válida.
# Si accion es “quitar”, retire por nombre o por índice (si posicion es un entero).
# Valida entradas y usa bucles para mostrar el total de items.


# def actualizar_carrito():
#     carrito = ["platos", "controles", "botellas",]
#     print("escirba agregar para añadir mas productos")
#     print("Escriba Quitar para borrar productos ")
#     conteo = len(carrito)
#     for i in carrito:
#         opction = input("Que opciones desea escriba aqui =")

#         if opction.lower() == "agregar":
#             agregar = input("Dgitie el nombre del producto a agregar ")
#             carrito.append(agregar)
#             conteo += 1
#             print(f"se añadio {agregar} al carrito")
#             print(f"total de items {conteo}")

#         elif opction.lower()== "quitar":
#             borrar = input("Digite el nombre del producto a borrar ")
#             if borrar in carrito:
#                 carrito.remove(borrar)
#                 conteo -= 1
#                 print(f"total de items {conteo}")
#                 print(carrito)

#             else:
#                 print("no se encuentra")
#                 continue
#         else:
#             print("Opcion invalidad ")
#             break
#     print(f" tu lista actual del carrito es {carrito}")

        

# actualizar_carrito()


# 14) RRHH “Top talentos” — Mezclar y ordenar candidatos
# Como reclutador, quiero una función fusionar_candidatos(base_a, base_b, clave_desc=False) que combine dos listas y ordene asc/desc según clave_desc.

# Valida que ambas listas contengan el mismo tipo de dato.
# Recorre para imprimir los primeros N candidatos.

listaOrigi = ["Con","Esto","Inicio"]
listaclon = []
for i in listaOrigi:
    agregar = input("escibre otros atirculos")
    listaclon.append(agregar)
    listaclon = [str(x) for x in listaclon]
    




# 15) Ventas “Depurar duplicados” — Primero elimina, luego compacta
# Como analista, quiero una función depurar_ventas(ventas, umbral) que:

# Recorra la lista y elimine valores no válidos (negativos o None).
# Si un valor se repite más de umbral, retira las apariciones extra hasta dejar umbral.
# Muestra la lista final y la cantidad de elementos removidos.