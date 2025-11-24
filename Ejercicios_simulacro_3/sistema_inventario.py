

from datetime import datetime

inventario = {}
ventas = []

# el requerimiento dice que se inicialice con 5 productos precargados
def inicializar_productos():
  
    productos_iniciales = [
        {
            "id": 1,
            "nombre": "Laptop HP",
            "marca": "HP",
            "categoria": "Computadoras",
            "precio": 850.00,
            "stock": 15,
            "garantia": 12
        },
        {
            "id": 2,
            "nombre": "Mouse Logitech",
            "marca": "Logitech",
            "categoria": "Accesorios",
            "precio": 25.50,
            "stock": 50,
            "garantia": 6
        },
        {
            "id": 3,
            "nombre": "Teclado Mecánico",
            "marca": "Corsair",
            "categoria": "Accesorios",
            "precio": 120.00,
            "stock": 20,
            "garantia": 12
        },
        {
            "id": 4,
            "nombre": "Monitor Samsung",
            "marca": "Samsung",
            "categoria": "Monitores",
            "precio": 300.00,
            "stock": 10,
            "garantia": 24
        },
        {
            "id": 5,
            "nombre": "Auriculares Sony",
            "marca": "Sony",
            "categoria": "Audio",
            "precio": 150.00,
            "stock": 30,
            "garantia": 12
        }
    ]
    
    for producto in productos_iniciales:
        inventario[producto["id"]] = producto

# Gestión de inventario
def registrar_producto():
    """Registra un nuevo producto en el inventario"""
    try:
        print("\n--- Register New Product ---")
        id_producto = int(input("Enter product ID: "))
        
        if id_producto in inventario:
            print("Error: Product ID already exists!")
            return
        
        nombre = input("Enter product name: ").strip()
        marca = input("Enter brand: ").strip()
        categoria = input("Enter category: ").strip()
        precio = float(input("Enter unit price: "))
        stock = int(input("Enter stock quantity: "))
        garantia = int(input("Enter warranty (months): "))
        
        if precio < 0 or stock < 0 or garantia < 0:
            print("Error: Negative values are not allowed!")
            return
        
        inventario[id_producto] = {
            "id": id_producto,
            "nombre": nombre,
            "marca": marca,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "garantia": garantia
        }
        print("Product '{}' registered successfully!".format(nombre))
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print("Error: {}".format(e))

def consultar_producto():
    """Consulta un producto por ID"""
    try:
        print("\n--- Consult Product ---")
        id_producto = int(input("Enter product ID: "))
        
        if id_producto in inventario:
            producto = inventario[id_producto]
            print("\nProduct ID: {}".format(producto['id']))
            print("Name: {}".format(producto['nombre']))
            print("Brand: {}".format(producto['marca']))
            print("Category: {}".format(producto['categoria']))
            print("Price: ${:.2f}".format(producto['precio']))
            print("Stock: {}".format(producto['stock']))
            print("Warranty: {} months".format(producto['garantia']))
        else:
            print("Error: Product not found!")
            
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        print("Error: {}".format(e))

def listar_productos():
    """Lista todos los productos del inventario"""
    print("\n--- Product List ---")
    if not inventario:
        print("No products in inventory.")
        return
    
    for producto in inventario.values():
        print("ID: {} | {} | Brand: {} | Stock: {} | Price: ${:.2f}".format(
            producto['id'], producto['nombre'], producto['marca'], 
            producto['stock'], producto['precio']))

def actualizar_producto():
    """Actualiza un producto existente"""
    try:
        print("\n--- Update Product ---")
        id_producto = int(input("Enter product ID to update: "))
        
        if id_producto not in inventario:
            print("Error: Product not found!")
            return
        
        producto = inventario[id_producto]
        print("\nCurrent product: {}".format(producto['nombre']))
        
        print("\nEnter new values (press Enter to keep current value):")
        nombre = input("Name [{}]: ".format(producto['nombre'])).strip()
        marca = input("Brand [{}]: ".format(producto['marca'])).strip()
        categoria = input("Category [{}]: ".format(producto['categoria'])).strip()
        precio = input("Price [${}]: ".format(producto['precio'])).strip()
        stock = input("Stock [{}]: ".format(producto['stock'])).strip()
        garantia = input("Warranty (months) [{}]: ".format(producto['garantia'])).strip()
        
        if nombre:
            producto['nombre'] = nombre
        if marca:
            producto['marca'] = marca
        if categoria:
            producto['categoria'] = categoria
        if precio:
            producto['precio'] = float(precio)
        if stock:
            producto['stock'] = int(stock)
        if garantia:
            producto['garantia'] = int(garantia)
        
        print("Product updated successfully!")
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print("Error: {}".format(e))

def eliminar_producto():
    """Elimina un producto del inventario"""
    try:
        print("\n--- Delete Product ---")
        id_producto = int(input("Enter product ID to delete: "))
        
        if id_producto in inventario:
            nombre = inventario[id_producto]['nombre']
            confirmar = input("Are you sure you want to delete '{}'? (yes/no): ".format(nombre)).strip().lower()
            if confirmar == 'yes':
                del inventario[id_producto]
                print("Product '{}' deleted successfully!".format(nombre))
            else:
                print("Operation cancelled.")
        else:
            print("Error: Product not found!")
            
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        print("Error: {}".format(e))

# Gestión de ventas
def calcular_descuento(tipo_cliente, precio_total):
    """Calcula el descuento según el tipo de cliente"""
    descuentos = {
        "regular": 0.0,
        "premium": 0.10,
        "vip": 0.20
    }
    
    descuento_porcentaje = descuentos.get(tipo_cliente.lower(), 0.0)
    return precio_total * descuento_porcentaje

def registrar_venta():
    """Registra una nueva venta"""
    try:
        print("\n--- Register Sale ---")
        
        if not inventario:
            print("Error: No products in inventory!")
            return
        
        listar_productos()
        id_producto = int(input("\nEnter product ID to sell: "))
        
        if id_producto not in inventario:
            print("Error: Product not found!")
            return
        
        producto = inventario[id_producto]
        cantidad = int(input("Enter quantity (available: {}): ".format(producto['stock'])))
        
        if cantidad <= 0:
            print("Error: Quantity must be greater than 0!")
            return
        
        if cantidad > producto['stock']:
            print("Error: Insufficient stock!")
            return
        
        cliente = input("Enter client name: ").strip()
        if not cliente:
            print("Error: Client name cannot be empty!")
            return
        
        print("\nClient types: regular, premium, vip")
        tipo_cliente = input("Enter client type: ").strip().lower()
        
        if tipo_cliente not in ["regular", "premium", "vip"]:
            print("Error: Invalid client type! Using 'regular'.")
            tipo_cliente = "regular"
        
        precio_unitario = producto['precio']
        precio_total = precio_unitario * cantidad
        descuento = calcular_descuento(tipo_cliente, precio_total)
        precio_final = precio_total - descuento
        
        fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        venta = {
            "id": len(ventas) + 1,
            "cliente": cliente,
            "tipo_cliente": tipo_cliente,
            "id_producto": id_producto,
            "nombre_producto": producto['nombre'],
            "marca": producto['marca'],
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "precio_total": precio_total,
            "descuento": descuento,
            "precio_final": precio_final,
            "fecha": fecha_venta
        }
        
        ventas.append(venta)
        inventario[id_producto]['stock'] -= cantidad
        
        print("\nSale registered successfully!")
        print("Total: ${:.2f}".format(precio_total))
        print("Discount: ${:.2f}".format(descuento))
        print("Final price: ${:.2f}".format(precio_final))
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print("Error: {}".format(e))

def consultar_ventas():
    """Consulta el historial de ventas"""
    print("\n--- Sales History ---")
    if not ventas:
        print("No sales registered.")
        return
    
    for venta in ventas:
        print("\nSale ID: {}".format(venta['id']))
        print("Client: {} ({})".format(venta['cliente'], venta['tipo_cliente']))
        print("Product: {} ({})".format(venta['nombre_producto'], venta['marca']))
        print("Quantity: {}".format(venta['cantidad']))
        print("Price: ${:.2f} (Discount: ${:.2f})".format(venta['precio_final'], venta['descuento']))
        print("Date: {}".format(venta['fecha']))

# Módulo de reportes
def top_productos_vendidos():
    """Muestra el top 3 de productos más vendidos"""
    print("\n--- Top 3 Best Selling Products ---")
    
    if not ventas:
        print("No sales registered.")
        return
    
    # Contar ventas por producto
    ventas_por_producto = {}
    for venta in ventas:
        id_producto = venta['id_producto']
        if id_producto not in ventas_por_producto:
            ventas_por_producto[id_producto] = {
                "nombre": venta['nombre_producto'],
                "cantidad_total": 0
            }
        ventas_por_producto[id_producto]['cantidad_total'] += venta['cantidad']
    
    # Ordenar por cantidad vendida
    productos_ordenados = sorted(
        ventas_por_producto.items(),
        key=lambda x: x[1]['cantidad_total'],
        reverse=True
    )
    
    # Mostrar top 3
    top_3 = productos_ordenados[:3]
    for i, (id_producto, datos) in enumerate(top_3, 1):
        print("{}. {} - Total sold: {} units".format(i, datos['nombre'], datos['cantidad_total']))

def ventas_por_marca():
    """Agrupa y muestra ventas por marca"""
    print("\n--- Sales by Brand ---")
    
    if not ventas:
        print("No sales registered.")
        return
    
    ventas_marca = {}
    for venta in ventas:
        marca = venta['marca']
        if marca not in ventas_marca:
            ventas_marca[marca] = {
                "cantidad": 0,
                "ingreso": 0.0
            }
        ventas_marca[marca]['cantidad'] += venta['cantidad']
        ventas_marca[marca]['ingreso'] += venta['precio_final']
    
    for marca, datos in ventas_marca.items():
        print("\n{}:".format(marca))
        print("  Units sold: {}".format(datos['cantidad']))
        print("  Revenue: ${:.2f}".format(datos['ingreso']))

def ingresos_bruto_neto():
    """Calcula ingresos brutos y netos"""
    print("\n--- Gross and Net Income ---")
    
    if not ventas:
        print("No sales registered.")
        return
    
    # Usando función lambda para calcular totales
    calcular_total = lambda ventas, campo: sum(v[campo] for v in ventas)
    
    ingreso_bruto = calcular_total(ventas, 'precio_total')
    total_descuentos = calcular_total(ventas, 'descuento')
    ingreso_neto = calcular_total(ventas, 'precio_final')
    
    print("Gross income: ${:.2f}".format(ingreso_bruto))
    print("Total discounts: ${:.2f}".format(total_descuentos))
    print("Net income: ${:.2f}".format(ingreso_neto))

def rendimiento_inventario():
    """Reporte de rendimiento del inventario"""
    print("\n--- Inventory Performance Report ---")
    
    if not inventario:
        print("No products in inventory.")
        return
    
    print("\nProduct Performance:")
    for producto in inventario.values():
        # Contar ventas de este producto
        ventas_producto = [v for v in ventas if v['id_producto'] == producto['id']]
        cantidad_vendida = sum(v['cantidad'] for v in ventas_producto)
        
        stock_inicial = producto['stock'] + cantidad_vendida if cantidad_vendida > 0 else producto['stock']
        porcentaje_vendido = (cantidad_vendida / stock_inicial * 100) if stock_inicial > 0 else 0
        
        print("\n{} ({}):".format(producto['nombre'], producto['marca']))
        print("  Current stock: {}".format(producto['stock']))
        print("  Units sold: {}".format(cantidad_vendida))
        print("  Sales percentage: {:.1f}%".format(porcentaje_vendido))

# Menú principal
def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("ELECTRONICS STORE - INVENTORY AND SALES SYSTEM")
    print("="*50)
    print("1. Register Product")
    print("2. Consult Product")
    print("3. List All Products")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Register Sale")
    print("7. Consult Sales History")
    print("8. Top 3 Best Selling Products")
    print("9. Sales by Brand")
    print("10. Gross and Net Income")
    print("11. Inventory Performance Report")
    print("0. Exit")
    print("="*50)

def main():
    """Función principal del programa"""
    inicializar_productos()
    print("System initialized with 5 preloaded products.")
    
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSelect an option: ").strip()
            
            if opcion == "0":
                print("\nThank you for using the system. Goodbye!")
                break
            elif opcion == "1":
                registrar_producto()
            elif opcion == "2":
                consultar_producto()
            elif opcion == "3":
                listar_productos()
            elif opcion == "4":
                actualizar_producto()
            elif opcion == "5":
                eliminar_producto()
            elif opcion == "6":
                registrar_venta()
            elif opcion == "7":
                consultar_ventas()
            elif opcion == "8":
                top_productos_vendidos()
            elif opcion == "9":
                ventas_por_marca()
            elif opcion == "10":
                ingresos_bruto_neto()
            elif opcion == "11":
                rendimiento_inventario()
            else:
                print("Error: Invalid option. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            break
        except Exception as e:
            print("Unexpected error: {}".format(e))
            print("Please try again.")

if __name__ == "__main__":
    main()

