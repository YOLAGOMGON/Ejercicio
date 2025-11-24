from usuarios import validar_login
from equipos import cargar_equipos, registrar_equipo, guardar_equipos_csv, listar_equipos, buscar_equipo
from prestamos import (
    cargar_prestamos, registrar_solicitud_prestamo, guardar_prestamos_csv, LIMITES_DIAS,
    listar_prestamos_pendientes, buscar_prestamo, aprobar_prestamo, rechazar_prestamo,
    listar_prestamos_activos, registrar_devolucion, consultar_historial_equipo, consultar_historial_usuario
)
from reportes import exportar_reporte_mes_anio

def main():
    """
    Función principal del programa.
    Maneja el inicio de sesión y el flujo principal.
    """
    print("\n" + "="*60)
    print("  TECH LAB - Sistema de Gestión de Inventario")
    print("="*60)
    print("\nInicio de sesión requerido")
    print("-"*60)
    
    # Intentos de login
    intentos_maximos = 3
    intentos = 0
    login_exitoso = False
    
    while intentos < intentos_maximos and not login_exitoso:
        usuario = input("\nUsuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        
        if validar_login(usuario, contrasena):
            login_exitoso = True
            print("\n" + "="*60)
            print("  ✓ Login exitoso. Bienvenido al sistema.")
            print("="*60)
        else:
            intentos += 1
            intentos_restantes = intentos_maximos - intentos
            
            if intentos_restantes > 0:
                print(f"\n[ERROR] Credenciales incorrectas.")
                print(f"Intentos restantes: {intentos_restantes}")
            else:
                print("\n[ERROR] Credenciales incorrectas.")
                print("\n[ADVERTENCIA] Máximo de intentos alcanzado.")
                print("El programa se cerrará.")
                return
    
    if login_exitoso:
        # Cargar datos desde CSV
        lista_equipos = cargar_equipos()
        lista_prestamos = cargar_prestamos()
        
        print(f"\n[Datos cargados] Equipos: {len(lista_equipos)}, Préstamos: {len(lista_prestamos)}")
        
        mostrar_menu(lista_equipos, lista_prestamos)

def mostrar_menu(lista_equipos, lista_prestamos):
    """
    Muestra el menú principal del sistema.
    Permite navegar por las diferentes opciones del sistema.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos
        lista_prestamos: lista de diccionarios con los préstamos
    """
    while True:
        print("\n" + "="*60)
        print("  MENÚ PRINCIPAL")
        print("="*60)
        print("1. Gestión de equipos")
        print("2. Gestión de préstamos")
        print("3. Historial")
        print("4. Reportes")
        print("5. Salir")
        print("="*60)
        
        try:
            opcion = input("\nSeleccione una opción (1-5): ").strip()
            
            if opcion == "1":
                menu_equipos(lista_equipos, lista_prestamos)
            elif opcion == "2":
                menu_prestamos(lista_equipos, lista_prestamos)
            elif opcion == "3":
                menu_historial(lista_equipos, lista_prestamos)
            elif opcion == "4":
                menu_reportes(lista_prestamos)
            elif opcion == "5":
                print("\nSaliendo del sistema...")
                print("¡Hasta luego!")
                break
            else:
                print("\n[ERROR] Opción inválida. Por favor seleccione una opción del 1 al 5.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"\n[ERROR] Ocurrió un error: {str(e)}")
            print("Por favor intente nuevamente.")

def menu_equipos(lista_equipos, lista_prestamos):
    """
    Menú de gestión de equipos.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        lista_prestamos: lista de diccionarios con los préstamos (list)
    """
    while True:
        print("\n" + "="*60)
        print("  GESTIÓN DE EQUIPOS")
        print("="*60)
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Consultar equipo")
        print("4. Volver al menú principal")
        print("="*60)
        
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                # Registrar equipo
                print("\n" + "-"*60)
                print("  REGISTRAR NUEVO EQUIPO")
                print("-"*60)
                
                nombre = input("\nNombre del equipo: ").strip()
                categoria = input("Categoría (laptops, drones, tablets, cámaras, herramientas, etc.): ").strip()
                descripcion = input("Descripción (opcional, Enter para omitir): ").strip()
                
                equipo = registrar_equipo(lista_equipos, nombre, categoria, descripcion)
                
                if equipo:
                    # Guardar inmediatamente en CSV
                    if guardar_equipos_csv(lista_equipos):
                        print(f"\n✓ Equipo '{equipo['nombre_equipo']}' registrado exitosamente con ID: {equipo['equipo_id']}")
                        print("✓ Datos guardados en equipos.csv\n")
                    else:
                        print("\n[ERROR] El equipo se registró pero no se pudo guardar en el archivo CSV.\n")
                
            elif opcion == "2":
                # Listar equipos
                listar_equipos(lista_equipos)
            
            elif opcion == "3":
                # Consultar equipo por ID
                if not lista_equipos:
                    print("\n[ADVERTENCIA] No hay equipos registrados.\n")
                    continue
                
                equipo_id = input("\nIngrese el ID del equipo a consultar (ej: EQ001): ").strip()
                equipo = buscar_equipo(lista_equipos, equipo_id)
                
                if equipo:
                    print("\n" + "="*60)
                    print("  INFORMACIÓN DEL EQUIPO")
                    print("="*60)
                    print(f"ID: {equipo['equipo_id']}")
                    print(f"Nombre: {equipo['nombre_equipo']}")
                    print(f"Categoría: {equipo['categoria']}")
                    print(f"Estado: {equipo['estado_actual']}")
                    print(f"Fecha de registro: {equipo['fecha_registro']}")
                    if equipo['descripcion']:
                        print(f"Descripción: {equipo['descripcion']}")
                    print("="*60 + "\n")
                else:
                    print(f"\n[ERROR] No se encontró un equipo con ID '{equipo_id}'.\n")
            
            elif opcion == "4":
                # Volver al menú principal
                break
            
            else:
                print("\n[ERROR] Opción inválida. Por favor seleccione una opción del 1 al 4.")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada. Volviendo al menú principal...")
            break
        except Exception as e:
            print(f"\n[ERROR] Ocurrió un error: {str(e)}")
            print("Por favor intente nuevamente.")

def menu_prestamos(lista_equipos, lista_prestamos):
    """
    Menú de gestión de préstamos.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        lista_prestamos: lista de diccionarios con los préstamos (list)
    """
    while True:
        print("\n" + "="*60)
        print("  GESTIÓN DE PRÉSTAMOS")
        print("="*60)
        print("1. Registrar solicitud de préstamo")
        print("2. Aprobar/Rechazar préstamo")
        print("3. Registrar devolución")
        print("4. Volver al menú principal")
        print("="*60)
        
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                # Registrar solicitud de préstamo
                print("\n" + "-"*60)
                print("  REGISTRAR SOLICITUD DE PRÉSTAMO")
                print("-"*60)
                
                if not lista_equipos:
                    print("\n[ADVERTENCIA] No hay equipos registrados.\n")
                    continue
                
                # Mostrar límites por tipo de usuario
                print("\nLímites de préstamo por tipo de usuario:")
                for tipo, limite in LIMITES_DIAS.items():
                    print(f"  - {tipo}: {limite} días máximo")
                
                equipo_id = input("\nID del equipo a prestar (ej: EQ001): ").strip()
                usuario = input("Nombre del usuario prestatario: ").strip()
                
                print("\nTipos de usuario disponibles:")
                print("  1. ESTUDIANTE")
                print("  2. INSTRUCTOR")
                print("  3. ADMINISTRATIVO")
                tipo_opcion = input("Seleccione tipo de usuario (1-3): ").strip()
                
                tipo_usuario_map = {
                    "1": "ESTUDIANTE",
                    "2": "INSTRUCTOR",
                    "3": "ADMINISTRATIVO"
                }
                
                tipo_usuario = tipo_usuario_map.get(tipo_opcion)
                if not tipo_usuario:
                    print("\n[ERROR] Opción de tipo de usuario inválida.\n")
                    continue
                
                try:
                    dias = int(input(f"Días solicitados (máximo {LIMITES_DIAS[tipo_usuario]}): "))
                except ValueError:
                    print("\n[ERROR] Por favor ingrese un número válido.\n")
                    continue
                
                fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD, Enter para hoy): ").strip()
                if fecha_prestamo:
                    # Validar formato básico
                    from prestamos import validar_formato_fecha
                    valida, mensaje = validar_formato_fecha(fecha_prestamo)
                    if not valida:
                        print(f"\n[ERROR] {mensaje}\n")
                        continue
                else:
                    fecha_prestamo = None
                
                prestamo = registrar_solicitud_prestamo(
                    lista_prestamos, lista_equipos, equipo_id,
                    usuario, tipo_usuario, dias, fecha_prestamo
                )
                
                if prestamo:
                    # Guardar inmediatamente en CSV
                    if guardar_prestamos_csv(lista_prestamos):
                        print(f"\n✓ Solicitud de préstamo registrada exitosamente con ID: {prestamo['prestamo_id']}")
                        print(f"  Equipo: {prestamo['nombre_equipo']}")
                        print(f"  Usuario: {prestamo['usuario_prestatario']}")
                        print(f"  Estado: {prestamo['estado']}")
                        print("✓ Datos guardados en prestamos.csv\n")
                    else:
                        print("\n[ERROR] El préstamo se registró pero no se pudo guardar en el archivo CSV.\n")
            
            elif opcion == "2":
                # Aprobar/Rechazar préstamo
                print("\n" + "-"*60)
                print("  APROBAR/RECHAZAR PRÉSTAMO")
                print("-"*60)
                
                pendientes = listar_prestamos_pendientes(lista_prestamos)
                
                if not pendientes:
                    print("\n[ADVERTENCIA] No hay préstamos pendientes.\n")
                    continue
                
                print("\nPréstamos pendientes:")
                print("-"*60)
                print(f"{'ID':<8} {'Equipo':<25} {'Usuario':<20} {'Días':<6} {'Fecha Sol.'}")
                print("-"*60)
                for prestamo in pendientes:
                    print(f"{prestamo['prestamo_id']:<8} {prestamo['nombre_equipo'][:25]:<25} {prestamo['usuario_prestatario'][:20]:<20} {prestamo['dias_autorizados']:<6} {prestamo['fecha_solicitud']}")
                print("-"*60)
                
                prestamo_id = input("\nID del préstamo a procesar (ej: P001): ").strip()
                prestamo = buscar_prestamo(lista_prestamos, prestamo_id)
                
                if not prestamo:
                    print(f"\n[ERROR] No se encontró un préstamo con ID '{prestamo_id}'.\n")
                    continue
                
                if prestamo.get("estado", "") != "PENDIENTE":
                    print(f"\n[ERROR] El préstamo con ID '{prestamo_id}' no está pendiente.\n")
                    continue
                
                # Mostrar información del préstamo
                print(f"\nPréstamo ID: {prestamo['prestamo_id']}")
                print(f"Equipo: {prestamo['nombre_equipo']}")
                print(f"Usuario: {prestamo['usuario_prestatario']} ({prestamo['tipo_usuario']})")
                print(f"Días autorizados: {prestamo['dias_autorizados']}")
                print(f"Fecha solicitud: {prestamo['fecha_solicitud']}")
                
                accion = input("\n¿Aprobar (A) o Rechazar (R)? ").strip().upper()
                
                if accion == "A":
                    # Aprobar
                    if aprobar_prestamo(lista_prestamos, lista_equipos, prestamo_id):
                        # Guardar cambios en ambos CSV
                        if guardar_prestamos_csv(lista_prestamos) and guardar_equipos_csv(lista_equipos):
                            print(f"\n✓ Préstamo {prestamo_id} aprobado exitosamente.")
                            print(f"✓ Estado del equipo '{prestamo['nombre_equipo']}' actualizado a PRESTADO.")
                            print("✓ Datos guardados en prestamos.csv y equipos.csv\n")
                        else:
                            print("\n[ERROR] El préstamo se aprobó pero no se pudo guardar en los archivos CSV.\n")
                    else:
                        print(f"\n[ERROR] No se pudo aprobar el préstamo {prestamo_id}.\n")
                
                elif accion == "R":
                    # Rechazar
                    if rechazar_prestamo(lista_prestamos, prestamo_id):
                        # Guardar cambios en CSV
                        if guardar_prestamos_csv(lista_prestamos):
                            print(f"\n✓ Préstamo {prestamo_id} rechazado exitosamente.")
                            print("✓ Datos guardados en prestamos.csv\n")
                        else:
                            print("\n[ERROR] El préstamo se rechazó pero no se pudo guardar en el archivo CSV.\n")
                    else:
                        print(f"\n[ERROR] No se pudo rechazar el préstamo {prestamo_id}.\n")
                
                else:
                    print("\n[ERROR] Opción inválida. Debe ser 'A' para aprobar o 'R' para rechazar.\n")
            
            elif opcion == "3":
                # Registrar devolución
                print("\n" + "-"*60)
                print("  REGISTRAR DEVOLUCIÓN DE EQUIPO")
                print("-"*60)
                
                activos = listar_prestamos_activos(lista_prestamos)
                
                if not activos:
                    print("\n[ADVERTENCIA] No hay préstamos activos para devolver.\n")
                    continue
                
                print("\nPréstamos activos (pendientes de devolución):")
                print("-"*60)
                print(f"{'ID':<8} {'Equipo':<25} {'Usuario':<20} {'Días Aut.':<10} {'Fecha Préstamo'}")
                print("-"*60)
                for prestamo in activos:
                    print(f"{prestamo['prestamo_id']:<8} {prestamo['nombre_equipo'][:25]:<25} {prestamo['usuario_prestatario'][:20]:<20} {prestamo['dias_autorizados']:<10} {prestamo['fecha_prestamo']}")
                print("-"*60)
                
                prestamo_id = input("\nID del préstamo a devolver (ej: P001): ").strip()
                fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD, Enter para hoy): ").strip()
                
                if not fecha_devolucion:
                    from datetime import datetime
                    fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
                else:
                    # Validar formato antes de continuar
                    from prestamos import validar_formato_fecha
                    valida, mensaje = validar_formato_fecha(fecha_devolucion)
                    if not valida:
                        print(f"\n[ERROR] {mensaje}\n")
                        continue
                
                resultado = registrar_devolucion(lista_prestamos, lista_equipos, prestamo_id, fecha_devolucion)
                
                if resultado:
                    # Guardar cambios en ambos CSV
                    if guardar_prestamos_csv(lista_prestamos) and guardar_equipos_csv(lista_equipos):
                        print(f"\n✓ Devolución registrada exitosamente para el préstamo {prestamo_id}.")
                        print(f"  Días autorizados: {resultado['dias_autorizados']}")
                        print(f"  Días reales usados: {resultado['dias_reales_usados']}")
                        print(f"  Retraso: {resultado['retraso']}")
                        print(f"✓ Estado del préstamo actualizado a DEVUELTO.")
                        print(f"✓ Estado del equipo actualizado a DISPONIBLE.")
                        print("✓ Datos guardados en prestamos.csv y equipos.csv\n")
                    else:
                        print("\n[ERROR] La devolución se registró pero no se pudo guardar en los archivos CSV.\n")
                else:
                    print(f"\n[ERROR] No se pudo registrar la devolución del préstamo {prestamo_id}.\n")
            
            elif opcion == "4":
                # Volver al menú principal
                break
            
            else:
                print("\n[ERROR] Opción inválida. Por favor seleccione una opción del 1 al 4.")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada. Volviendo al menú principal...")
            break
        except Exception as e:
            print(f"\n[ERROR] Ocurrió un error: {str(e)}")
            print("Por favor intente nuevamente.")

def menu_historial(lista_equipos, lista_prestamos):
    """
    Menú de consulta de historial.
    
    Parámetros:
        lista_equipos: lista de diccionarios con los equipos (list)
        lista_prestamos: lista de diccionarios con los préstamos (list)
    """
    while True:
        print("\n" + "="*60)
        print("  CONSULTAR HISTORIAL")
        print("="*60)
        print("1. Historial por equipo")
        print("2. Historial por usuario")
        print("3. Volver al menú principal")
        print("="*60)
        
        try:
            opcion = input("\nSeleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                # Historial por equipo
                print("\n" + "-"*60)
                print("  HISTORIAL POR EQUIPO")
                print("-"*60)
                
                if not lista_equipos:
                    print("\n[ADVERTENCIA] No hay equipos registrados.\n")
                    continue
                
                equipo_id = input("\nID del equipo a consultar (ej: EQ001): ").strip()
                
                # Verificar que el equipo existe
                equipo = buscar_equipo(lista_equipos, equipo_id)
                if not equipo:
                    print(f"\n[ERROR] No se encontró un equipo con ID '{equipo_id}'.\n")
                    continue
                
                historial = consultar_historial_equipo(lista_prestamos, equipo_id)
                
                if not historial:
                    print(f"\n[ADVERTENCIA] El equipo '{equipo['nombre_equipo']}' no tiene historial de préstamos.\n")
                    continue
                
                print(f"\nHistorial de préstamos del equipo '{equipo['nombre_equipo']}' (ID: {equipo_id}):")
                print("="*80)
                print(f"{'ID Préstamo':<12} {'Usuario':<20} {'Tipo':<12} {'Estado':<12} {'F. Solicitud':<12} {'F. Préstamo':<12} {'Días':<6} {'Retraso':<8}")
                print("-"*80)
                
                for prestamo in historial:
                    fecha_prestamo = prestamo.get("fecha_prestamo", "N/A")[:12]
                    dias_aut = prestamo.get("dias_autorizados", 0)
                    retraso = prestamo.get("retraso", "N/A")
                    
                    print(f"{prestamo['prestamo_id']:<12} {prestamo['usuario_prestatario'][:20]:<20} {prestamo['tipo_usuario'][:12]:<12} {prestamo['estado'][:12]:<12} {prestamo['fecha_solicitud']:<12} {fecha_prestamo:<12} {dias_aut:<6} {retraso:<8}")
                
                print("="*80 + "\n")
            
            elif opcion == "2":
                # Historial por usuario
                print("\n" + "-"*60)
                print("  HISTORIAL POR USUARIO")
                print("-"*60)
                
                if not lista_prestamos:
                    print("\n[ADVERTENCIA] No hay préstamos registrados.\n")
                    continue
                
                usuario = input("\nNombre del usuario a consultar: ").strip()
                
                historial = consultar_historial_usuario(lista_prestamos, usuario)
                
                if not historial:
                    print(f"\n[ADVERTENCIA] El usuario '{usuario}' no tiene historial de préstamos.\n")
                    continue
                
                print(f"\nHistorial de préstamos del usuario '{usuario}':")
                print("="*80)
                print(f"{'ID Préstamo':<12} {'Equipo':<25} {'Tipo':<12} {'Estado':<12} {'F. Solicitud':<12} {'Días Aut.':<10} {'Retraso':<8}")
                print("-"*80)
                
                for prestamo in historial:
                    print(f"{prestamo['prestamo_id']:<12} {prestamo['nombre_equipo'][:25]:<25} {prestamo['tipo_usuario'][:12]:<12} {prestamo['estado'][:12]:<12} {prestamo['fecha_solicitud']:<12} {prestamo['dias_autorizados']:<10} {prestamo.get('retraso', 'N/A'):<8}")
                
                print("="*80 + "\n")
            
            elif opcion == "3":
                # Volver al menú principal
                break
            
            else:
                print("\n[ERROR] Opción inválida. Por favor seleccione una opción del 1 al 3.")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada. Volviendo al menú principal...")
            break
        except Exception as e:
            print(f"\n[ERROR] Ocurrió un error: {str(e)}")
            print("Por favor intente nuevamente.")

def menu_reportes(lista_prestamos):
    """
    Menú de exportación de reportes.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
    """
    while True:
        print("\n" + "="*60)
        print("  EXPORTAR REPORTE CSV")
        print("="*60)
        print("1. Generar reporte por mes y año")
        print("2. Volver al menú principal")
        print("="*60)
        
        try:
            opcion = input("\nSeleccione una opción (1-2): ").strip()
            
            if opcion == "1":
                # Exportar reporte por mes y año
                print("\n" + "-"*60)
                print("  GENERAR REPORTE POR MES Y AÑO")
                print("-"*60)
                
                if not lista_prestamos:
                    print("\n[ADVERTENCIA] No hay préstamos registrados.\n")
                    continue
                
                try:
                    anio = input("Año (YYYY): ").strip()
                    mes = input("Mes (MM): ").strip()
                    
                    if not anio or not mes:
                        print("\n[ERROR] Debe ingresar año y mes.\n")
                        continue
                    
                    # Validar formato
                    anio_int = int(anio)
                    mes_int = int(mes)
                    
                    if mes_int < 1 or mes_int > 12:
                        print("\n[ERROR] El mes debe estar entre 1 y 12.\n")
                        continue
                    
                    if anio_int < 2000 or anio_int > 2100:
                        print("\n[ERROR] El año debe ser un valor razonable (2000-2100).\n")
                        continue
                    
                    # Exportar reporte
                    exportar_reporte_mes_anio(lista_prestamos, mes_int, anio_int)
                
                except ValueError:
                    print("\n[ERROR] Por favor ingrese valores numéricos válidos para mes y año.\n")
                except Exception as e:
                    print(f"\n[ERROR] Ocurrió un error: {str(e)}\n")
            
            elif opcion == "2":
                # Volver al menú principal
                break
            
            else:
                print("\n[ERROR] Opción inválida. Por favor seleccione una opción del 1 al 2.")
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada. Volviendo al menú principal...")
            break
        except Exception as e:
            print(f"\n[ERROR] Ocurrió un error: {str(e)}")
            print("Por favor intente nuevamente.")

if __name__ == "__main__":
    main()

