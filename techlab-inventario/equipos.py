import csv
from datetime import datetime

def cargar_equipos(ruta="equipos.csv"):
    """
    Carga los equipos desde el archivo CSV.
    
    Parámetros:
        ruta: ruta del archivo CSV de equipos (str)
    
    Retorno:
        list: lista de diccionarios con los equipos
    """
    equipos = []
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Validar que la fila no esté vacía
                if fila.get("equipo_id", "").strip():
                    equipos.append({
                        "equipo_id": fila["equipo_id"].strip(),
                        "nombre_equipo": fila["nombre_equipo"].strip(),
                        "categoria": fila["categoria"].strip(),
                        "estado_actual": fila["estado_actual"].strip(),
                        "fecha_registro": fila["fecha_registro"].strip(),
                        "descripcion": fila.get("descripcion", "").strip()
                    })
    except FileNotFoundError:
        # Si el archivo no existe, retornar lista vacía (es normal al inicio)
        return []
    except Exception as e:
        print(f"\n[ERROR] No se pudo cargar el archivo de equipos: {str(e)}\n")
        return []
    
    return equipos

def generar_equipo_id(lista_equipos):
    """
    Genera un ID único para un nuevo equipo.
    
    Parámetros:
        lista_equipos: lista de equipos existentes (list)
    
    Retorno:
        str: ID único en formato EQ001, EQ002, etc.
    """
    if not lista_equipos:
        return "EQ001"
    
    # Encontrar el número más alto
    numeros = []
    for equipo in lista_equipos:
        equipo_id = equipo.get("equipo_id", "")
        if equipo_id.startswith("EQ"):
            try:
                numero = int(equipo_id[2:])
                numeros.append(numero)
            except ValueError:
                continue
    
    if numeros:
        siguiente_numero = max(numeros) + 1
    else:
        siguiente_numero = 1
    
    return f"EQ{siguiente_numero:03d}"

def registrar_equipo(lista_equipos, nombre_equipo, categoria, descripcion=""):
    """
    Registra un nuevo equipo en el inventario.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        nombre_equipo: nombre del equipo (str)
        categoria: categoría del equipo (str)
        descripcion: descripción opcional del equipo (str)
    
    Retorno:
        dict: diccionario del equipo registrado, o None si hay error
    """
    # Validar que el nombre no esté vacío
    if not nombre_equipo or not nombre_equipo.strip():
        print("\n[ERROR] El nombre del equipo no puede estar vacío.\n")
        return None
    
    # Validar que la categoría no esté vacía
    if not categoria or not categoria.strip():
        print("\n[ERROR] La categoría no puede estar vacía.\n")
        return None
    
    # Generar ID único
    equipo_id = generar_equipo_id(lista_equipos)
    
    # Obtener fecha actual en formato YYYY-MM-DD
    fecha_registro = datetime.now().strftime("%Y-%m-%d")
    
    # Crear diccionario del equipo
    equipo = {
        "equipo_id": equipo_id,
        "nombre_equipo": nombre_equipo.strip(),
        "categoria": categoria.strip(),
        "estado_actual": "DISPONIBLE",
        "fecha_registro": fecha_registro,
        "descripcion": descripcion.strip() if descripcion else ""
    }
    
    # Agregar a la lista
    lista_equipos.append(equipo)
    
    return equipo

def guardar_equipos_csv(lista_equipos, ruta="equipos.csv"):
    """
    Guarda la lista de equipos en un archivo CSV.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        ruta: ruta del archivo CSV donde guardar (str)
    
    Retorno:
        bool: True si se guardó correctamente, False en caso contrario
    """
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campo_nombres = ["equipo_id", "nombre_equipo", "categoria", "estado_actual", "fecha_registro", "descripcion"]
            escritor = csv.DictWriter(archivo, fieldnames=campo_nombres)
            
            # Escribir encabezado
            escritor.writeheader()
            
            # Escribir equipos
            for equipo in lista_equipos:
                escritor.writerow(equipo)
        
        return True
    
    except Exception as e:
        print(f"\n[ERROR] No se pudo guardar el archivo de equipos: {str(e)}\n")
        return False

def buscar_equipo(lista_equipos, equipo_id):
    """
    Busca un equipo por su ID.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        equipo_id: ID del equipo a buscar (str)
    
    Retorno:
        dict: diccionario del equipo si se encuentra, None en caso contrario
    """
    for equipo in lista_equipos:
        if equipo.get("equipo_id", "").upper() == equipo_id.upper():
            return equipo
    return None

def listar_equipos(lista_equipos):
    """
    Muestra todos los equipos del inventario.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
    
    Retorno:
        None
    """
    if not lista_equipos:
        print("\n[ADVERTENCIA] No hay equipos registrados en el inventario.\n")
        return
    
    print("\n" + "="*80)
    print("  LISTADO DE EQUIPOS")
    print("="*80)
    print(f"{'ID':<8} {'Nombre':<30} {'Categoría':<15} {'Estado':<15} {'Fecha Reg.'}")
    print("-"*80)
    
    for equipo in lista_equipos:
        print(f"{equipo['equipo_id']:<8} {equipo['nombre_equipo']:<30} {equipo['categoria']:<15} {equipo['estado_actual']:<15} {equipo['fecha_registro']}")
    
    print("="*80 + "\n")

