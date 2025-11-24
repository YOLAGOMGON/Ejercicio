import csv

def cargar_usuarios(ruta="usuarios.csv"):
    """
    Carga los usuarios desde el archivo CSV.
    
    Parámetros:
        ruta: ruta del archivo CSV de usuarios (str)
    
    Retorno:
        list: lista de diccionarios con los usuarios
    """
    usuarios = []
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append({
                    "usuario": fila["usuario"].strip(),
                    "contrasena": fila["contrasena"].strip(),
                    "rol": fila["rol"].strip()
                })
    except FileNotFoundError:
        print(f"\n[ERROR] El archivo '{ruta}' no existe.\n")
    except Exception as e:
        print(f"\n[ERROR] No se pudo cargar el archivo de usuarios: {str(e)}\n")
    
    return usuarios

def validar_login(usuario, contrasena, ruta="usuarios.csv"):
    """
    Valida las credenciales de un usuario contra el archivo CSV.
    
    Parámetros:
        usuario: nombre de usuario (str)
        contrasena: contraseña del usuario (str)
        ruta: ruta del archivo CSV de usuarios (str)
    
    Retorno:
        bool: True si las credenciales son válidas, False en caso contrario
    """
    usuarios = cargar_usuarios(ruta)
    
    for u in usuarios:
        if u["usuario"].lower() == usuario.lower() and u["contrasena"] == contrasena:
            return True
    
    return False

