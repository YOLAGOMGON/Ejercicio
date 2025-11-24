# # # Mini Proyectos en Python
# # # 1. Sistema de Biblioteca Virtual
# # # Descripción:
# # # Crea un programa que permita gestionar una pequeña biblioteca.

# # # Debe permitir:

# # # Ver los libros disponibles.
# # # Agregar nuevos libros.
# # # Prestar libros (cambiar su estado a “prestado”).
# # # Devolver libros.
# # # Ver el historial de préstamos.

# # # def ver_libros(biblioteca):
# # #     print("LIBROS DISPONIBLES")
# # #     disponibles = False

# # #     for libro in biblioteca:
# # #         if libro["estado"] == "disponible":
# # #             print(f"- {libro['titulo']} ({libro['autor']})")
# # #             disponibles = True

# # #     if not disponibles:
# # #         print("No hay libros disponibles.")


# # # def agregar_libro(biblioteca, titulo, autor):
# # #     nuevo_libro = {
# # #         "titulo": titulo,
# # #         "autor": autor,
# # #         "estado": "disponible",
# # #         "historial": ["Libro agregado a la biblioteca"]
# # #     }
# # #     biblioteca.append(nuevo_libro)
# # #     print(f"Libro '{titulo}' agregado correctamente.")


# # # # ------------------------------------------------------
# # # # FUNCIÓN 3: Prestar libros
# # # # ------------------------------------------------------
# # # def prestar_libro(biblioteca, titulo):
# # #     for libro in biblioteca:
# # #         if libro["titulo"].lower() == titulo.lower():
# # #             if libro["estado"] == "disponible":
# # #                 libro["estado"] = "prestado"
# # #                 libro["historial"].append("Libro prestado")
# # #                 print(f"El libro '{titulo}' ha sido prestado.")
# # #                 return
# # #             else:
# # #                 print(f"El libro '{titulo}' ya está prestado.")
# # #                 return

# # #     print(f"El libro '{titulo}' no existe en la biblioteca.")


# # # # ------------------------------------------------------
# # # # FUNCIÓN 4: Devolver libros
# # # # ------------------------------------------------------
# # # def devolver_libro(biblioteca, titulo):
# # #     for libro in biblioteca:
# # #         if libro["titulo"].lower() == titulo.lower():
# # #             if libro["estado"] == "prestado":
# # #                 libro["estado"] = "disponible"
# # #                 libro["historial"].append("Libro devuelto")
# # #                 print(f"El libro '{titulo}' ha sido devuelto.")
# # #                 return
# # #             else:
# # #                 print(f"El libro '{titulo}' no está prestado.")
# # #                 return

# # #     print(f"El libro '{titulo}' no está registrado en la biblioteca.")



# # # def ver_historial(biblioteca, titulo):
# # #     for libro in biblioteca:
# # #         if libro["titulo"].lower() == titulo.lower():
# # #             print(f"HISTORIAL DEL LIBRO {titulo}")
# # #             for evento in libro["historial"]:
# # #                 print(f"- {evento}")
# # #             return
    
# # #     print(f"El libro '{titulo}' no existe en la biblioteca.")


# # # def menu():
# # #     biblioteca = []

# # #     while True:
# # #         print("SISTEMA DE BIBLIOTECA")
# # #         print("1. Ver libros disponibles")
# # #         print("2. Agregar un libro")
# # #         print("3. Prestar un libro")
# # #         print("4. Devolver un libro")
# # #         print("5. Ver historial de un libro")
# # #         print("6. Salir")

# # #         opcion = input("Seleccione una opción: ")

# # #         if opcion == "1":
# # #             ver_libros(biblioteca)

# # #         elif opcion == "2":
# # #             titulo = input("Ingrese el título: ")
# # #             autor = input("Ingrese el autor: ")
# # #             agregar_libro(biblioteca, titulo, autor)

# # #         elif opcion == "3":
# # #             titulo = input("Ingrese el título del libro a prestar: ")
# # #             prestar_libro(biblioteca, titulo)

# # #         elif opcion == "4":
# # #             titulo = input("Ingrese el título del libro a devolver: ")
# # #             devolver_libro(biblioteca, titulo)

# # #         elif opcion == "5":
# # #             titulo = input("Ingrese el título del libro: ")
# # #             ver_historial(biblioteca, titulo)

# # #         elif opcion == "6":
# # #             print("\nSaliendo del sistema... ¡Hasta luego!")
# # #             break

# # #         else:
# # #             print("Opción inválida. Intente nuevamente.")

# # # menu()


# # # 2. Gestor de Tareas Diarias
# # # Descripción:
# # # Simula una app de tareas pendientes (To-Do List).

# # # Debe permitir:

# # # Agregar tareas.
# # # Marcar tareas como completadas.
# # # Eliminar tareas.
# # # Mostrar todas las tareas (pendientes y completadas).
# # # Salir del sistema.

# # # def agregar_tarea(tareas, descripcion):
# # #     nueva = {
# # #         "descripcion": descripcion,
# # #         "estado": "pendiente"
# # #     }
# # #     tareas.append(nueva)
# # #     print("Tarea agregada:", descripcion)


# # # def completar_tarea(tareas, indice):
# # #     if indice < 0 or indice >= len(tareas):
# # #         print("Índice inválido.")
# # #         return
    
# # #     tareas[indice]["estado"] = "completada"
# # #     print("Tarea completada:", tareas[indice]["descripcion"])


# # # def eliminar_tarea(tareas, indice):
# # #     if indice < 0 or indice >= len(tareas):
# # #         print("Índice inválido.")
# # #         return
    
# # #     eliminada = tareas.pop(indice)
# # #     print("Tarea eliminada:", eliminada["descripcion"])


# # # def mostrar_tareas(tareas):
# # #     if not tareas:
# # #         print("No hay tareas.")
# # #         return

# # #     for i, tarea in enumerate(tareas):
# # #         print(i, "-", tarea["descripcion"], "-", tarea["estado"])


# # # def menu():
# # #     tareas = []

# # #     while True:
# # #         print("Menú:")
# # #         print("1. Agregar tarea")
# # #         print("2. Completar tarea")
# # #         print("3. Eliminar tarea")
# # #         print("4. Mostrar tareas")
# # #         print("5. Salir")

# # #         opcion = input("Seleccione una opción: ")

# # #         if opcion == "1":
# # #             descripcion = input("Descripción de la tarea: ")
# # #             agregar_tarea(tareas, descripcion)

# # #         elif opcion == "2":
# # #             mostrar_tareas(tareas)
# # #             indice = int(input("Índice de la tarea a completar: "))
# # #             completar_tarea(tareas, indice)

# # #         elif opcion == "3":
# # #             mostrar_tareas(tareas)
# # #             indice = int(input("Índice de la tarea a eliminar: "))
# # #             eliminar_tarea(tareas, indice)

# # #         elif opcion == "4":
# # #             mostrar_tareas(tareas)

# # #         elif opcion == "5":
# # #             print("Saliendo...")
# # #             break

# # #         else:
# # #             print("Opción inválida.")


# # # menu()




# # # 3. Calculadora con Historial
# # # Descripción:
# # # Crea una calculadora que permita realizar operaciones básicas y guarde el historial.

# # # Debe permitir:

# # # Sumar, restar, multiplicar y dividir.
# # # Mostrar el resultado de la última operación.
# # # Mostrar todo el historial.
# # # Borrar el historial.

# # # def sumar(a, b):
# # #     return a + b

# # # def restar(a, b):
# # #     return a - b

# # # def multiplicar(a, b):
# # #     return a * b

# # # def dividir(a, b):
# # #     if b == 0:
# # #         print("No se puede dividir por cero.")
# # #         return None
# # #     return a / b


# # # def mostrar_historial(historial):
# # #     if not historial:
# # #         print("El historial está vacío.")
# # #         return
# # #     for item in historial:
# # #         print(item)


# # # def menu():
# # #     historial = []
# # #     ultimo_resultado = None

# # #     while True:
# # #         print("\nMenu:")
# # #         print("1. Sumar")
# # #         print("2. Restar")
# # #         print("3. Multiplicar")
# # #         print("4. Dividir")
# # #         print("5. Mostrar último resultado")
# # #         print("6. Mostrar historial")
# # #         print("7. Borrar historial")
# # #         print("8. Salir")

# # #         opcion = input("Seleccione una opción: ")

# # #         if opcion in ["1", "2", "3", "4"]:
# # #             a = float(input("Primer número: "))
# # #             b = float(input("Segundo número: "))

# # #             if opcion == "1":
# # #                 resultado = sumar(a, b)
# # #             elif opcion == "2":
# # #                 resultado = restar(a, b)
# # #             elif opcion == "3":
# # #                 resultado = multiplicar(a, b)
# # #             elif opcion == "4":
# # #                 resultado = dividir(a, b)

# # #             if resultado is not None:
# # #                 ultimo_resultado = resultado
# # #                 historial.append("Resultado: " + str(resultado))
# # #                 print("Resultado:", resultado)

# # #         elif opcion == "5":
# # #             if ultimo_resultado is None:
# # #                 print("No hay resultado previo.")
# # #             else:
# # #                 print("Último resultado:", ultimo_resultado)

# # #         elif opcion == "6":
# # #             mostrar_historial(historial)

# # #         elif opcion == "7":
# # #             historial.clear()
# # #             print("Historial borrado.")

# # #         elif opcion == "8":
# # #             print("Saliendo...")
# # #             break

# # #         else:
# # #             print("Opción inválida.")


# # # menu()



# # # 4. Mini Tienda Virtual
# # # Descripción:
# # # Simula una tienda pequeña donde el usuario puede comprar productos.

# # # Debe permitir:

# # # Mostrar el catálogo de productos con precios.
# # # Agregar productos al carrito.
# # # Ver el total a pagar.
# # # Finalizar la compra.

# # # def mostrar_catalogo(catalogo):
# # #     print("Catalogo de productos:")
# # #     for nombre, precio in catalogo.items():
# # #         print(nombre, "-", precio)


# # # def agregar_carrito(catalogo, carrito, producto):
# # #     if producto in catalogo:
# # #         carrito.append(catalogo[producto])
# # #         print("Producto agregado:", producto)
# # #     else:
# # #         print("Producto no encontrado.")


# # # def ver_total(carrito):
# # #     if not carrito:
# # #         print("El carrito esta vacio.")
# # #         return
# # #     total = sum(carrito)
# # #     print("Total a pagar:", total)


# # # def menu():
# # #     catalogo = {
# # #         "manzanas": 1500,
# # #         "pan": 2000,
# # #         "leche": 4000,
# # #         "huevos": 8000
# # #     }

# # #     carrito = []

# # #     while True:
# # #         print("\nMenu:")
# # #         print("1. Mostrar catalogo")
# # #         print("2. Agregar producto al carrito")
# # #         print("3. Ver total a pagar")
# # #         print("4. Finalizar compra")

# # #         opcion = input("Seleccione una opcion: ")

# # #         if opcion == "1":
# # #             mostrar_catalogo(catalogo)

# # #         elif opcion == "2":
# # #             producto = input("Escriba el nombre del producto: ").lower()
# # #             agregar_carrito(catalogo, carrito, producto)

# # #         elif opcion == "3":
# # #             ver_total(carrito)

# # #         elif opcion == "4":
# # #             print("Compra finalizada.")
# # #             ver_total(carrito)
# # #             break

# # #         else:
# # #             print("Opcion invalida.")


# # # menu()



# # # 5. Sistema de Recetas
# # # Descripción:
# # # Crea un programa que almacene y muestre recetas.

# # # Debe permitir:

# # # Agregar una receta con ingredientes y pasos.
# # # Buscar receta por nombre.
# # # Listar todas las recetas.
# # # Eliminar receta.

# # def agregar_receta(recetas):
# #     nombre = input("Nombre de la receta: ").lower()
# #     ingredientes = input("Ingredientes separados por coma: ")
# #     pasos = input("Pasos de la receta: ")

# #     recetas[nombre] = {
# #         "ingredientes": ingredientes,
# #         "pasos": pasos
# #     }

# #     print("Receta agregada:", nombre)


# # def buscar_receta(recetas):
# #     nombre = input("Nombre de la receta a buscar: ").lower()

# #     if nombre in recetas:
# #         print("Receta encontrada:", nombre)
# #         print("Ingredientes:", recetas[nombre]["ingredientes"])
# #         print("Pasos:", recetas[nombre]["pasos"])
# #     else:
# #         print("La receta no existe.")


# # def listar_recetas(recetas):
# #     if not recetas:
# #         print("No hay recetas registradas.")
# #         return

# #     print("Lista de recetas:")
# #     for nombre in recetas:
# #         print(nombre)


# # def eliminar_receta(recetas):
# #     nombre = input("Nombre de la receta a eliminar: ").lower()

# #     if nombre in recetas:
# #         del recetas[nombre]
# #         print("Receta eliminada:", nombre)
# #     else:
# #         print("La receta no existe.")


# # def menu():
# #     recetas = {}

# #     while True:
# #         print("\nMenu:")
# #         print("1. Agregar receta")
# #         print("2. Buscar receta")
# #         print("3. Listar todas las recetas")
# #         print("4. Eliminar receta")
# #         print("5. Salir")

# #         opcion = input("Seleccione una opcion: ")

# #         if opcion == "1":
# #             agregar_receta(recetas)

# #         elif opcion == "2":
# #             buscar_receta(recetas)

# #         elif opcion == "3":
# #             listar_recetas(recetas)

# #         elif opcion == "4":
# #             eliminar_receta(recetas)

# #         elif opcion == "5":
# #             print("Saliendo...")
# #             break

# #         else:
# #             print("Opcion invalida.")


# # menu()



# # # 6. Gestor de Cuentas Bancarias
# # # Descripción:
# # # Simula un sistema para gestionar múltiples cuentas.

# # # Debe permitir:

# # # Crear una nueva cuenta (nombre y saldo inicial).
# # # Depositar o retirar dinero en una cuenta seleccionada.
# # # Consultar el saldo.
# # # Ver todas las cuentas creadas.

# def crear_cuenta(cuentas):
#     nombre = input("Nombre de la cuenta: ").lower()
#     saldo = float(input("Saldo inicial: "))

#     cuentas[nombre] = saldo
#     print("Cuenta creada:", nombre)


# def depositar(cuentas):
#     nombre = input("Cuenta a depositar: ").lower()

#     if nombre not in cuentas:
#         print("La cuenta no existe.")
#         return

#     monto = float(input("Monto a depositar: "))
#     cuentas[nombre] += monto
#     print("Deposito realizado. Nuevo saldo:", cuentas[nombre])


# def retirar(cuentas):
#     nombre = input("Cuenta a retirar: ").lower()

#     if nombre not in cuentas:
#         print("La cuenta no existe.")
#         return

#     monto = float(input("Monto a retirar: "))

#     if monto > cuentas[nombre]:
#         print("Saldo insuficiente.")
#     else:
#         cuentas[nombre] -= monto
#         print("Retiro realizado. Nuevo saldo:", cuentas[nombre])


# def consultar_saldo(cuentas):
#     nombre = input("Cuenta a consultar: ").lower()

#     if nombre not in cuentas:
#         print("La cuenta no existe.")
#     else:
#         print("Saldo de", nombre, ":", cuentas[nombre])


# def ver_cuentas(cuentas):
#     if not cuentas:
#         print("No hay cuentas registradas.")
#         return

#     print("Cuentas registradas:")
#     for nombre, saldo in cuentas.items():
#         print(nombre, "-", saldo)


# def menu():
#     cuentas = {}

#     while True:
#         print("\nMenu:")
#         print("1. Crear cuenta")
#         print("2. Depositar dinero")
#         print("3. Retirar dinero")
#         print("4. Consultar saldo")
#         print("5. Ver todas las cuentas")
#         print("6. Salir")

#         opcion = input("Seleccione una opcion: ")

#         if opcion == "1":
#             crear_cuenta(cuentas)

#         elif opcion == "2":
#             depositar(cuentas)

#         elif opcion == "3":
#             retirar(cuentas)

#         elif opcion == "4":
#             consultar_saldo(cuentas)

#         elif opcion == "5":
#             ver_cuentas(cuentas)

#         elif opcion == "6":
#             print("Saliendo...")
#             break

#         else:
#             print("Opcion invalida.")


# menu()



# # # 7. Sistema de Reservas de Cine
# # # Descripción:
# # # Permite reservar asientos para una película.

# # # Debe permitir:

# # # Mostrar asientos disponibles.
# # # Reservar un asiento (cambiar su estado a “ocupado”).
# # # Cancelar una reserva.
# # # Ver el mapa de asientos actualizado.

# def mostrar_asientos(asientos):
#     print("Asientos disponibles:")
#     for i, estado in enumerate(asientos):
#         print(i, "-", estado)


# def reservar_asiento(asientos):
#     mostrar_asientos(asientos)
#     indice = int(input("Numero de asiento a reservar: "))

#     if indice < 0 or indice >= len(asientos):
#         print("Asiento invalido.")
#         return

#     if asientos[indice] == "ocupado":
#         print("El asiento ya esta ocupado.")
#     else:
#         asientos[indice] = "ocupado"
#         print("Asiento reservado.")


# def cancelar_reserva(asientos):
#     mostrar_asientos(asientos)
#     indice = int(input("Numero de asiento a cancelar: "))

#     if indice < 0 or indice >= len(asientos):
#         print("Asiento invalido.")
#         return

#     if asientos[indice] == "libre":
#         print("El asiento ya esta libre.")
#     else:
#         asientos[indice] = "libre"
#         print("Reserva cancelada.")


# def ver_mapa(asientos):
#     print("Mapa de asientos:")
#     for i, estado in enumerate(asientos):
#         print(i, "-", estado)


# def menu():
#     asientos = ["libre", "libre", "libre", "libre", "libre"]

#     while True:
#         print("\nMenu:")
#         print("1. Mostrar asientos disponibles")
#         print("2. Reservar asiento")
#         print("3. Cancelar reserva")
#         print("4. Ver mapa de asientos")
#         print("5. Salir")

#         opcion = input("Seleccione una opcion: ")

#         if opcion == "1":
#             mostrar_asientos(asientos)

#         elif opcion == "2":
#             reservar_asiento(asientos)

#         elif opcion == "3":
#             cancelar_reserva(asientos)

#         elif opcion == "4":
#             ver_mapa(asientos)

#         elif opcion == "5":
#             print("Saliendo...")
#             break

#         else:
#             print("Opcion invalida.")


# menu()


# # # 8. Registro de Estudiantes
# # # Descripción:
# # # Sistema básico de gestión de estudiantes.

# # # Debe permitir:

# # # Registrar estudiantes (nombre, edad, nota).
# # # Buscar estudiante por nombre.
# # # Mostrar el promedio general.
# # # Mostrar lista completa de estudiantes.


# def registrar_estudiante(estudiantes):
#     nombre = input("Nombre del estudiante: ").lower()
#     edad = int(input("Edad: "))
#     nota = float(input("Nota: "))

#     estudiantes.append({
#         "nombre": nombre,
#         "edad": edad,
#         "nota": nota
#     })

#     print("Estudiante registrado.")


# def buscar_estudiante(estudiantes):
#     nombre = input("Nombre del estudiante a buscar: ").lower()

#     for est in estudiantes:
#         if est["nombre"] == nombre:
#             print("Estudiante encontrado:")
#             print("Nombre:", est["nombre"])
#             print("Edad:", est["edad"])
#             print("Nota:", est["nota"])
#             return

#     print("No se encontro el estudiante.")


# def mostrar_promedio(estudiantes):
#     if not estudiantes:
#         print("No hay estudiantes registrados.")
#         return

#     total = 0
#     for est in estudiantes:
#         total += est["nota"]

#     promedio = total / len(estudiantes)
#     print("Promedio general:", promedio)


# def mostrar_lista(estudiantes):
#     if not estudiantes:
#         print("No hay estudiantes registrados.")
#         return

#     print("Lista de estudiantes:")
#     for est in estudiantes:
#         print(est["nombre"], "-", est["edad"], "-", est["nota"])


# def menu():
#     estudiantes = []

#     while True:
#         print("Menu:")
#         print("1. Registrar estudiante")
#         print("2. Buscar estudiante")
#         print("3. Mostrar promedio general")
#         print("4. Mostrar lista completa")
#         print("5. Salir")

#         opcion = input("Seleccione una opcion: ")

#         if opcion == "1":
#             registrar_estudiante(estudiantes)

#         elif opcion == "2":
#             buscar_estudiante(estudiantes)

#         elif opcion == "3":
#             mostrar_promedio(estudiantes)

#         elif opcion == "4":
#             mostrar_lista(estudiantes)

#         elif opcion == "5":
#             print("Saliendo...")
#             break

#         else:
#             print("Opcion invalida.")


# menu()

# # # 9. Juego: Adivina el Número
# # # Descripción:
# # # El sistema genera un número aleatorio del 1 al 100 y el jugador debe adivinarlo.

# # # Debe permitir:

# # # Adivinar hasta acertar o rendirse.
# # # Contar el número de intentos.
# # # Mostrar si el número ingresado es mayor o menor.
# # # Reiniciar el juego.

# import random

# def jugar():
#     numero = random.randint(1, 100)
#     intentos = 0

#     while True:
#         entrada = input("Ingrese un numero o escriba rendirse: ").lower()

#         if entrada == "rendirse":
#             print("Te rendiste. El numero era:", numero)
#             break

#         intento = int(entrada)
#         intentos += 1

#         if intento == numero:
#             print("Adivinaste el numero en", intentos, "intentos.")
#             break
#         elif intento < numero:
#             print("El numero es mayor.")
#         else:
#             print("El numero es menor.")


# def menu():
#     while True:
#         print("Menu:")
#         print("1. Jugar")
#         print("2. Salir")

#         opcion = input("Seleccione una opcion: ")

#         if opcion == "1":
#             jugar()
#         elif opcion == "2":
#             print("Saliendo...")
#             break
#         else:
#             print("Opcion invalida.")


# menu()

# # # 10. Control de Gastos Personales
# # # Descripción:
# # # Sistema para registrar y analizar gastos diarios.

# # # Debe permitir:

# # # Registrar un gasto (nombre, monto, categoría).
# # # Mostrar el total gastado.
# # # Mostrar gastos por categoría.
# # # Eliminar un gasto.


def registrarGasto ():
    print("vamos a agregar un gasto")
    nombre = input("digite el nombre del gasto")
    monto = float(input("Digite cuanto fue el precio del gasto"))
    categoria = input("Cual es la categoria del gasto")

    Gasto = {
        "Nombre" : nombre,
        "Monto" : monto,
        "Categoria" : categoria
    }
