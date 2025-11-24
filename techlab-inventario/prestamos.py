import csv
from datetime import datetime

def validar_formato_fecha(fecha_str):
    """
    Valida que una fecha tenga el formato YYYY-MM-DD.
    
    Parámetros:
        fecha_str: fecha en formato string (str)
    
    Retorno:
        tuple: (bool, str) - (True si es válida, mensaje de error)
    """
    if not fecha_str or not fecha_str.strip():
        return False, "La fecha no puede estar vacía."
    
    fecha_str = fecha_str.strip()
    
    try:
        # Intentar parsear la fecha
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, f"Formato de fecha inválido: '{fecha_str}'. Debe ser YYYY-MM-DD (ej: 2025-01-15)."

def cargar_prestamos(ruta="prestamos.csv"):
    """
    Carga los préstamos desde el archivo CSV.
    
    Parámetros:
        ruta: ruta del archivo CSV de préstamos (str)
    
    Retorno:
        list: lista de diccionarios con los préstamos
    """
    prestamos = []
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Validar que la fila no esté vacía
                if fila.get("prestamo_id", "").strip():
                    prestamos.append({
                        "prestamo_id": fila["prestamo_id"].strip(),
                        "equipo_id": fila["equipo_id"].strip(),
                        "nombre_equipo": fila["nombre_equipo"].strip(),
                        "usuario_prestatario": fila["usuario_prestatario"].strip(),
                        "tipo_usuario": fila["tipo_usuario"].strip(),
                        "fecha_solicitud": fila["fecha_solicitud"].strip(),
                        "fecha_prestamo": fila.get("fecha_prestamo", "").strip(),
                        "fecha_devolucion": fila.get("fecha_devolucion", "").strip(),
                        "dias_autorizados": int(fila["dias_autorizados"]) if fila.get("dias_autorizados", "").strip() else 0,
                        "dias_reales_usados": int(fila["dias_reales_usados"]) if fila.get("dias_reales_usados", "").strip() else 0,
                        "retraso": fila["retraso"].strip(),
                        "estado": fila["estado"].strip(),
                        "mes": fila.get("mes", "").strip(),
                        "anio": fila.get("anio", "").strip()
                    })
    except FileNotFoundError:
        # Si el archivo no existe, retornar lista vacía (es normal al inicio)
        return []
    except Exception as e:
        print(f"\n[ERROR] No se pudo cargar el archivo de préstamos: {str(e)}\n")
        return []
    
    return prestamos

# Límites de días por tipo de usuario
LIMITES_DIAS = {
    "ESTUDIANTE": 3,
    "INSTRUCTOR": 7,
    "ADMINISTRATIVO": 10
}

def validar_dias_por_tipo(tipo_usuario, dias_solicitados):
    """
    Valida que los días solicitados no excedan el límite del tipo de usuario.
    
    Parámetros:
        tipo_usuario: tipo de usuario (ESTUDIANTE, INSTRUCTOR, ADMINISTRATIVO) (str)
        dias_solicitados: días solicitados para el préstamo (int)
    
    Retorno:
        bool: True si los días son válidos, False en caso contrario
    """
    tipo_usuario = tipo_usuario.upper()
    
    if tipo_usuario not in LIMITES_DIAS:
        return False
    
    limite = LIMITES_DIAS[tipo_usuario]
    
    return dias_solicitados > 0 and dias_solicitados <= limite

def generar_prestamo_id(lista_prestamos):
    """
    Genera un ID único para un nuevo préstamo.
    
    Parámetros:
        lista_prestamos: lista de préstamos existentes (list)
    
    Retorno:
        str: ID único en formato P001, P002, etc.
    """
    if not lista_prestamos:
        return "P001"
    
    # Encontrar el número más alto
    numeros = []
    for prestamo in lista_prestamos:
        prestamo_id = prestamo.get("prestamo_id", "")
        if prestamo_id.startswith("P"):
            try:
                numero = int(prestamo_id[1:])
                numeros.append(numero)
            except ValueError:
                continue
    
    if numeros:
        siguiente_numero = max(numeros) + 1
    else:
        siguiente_numero = 1
    
    return f"P{siguiente_numero:03d}"

def verificar_equipo_disponible(lista_equipos, lista_prestamos, equipo_id):
    """
    Verifica si un equipo está disponible para préstamo.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        lista_prestamos: lista de diccionarios con los préstamos (list)
        equipo_id: ID del equipo a verificar (str)
    
    Retorno:
        tuple: (bool, str) - (True si disponible, mensaje)
    """
    # Buscar equipo
    equipo = None
    for eq in lista_equipos:
        if eq.get("equipo_id", "").upper() == equipo_id.upper():
            equipo = eq
            break
    
    if not equipo:
        return False, f"El equipo con ID '{equipo_id}' no existe."
    
    # Verificar estado
    if equipo.get("estado_actual", "") != "DISPONIBLE":
        return False, f"El equipo '{equipo['nombre_equipo']}' no está disponible. Estado actual: {equipo.get('estado_actual', 'DESCONOCIDO')}"
    
    # Verificar que no tenga préstamos activos (APROBADO sin devolución)
    for prestamo in lista_prestamos:
        if prestamo.get("equipo_id", "").upper() == equipo_id.upper():
            estado = prestamo.get("estado", "")
            fecha_devolucion = prestamo.get("fecha_devolucion", "").strip()
            if estado == "APROBADO" and not fecha_devolucion:
                return False, f"El equipo tiene un préstamo activo (Préstamo ID: {prestamo.get('prestamo_id', 'N/A')})"
    
    return True, "Equipo disponible"

def registrar_solicitud_prestamo(lista_prestamos, lista_equipos, equipo_id, usuario_prestatario, tipo_usuario, dias_solicitados, fecha_prestamo=None):
    """
    Registra una nueva solicitud de préstamo (estado PENDIENTE).
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        lista_equipos: lista de diccionarios con los equipos (list)
        equipo_id: ID del equipo a prestar (str)
        usuario_prestatario: nombre del usuario que solicita (str)
        tipo_usuario: tipo de usuario (ESTUDIANTE, INSTRUCTOR, ADMINISTRATIVO) (str)
        dias_solicitados: días solicitados para el préstamo (int)
        fecha_prestamo: fecha de préstamo en formato YYYY-MM-DD (str, opcional)
    
    Retorno:
        dict: diccionario del préstamo registrado, o None si hay error
    """
    # Validar que el usuario no esté vacío
    if not usuario_prestatario or not usuario_prestatario.strip():
        print("\n[ERROR] El nombre del usuario no puede estar vacío.\n")
        return None
    
    # Validar tipo de usuario
    tipo_usuario = tipo_usuario.upper()
    if tipo_usuario not in LIMITES_DIAS:
        print(f"\n[ERROR] Tipo de usuario inválido. Debe ser: ESTUDIANTE, INSTRUCTOR o ADMINISTRATIVO.\n")
        return None
    
    # Validar días
    if not validar_dias_por_tipo(tipo_usuario, dias_solicitados):
        limite = LIMITES_DIAS[tipo_usuario]
        print(f"\n[ERROR] Los días solicitados ({dias_solicitados}) exceden el límite para {tipo_usuario} (máximo {limite} días).\n")
        return None
    
    # Verificar que el equipo esté disponible
    disponible, mensaje = verificar_equipo_disponible(lista_equipos, lista_prestamos, equipo_id)
    if not disponible:
        print(f"\n[ERROR] {mensaje}\n")
        return None
    
    # Buscar información del equipo
    equipo = None
    for eq in lista_equipos:
        if eq.get("equipo_id", "").upper() == equipo_id.upper():
            equipo = eq
            break
    
    if not equipo:
        print(f"\n[ERROR] No se encontró el equipo con ID '{equipo_id}'.\n")
        return None
    
    # Generar ID único
    prestamo_id = generar_prestamo_id(lista_prestamos)
    
    # Fecha actual
    fecha_actual = datetime.now()
    fecha_solicitud = fecha_actual.strftime("%Y-%m-%d")
    
    # Validar y usar fecha de préstamo
    if fecha_prestamo:
        valida_fecha, mensaje_fecha = validar_formato_fecha(fecha_prestamo)
        if not valida_fecha:
            print(f"\n[ERROR] {mensaje_fecha}\n")
            return None
        fecha_prestamo_str = fecha_prestamo.strip()
    else:
        fecha_prestamo_str = fecha_solicitud
    
    # Extraer mes y año
    mes = fecha_actual.strftime("%m")
    anio = fecha_actual.strftime("%Y")
    
    # Crear diccionario del préstamo
    prestamo = {
        "prestamo_id": prestamo_id,
        "equipo_id": equipo_id.upper(),
        "nombre_equipo": equipo.get("nombre_equipo", ""),
        "usuario_prestatario": usuario_prestatario.strip(),
        "tipo_usuario": tipo_usuario,
        "fecha_solicitud": fecha_solicitud,
        "fecha_prestamo": fecha_prestamo_str,
        "fecha_devolucion": "",
        "dias_autorizados": dias_solicitados,
        "dias_reales_usados": 0,
        "retraso": "NO",
        "estado": "PENDIENTE",
        "mes": mes,
        "anio": anio
    }
    
    # Agregar a la lista
    lista_prestamos.append(prestamo)
    
    return prestamo

def guardar_prestamos_csv(lista_prestamos, ruta="prestamos.csv"):
    """
    Guarda la lista de préstamos en un archivo CSV.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        ruta: ruta del archivo CSV donde guardar (str)
    
    Retorno:
        bool: True si se guardó correctamente, False en caso contrario
    """
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campo_nombres = [
                "prestamo_id", "equipo_id", "nombre_equipo", "usuario_prestatario",
                "tipo_usuario", "fecha_solicitud", "fecha_prestamo", "fecha_devolucion",
                "dias_autorizados", "dias_reales_usados", "retraso", "estado", "mes", "anio"
            ]
            escritor = csv.DictWriter(archivo, fieldnames=campo_nombres)
            
            # Escribir encabezado
            escritor.writeheader()
            
            # Escribir préstamos
            for prestamo in lista_prestamos:
                # Convertir enteros a string para CSV
                prestamo_csv = prestamo.copy()
                prestamo_csv["dias_autorizados"] = str(prestamo.get("dias_autorizados", 0))
                prestamo_csv["dias_reales_usados"] = str(prestamo.get("dias_reales_usados", 0))
                escritor.writerow(prestamo_csv)
        
        return True
    
    except Exception as e:
        print(f"\n[ERROR] No se pudo guardar el archivo de préstamos: {str(e)}\n")
        return False

def listar_prestamos_pendientes(lista_prestamos):
    """
    Lista todos los préstamos con estado PENDIENTE.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
    
    Retorno:
        list: lista de préstamos pendientes
    """
    pendientes = [p for p in lista_prestamos if p.get("estado", "") == "PENDIENTE"]
    return pendientes

def buscar_prestamo(lista_prestamos, prestamo_id):
    """
    Busca un préstamo por su ID.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        prestamo_id: ID del préstamo a buscar (str)
    
    Retorno:
        dict: diccionario del préstamo si se encuentra, None en caso contrario
    """
    for prestamo in lista_prestamos:
        if prestamo.get("prestamo_id", "").upper() == prestamo_id.upper():
            return prestamo
    return None

def aprobar_prestamo(lista_prestamos, lista_equipos, prestamo_id):
    """
    Aprueba un préstamo pendiente.
    Cambia el estado del préstamo a APROBADO y el equipo a PRESTADO.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        lista_equipos: lista de diccionarios con los equipos (list)
        prestamo_id: ID del préstamo a aprobar (str)
    
    Retorno:
        bool: True si se aprobó correctamente, False en caso contrario
    """
    prestamo = buscar_prestamo(lista_prestamos, prestamo_id)
    
    if not prestamo:
        print(f"\n[ERROR] No se encontró un préstamo con ID '{prestamo_id}'.\n")
        return False
    
    if prestamo.get("estado", "") != "PENDIENTE":
        print(f"\n[ERROR] El préstamo con ID '{prestamo_id}' no está pendiente. Estado actual: {prestamo.get('estado', 'DESCONOCIDO')}\n")
        return False
    
    # Buscar el equipo
    equipo_id = prestamo.get("equipo_id", "")
    equipo = None
    for eq in lista_equipos:
        if eq.get("equipo_id", "").upper() == equipo_id.upper():
            equipo = eq
            break
    
    if not equipo:
        print(f"\n[ERROR] No se encontró el equipo con ID '{equipo_id}'.\n")
        return False
    
    # Verificar que el equipo esté disponible
    if equipo.get("estado_actual", "") != "DISPONIBLE":
        print(f"\n[ERROR] El equipo '{equipo.get('nombre_equipo', '')}' no está disponible. Estado actual: {equipo.get('estado_actual', 'DESCONOCIDO')}\n")
        return False
    
    # Actualizar préstamo
    prestamo["estado"] = "APROBADO"
    
    # Actualizar equipo
    equipo["estado_actual"] = "PRESTADO"
    
    return True

def rechazar_prestamo(lista_prestamos, prestamo_id):
    """
    Rechaza un préstamo pendiente.
    Cambia el estado del préstamo a RECHAZADO.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        prestamo_id: ID del préstamo a rechazar (str)
    
    Retorno:
        bool: True si se rechazó correctamente, False en caso contrario
    """
    prestamo = buscar_prestamo(lista_prestamos, prestamo_id)
    
    if not prestamo:
        print(f"\n[ERROR] No se encontró un préstamo con ID '{prestamo_id}'.\n")
        return False
    
    if prestamo.get("estado", "") != "PENDIENTE":
        print(f"\n[ERROR] El préstamo con ID '{prestamo_id}' no está pendiente. Estado actual: {prestamo.get('estado', 'DESCONOCIDO')}\n")
        return False
    
    # Actualizar préstamo
    prestamo["estado"] = "RECHAZADO"
    
    return True

def calcular_dias_diferencia(fecha_inicio, fecha_fin):
    """
    Calcula la diferencia en días entre dos fechas.
    
    Parámetros:
        fecha_inicio: fecha inicial en formato YYYY-MM-DD (str)
        fecha_fin: fecha final en formato YYYY-MM-DD (str)
    
    Retorno:
        tuple: (int, str) - (número de días de diferencia, mensaje de error)
    """
    # Validar formato de fecha_inicio
    valida_inicio, mensaje_inicio = validar_formato_fecha(fecha_inicio)
    if not valida_inicio:
        return 0, mensaje_inicio
    
    # Validar formato de fecha_fin
    valida_fin, mensaje_fin = validar_formato_fecha(fecha_fin)
    if not valida_fin:
        return 0, mensaje_fin
    
    try:
        fecha_i = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_f = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        # Verificar que fecha_fin no sea anterior a fecha_inicio
        if fecha_f < fecha_i:
            return 0, f"La fecha de devolución ({fecha_fin}) no puede ser anterior a la fecha de préstamo ({fecha_inicio})."
        
        diferencia = (fecha_f - fecha_i).days
        return max(0, diferencia), ""  # No permitir valores negativos
    except Exception as e:
        return 0, f"Error al calcular diferencia de fechas: {str(e)}"

def listar_prestamos_activos(lista_prestamos):
    """
    Lista todos los préstamos aprobados sin devolución.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
    
    Retorno:
        list: lista de préstamos activos (APROBADO sin fecha_devolucion)
    """
    activos = []
    for prestamo in lista_prestamos:
        estado = prestamo.get("estado", "")
        fecha_devolucion = prestamo.get("fecha_devolucion", "").strip()
        if estado == "APROBADO" and not fecha_devolucion:
            activos.append(prestamo)
    return activos

def registrar_devolucion(lista_prestamos, lista_equipos, prestamo_id, fecha_devolucion):
    """
    Registra la devolución de un equipo prestado.
    Calcula días reales usados y determina si hay retraso.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        lista_equipos: lista de diccionarios con los equipos (list)
        prestamo_id: ID del préstamo a devolver (str)
        fecha_devolucion: fecha de devolución en formato YYYY-MM-DD (str)
    
    Retorno:
        dict: diccionario con información de la devolución, o None si hay error
    """
    prestamo = buscar_prestamo(lista_prestamos, prestamo_id)
    
    if not prestamo:
        print(f"\n[ERROR] No se encontró un préstamo con ID '{prestamo_id}'.\n")
        return None
    
    estado = prestamo.get("estado", "")
    fecha_devolucion_actual = prestamo.get("fecha_devolucion", "").strip()
    
    if estado != "APROBADO":
        print(f"\n[ERROR] El préstamo con ID '{prestamo_id}' no está aprobado. Estado actual: {estado}\n")
        return None
    
    if fecha_devolucion_actual:
        print(f"\n[ERROR] El préstamo con ID '{prestamo_id}' ya tiene una fecha de devolución registrada.\n")
        return None
    
    # Validar formato de fecha de devolución
    valida_fecha, mensaje_fecha = validar_formato_fecha(fecha_devolucion)
    if not valida_fecha:
        print(f"\n[ERROR] {mensaje_fecha}\n")
        return None
    
    # Calcular días reales usados
    fecha_prestamo = prestamo.get("fecha_prestamo", "").strip()
    if not fecha_prestamo:
        print(f"\n[ERROR] El préstamo no tiene fecha de préstamo registrada.\n")
        return None
    
    dias_reales_usados, mensaje_error = calcular_dias_diferencia(fecha_prestamo, fecha_devolucion)
    
    if mensaje_error:
        print(f"\n[ERROR] {mensaje_error}\n")
        return None
    
    # Obtener días autorizados
    dias_autorizados = prestamo.get("dias_autorizados", 0)
    
    # Determinar si hay retraso
    retraso = "SI" if dias_reales_usados > dias_autorizados else "NO"
    
    # Actualizar préstamo
    prestamo["fecha_devolucion"] = fecha_devolucion
    prestamo["dias_reales_usados"] = dias_reales_usados
    prestamo["retraso"] = retraso
    prestamo["estado"] = "DEVUELTO"
    
    # Buscar y actualizar equipo
    equipo_id = prestamo.get("equipo_id", "")
    equipo = None
    for eq in lista_equipos:
        if eq.get("equipo_id", "").upper() == equipo_id.upper():
            equipo = eq
            break
    
    if equipo:
        equipo["estado_actual"] = "DISPONIBLE"
    else:
        print(f"\n[ADVERTENCIA] No se encontró el equipo con ID '{equipo_id}' para actualizar su estado.\n")
    
    # Retornar información de la devolución
    return {
        "prestamo_id": prestamo_id,
        "dias_reales_usados": dias_reales_usados,
        "dias_autorizados": dias_autorizados,
        "retraso": retraso
    }

def consultar_historial_equipo(lista_prestamos, equipo_id):
    """
    Consulta el historial de préstamos de un equipo específico.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        equipo_id: ID del equipo a consultar (str)
    
    Retorno:
        list: lista de préstamos relacionados con el equipo
    """
    historial = []
    for prestamo in lista_prestamos:
        if prestamo.get("equipo_id", "").upper() == equipo_id.upper():
            historial.append(prestamo)
    
    # Ordenar por fecha de solicitud (más reciente primero)
    historial.sort(key=lambda x: x.get("fecha_solicitud", ""), reverse=True)
    
    return historial

def consultar_historial_usuario(lista_prestamos, usuario_prestatario):
    """
    Consulta el historial de préstamos de un usuario específico.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        usuario_prestatario: nombre del usuario a consultar (str)
    
    Retorno:
        list: lista de préstamos del usuario
    """
    historial = []
    usuario_lower = usuario_prestatario.lower()
    for prestamo in lista_prestamos:
        if prestamo.get("usuario_prestatario", "").lower() == usuario_lower:
            historial.append(prestamo)
    
    # Ordenar por fecha de solicitud (más reciente primero)
    historial.sort(key=lambda x: x.get("fecha_solicitud", ""), reverse=True)
    
    return historial

