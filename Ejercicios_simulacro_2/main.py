# ============================================
# SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS
# Totalmente modular, validado y explicado.
# ============================================

# --------------------------------------------
# Datos iniciales (5 productos precargados)
# --------------------------------------------
inventario = [
    {
        "nombre": "Laptop X200",
        "marca": "Lenovo",
        "categoria": "Computadores",
        "precio_unitario": 3000,
        "stock": 10,
        "garantia": 12
    },
    {
        "nombre": "Mouse Gamer",
        "marca": "Logitech",
        "categoria": "Accesorios",
        "precio_unitario": 120,
        "stock": 30,
        "garantia": 6
    },
    {
        "nombre": "Smartphone A55",
        "marca": "Samsung",
        "categoria": "Celulares",
        "precio_unitario": 1500,
        "stock": 15,
        "garantia": 12
    },
    {
        "nombre": "Parlante Bluetooth",
        "marca": "Sony",
        "categoria": "Audio",
        "precio_unitario": 200,
        "stock": 20,
        "garantia": 8
    },
    {
        "nombre": "Teclado K120",
        "marca": "Logitech",
        "categoria": "Accesorios",
        "precio_unitario": 80,
        "stock": 25,
        "garantia": 6
    }
]

# Lista donde se guardan las ventas
ventas = []


# ======================================================
# Función para validar entrada numérica sin fallos
# ======================================================
def pedir_numero(texto, tipo=float):
    """Pide al usuario un número de forma segura.
       Si escribe algo inválido, vuelve a pedirlo."""
    while True:
        try:
            valor = tipo(input(texto))
            return valor
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número.")


# ======================================================
# 1. MÓDULO DE INVENTARIO
# ======================================================

def agregar_producto():
    """Registra un nuevo producto en el inventario."""
    print("\n--- REGISTRAR PRODUCTO ---")

    nombre = input("Nombre del producto: ")
    marca = input("Marca: ")
    categoria = input("Categoría: ")
    precio_unitario = pedir_numero("Precio unitario: ", float)
    stock = pedir_numero("Cantidad en stock: ", int)
    garantia = pedir_numero("Garantía (meses): ", int)

    producto = {
        "nombre": nombre,
        "marca": marca,
        "categoria": categoria,
        "precio_unitario": precio_unitario,
        "stock": stock,
        "garantia": garantia
    }

    inventario.append(producto)
    print("✔ Producto agregado exitosamente.")


def ver_inventario():
    """Muestra todos los productos del inventario."""
    print("\n--- INVENTARIO ---")
    for i, p in enumerate(inventario):
        print(f"{i+1}. {p['nombre']} | Marca: {p['marca']} | Stock: {p['stock']} | Precio: ${p['precio_unitario']}")


def actualizar_producto():
    """Modifica un producto existente."""
    ver_inventario()
    indice = pedir_numero("Seleccione número de producto a actualizar: ", int) - 1

    if indice not in range(len(inventario)):
        print("❌ Número inválido.")
        return

    print("\nSi deja un campo vacío, se mantiene el valor actual.\n")

    producto = inventario[indice]

    nuevo_nombre = input(f"Nuevo nombre ({producto['nombre']}): ") or producto["nombre"]
    nueva_marca = input(f"Nueva marca ({producto['marca']}): ") or producto["marca"]
    nueva_categoria = input(f"Nueva categoría ({producto['categoria']}): ") or producto["categoria"]

    precio = input(f"Nuevo precio ({producto['precio_unitario']}): ")
    stock = input(f"Nuevo stock ({producto['stock']}): ")
    garantia = input(f"Nueva garantía ({producto['garantia']}): ")

    producto["nombre"] = nuevo_nombre
    producto["marca"] = nueva_marca
    producto["categoria"] = nueva_categoria
    producto["precio_unitario"] = float(precio) if precio else producto["precio_unitario"]
    producto["stock"] = int(stock) if stock else producto["stock"]
    producto["garantia"] = int(garantia) if garantia else producto["garantia"]

    print("✔ Producto actualizado correctamente.")


def eliminar_producto():
    """Elimina un producto del inventario."""
    ver_inventario()
    indice = pedir_numero("Seleccione número de producto a eliminar: ", int) - 1

    if indice not in range(len(inventario)):
        print("❌ Número inválido.")
        return

    eliminado = inventario.pop(indice)
    print(f"✔ Producto '{eliminado['nombre']}' eliminado.")


# ======================================================
# 2. MÓDULO DE VENTAS
# ======================================================

def registrar_venta():
    """Registra una venta y actualiza el inventario automáticamente."""
    print("\n--- REGISTRAR VENTA ---")

    cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (Normal/VIP): ")

    ver_inventario()
    indice = pedir_numero("Seleccione número de producto vendido: ", int) - 1

    if indice not in range(len(inventario)):
        print("❌ Número inválido.")
        return

    producto = inventario[indice]

    cantidad = pedir_numero("Cantidad vendida: ", int)

    if cantidad > producto["stock"]:
        print("❌ Stock insuficiente. No se puede realizar la venta.")
        return

    descuento = pedir_numero("Descuento aplicado (%): ", float)
    fecha = input("Fecha de venta (YYYY-MM-DD): ")

    # Actualiza stock
    producto["stock"] -= cantidad

    total = (producto["precio_unitario"] * cantidad) * (1 - descuento / 100)

    venta = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "descuento": descuento,
        "fecha": fecha,
        "total": total
    }

    ventas.append(venta)
    print("✔ Venta registrada exitosamente.")


def ver_ventas():
    """Muestra el historial completo de ventas."""
    print("\n--- HISTORIAL DE VENTAS ---")
    for v in ventas:
        print(f"{v['fecha']} - {v['producto']} x{v['cantidad']} | Cliente: {v['cliente']} | Total: ${v['total']}")


# ======================================================
# 3. MÓDULO DE REPORTES
# ======================================================

def top_3_productos():
    """Muestra los 3 productos más vendidos."""
    print("\n--- TOP 3 PRODUCTOS MÁS VENDIDOS ---")

    conteo = {}

    for venta in ventas:
        conteo[venta["producto"]] = conteo.get(venta["producto"], 0) + venta["cantidad"]

    ranking = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    print(ranking[:3])


def ventas_por_marca():
    """Agrupa las ventas por marca."""
    print("\n--- VENTAS POR MARCA ---")

    totales = {}

    for venta in ventas:
        marca = next(p["marca"] for p in inventario if p["nombre"] == venta["producto"])
        totales[marca] = totales.get(marca, 0) + venta["total"]

    for marca, total in totales.items():
        print(f"{marca}: ${total}")


def reporte_ingresos():
    """Muestra ingresos brutos y netos."""
    print("\n--- REPORTE DE INGRESOS ---")

    bruto = sum(v["total"] for v in ventas)
    neto = bruto * 0.90  # simulación de costos

    print(f"Ingreso bruto: ${bruto}")
    print(f"Ingreso neto (después del 10%): ${neto}")


# ======================================================
# MENÚ PRINCIPAL
# ======================================================

def menu():
    while True:
        print("""
=============== MENÚ PRINCIPAL ===============
1. Agregar producto
2. Ver inventario
3. Actualizar producto
4. Eliminar producto
5. Registrar venta
6. Ver ventas
7. Top 3 productos más vendidos
8. Ventas por marca
9. Reporte de ingresos
0. Salir
===============================================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            ver_ventas()
        elif opcion == "7":
            top_3_productos()
        elif opcion == "8":
            ventas_por_marca()
        elif opcion == "9":
            reporte_ingresos()
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")


# Ejecutar el sistema
menu()