import csv
from datetime import datetime

def exportar_reporte_mes_anio(lista_prestamos, mes, anio, ruta=None):
    """
    Exporta un reporte CSV de préstamos devueltos del mes y año especificados.
    
    Parámetros:
        lista_prestamos: lista de diccionarios con los préstamos (list)
        mes: mes a filtrar (formato MM) (str o int)
        anio: año a filtrar (formato YYYY) (str o int)
        ruta: ruta del archivo CSV donde guardar (str, opcional)
    
    Retorno:
        bool: True si se exportó correctamente, False en caso contrario
    """
    # Convertir mes y año a strings
    mes_str = str(mes).zfill(2)
    anio_str = str(anio)
    
    # Filtrar préstamos DEVUELTOS del mes y año especificados
    prestamos_filtrados = []
    for prestamo in lista_prestamos:
        estado = prestamo.get("estado", "")
        prestamo_mes = prestamo.get("mes", "").strip().zfill(2)
        prestamo_anio = prestamo.get("anio", "").strip()
        
        if estado == "DEVUELTO" and prestamo_mes == mes_str and prestamo_anio == anio_str:
            prestamos_filtrados.append(prestamo)
    
    if not prestamos_filtrados:
        print(f"\n[ADVERTENCIA] No hay préstamos devueltos para el mes {mes_str}/{anio_str}.\n")
        return False
    
    # Generar nombre de archivo si no se proporciona ruta
    if not ruta:
        ruta = f"reporte_prestamos_{anio_str}_{mes_str}.csv"
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campo_nombres = [
                "prestamo_id", "equipo_id", "nombre_equipo", "usuario_prestatario",
                "tipo_usuario", "dias_autorizados", "dias_reales_usados", "retraso",
                "estado", "mes", "anio"
            ]
            escritor = csv.DictWriter(archivo, fieldnames=campo_nombres)
            
            # Escribir encabezado
            escritor.writeheader()
            
            # Escribir préstamos filtrados
            for prestamo in prestamos_filtrados:
                prestamo_csv = {
                    "prestamo_id": prestamo.get("prestamo_id", ""),
                    "equipo_id": prestamo.get("equipo_id", ""),
                    "nombre_equipo": prestamo.get("nombre_equipo", ""),
                    "usuario_prestatario": prestamo.get("usuario_prestatario", ""),
                    "tipo_usuario": prestamo.get("tipo_usuario", ""),
                    "dias_autorizados": str(prestamo.get("dias_autorizados", 0)),
                    "dias_reales_usados": str(prestamo.get("dias_reales_usados", 0)),
                    "retraso": prestamo.get("retraso", "NO"),
                    "estado": prestamo.get("estado", ""),
                    "mes": prestamo.get("mes", ""),
                    "anio": prestamo.get("anio", "")
                }
                escritor.writerow(prestamo_csv)
        
        print(f"\n✓ Reporte exportado exitosamente: {ruta}")
        print(f"  Total de préstamos devueltos en {mes_str}/{anio_str}: {len(prestamos_filtrados)}\n")
        return True
    
    except Exception as e:
        print(f"\n[ERROR] No se pudo exportar el reporte: {str(e)}\n")
        return False

