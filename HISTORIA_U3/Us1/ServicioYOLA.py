import json 
import csv



lista_inventario=[]

def agregar_producto():
    while True:
        nombre= str(input("Ingrese nombre del producto"))
        precio= float (input ("Ingrese precio producto"))
        cantidad= int(input("Ingrese cantidad de producto"))

        inventario ={
            "nombre":nombre, 
            "precio": precio,
            "cantidad": cantidad,

        }
    

        lista_inventario.append(inventario)
        print (lista_inventario) 
        while True:
            salir = input('Desea agregar otro Producto? (s/n): ')
            if salir.lower() == "s":
                print(f'\nTotal de Producto: {lista_inventario}')
                break
            elif salir.lower() == "n":
                return

def mostrar_prodcutos(inventario):
    if not  inventario: 
        print("Producto no encontrado")
    else:
        for i in lista_inventario: 
            print(f"nombre {i['nombre']} precio{i['precio']} cantidad {i['cantidad']}")

def buscar_producto(inventario):
    if not inventario: 
        print("no hay producto para mostrar")
    else:
        buscar= input("Digite nombre del producto buscar")
        for i in lista_inventario:
            if i["nombre"]==buscar:
                print("este es el producto encontrado, ", i )

def actualizar_producto (inventario):
    if not inventario:
        print ("producto no encontrado")
    else:
        actualizar= input("ingrese nombre del procduto a actualizar")
        for i in inventario:
            if i["nombre"] == actualizar:
                print("Producto encontrado", i)

                nombre=input ("Desea cambiar el nombre Si / no")
                if nombre.lower()== "si":
                    nombre=input ("nombre nuevo a actualizar  ")
                    i["nombre"]=nombre


                
                precio= input("Desea cambiar Precio SI-NO  ")
                if precio.lower()== "si":
                    precio=float(input ("precio nuevo a actualizar  "))
                    i["precio"]=precio


                cantidad= input("Desea cambiar cantidad SI-NO " )
                if cantidad.lower()== "si":
                    cantidad=int(input ("cantidad nuevo a actualizar  "))
                    i["precio"]=cantidad

                print("Guardado con exito el producto", i   )
                while True:
                    salir = input('Desea actualizar otro Producto? (s/n): ')
                    if salir.lower() == "s":
                        print(f'\nTotal de Producto: {lista_inventario}')
                        break
                    elif salir.lower() == "n":
                        return
                    
def eliminar_producto(inventario):
    if not inventario:
        print("No exixte registro")
    else:
        eliminar= input ("Ingrese nombre del producto a eliminar")
        for i in inventario:
            if i ["nombre"] == eliminar:
                eliminar=input("Esta seguro que desea Eliminar   SI-NO")
                if eliminar.lower()=="si":
                    inventario.remove(i)
                    print ("Elproducto eliminado es", i)

def calcular_estadistica(inventario):
    # !-------- Funcion Estadisticas ------------!
    if not inventario:
        print("\n[ADVERTENCIA] No hay productos en el inventario.\n")
        return

    unidades_totales = sum(prod["cantidad"] for prod in inventario)
    valor_total = sum(prod["cantidad"] * prod["precio"] for prod in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"]) 
    #Indica cómo seleccionar el valor que se comparará. y lambda es Indica que, para cada producto, use su "Cantidad" para comparar
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("\n────────── ESTADÍSTICAS DEL INVENTARIO ──────────")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f" Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)")
    print("──────────────────────────────────────────────────\n")

ARCHIVO_JSON = "Inventario.json"
ARCHIVO_CSV = "Inventario.csv"
def guardar_json():
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(lista_inventario, archivo, indent=4)
    print("\n[OK] Datos guardados en estudiantes.json\n")

def cargarJSON():
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return []   # si no existe, lista vacía
    
def cargarJSON_en_lista():
    global lista_inventario
    lista_inventario = cargarJSON()
    print("\n[OK] Inventario cargado desde Inventario.json\n")

# ✔ Exportar a CSV
def exportarCSV():
    with open(ARCHIVO_CSV, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre", "Cantidad", "Precio"])  # encabezados
        for prod in lista_inventario:
            writer.writerow([prod["nombre"],prod["cantidad"],prod["precio"]])

    print("\n[OK] Datos exportados a Inventario.csv\n")

def cargarCSV():
    datos = []
    try:
        with open(ARCHIVO_CSV, "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # saltar encabezado

            for fila in lector:
                if len(fila) == 3:
                    nombre, cantidad, precio = fila
                    datos.append({
                        "nombre": nombre,
                        "cantidad": int(cantidad),
                        "precio": float(precio)
                    })
        print("\n[OK] Datos cargados desde Inventario.csv\n")
    except FileNotFoundError:
        print("\n[ADVERTENCIA] No existe Inventario.csv aún.\n")

    return datos


