# TechLab Inventory Console – Gestión de Equipos Tecnológicos

## 📋 Descripción General

Este proyecto es un sistema de gestión de inventario y préstamos de equipos tecnológicos para el Laboratorio de Innovación Tecnológica (TechLab). Permite a los administradores gestionar equipos, aprobar préstamos a estudiantes/instructores/administrativos, y generar reportes.

---

## 👤 Datos del Desarrollador

*Nombre:* [Tu nombre aquí]  
*Fecha de desarrollo:* [Fecha]  
*Curso:* Programación - Semana [X]

---

## 📚 Plan de Desarrollo Paso a Paso

> **Nota:** Este plan está escrito como si fuera un cuaderno de trabajo, pensando paso a paso qué hacer antes de escribir código.

---

### 📝 FASE 1: ANÁLISIS Y PLANIFICACIÓN (En papel/cuaderno)

#### Paso 1.1: Entender el problema
**¿Qué necesito hacer?**
- Un sistema que gestione equipos tecnológicos (laptops, drones, tablets, etc.)
- Los equipos se pueden prestar a estudiantes, instructores o administrativos
- Cada tipo de usuario tiene límite de días diferente
- Debo llevar registro de quién pidió qué, cuándo y si devolvió a tiempo

**Preguntas clave que debo responder:**
- ¿Qué datos guardo? → Equipos, Usuarios, Préstamos
- ¿Dónde guardo los datos? → Archivos CSV
- ¿Quién puede usar el sistema? → Solo administrador (login)
- ¿Qué puede hacer el admin? → Ver menú con opciones

---

#### Paso 1.2: Identificar las "piezas" del programa
**Archivos CSV que necesito:**
1. `usuarios.csv` → Para login (solo ADMIN)
2. `equipos.csv` → Lista de equipos disponibles
3. `prestamos.csv` → Historial de préstamos

**Archivos Python que voy a crear:**
1. `main.py` → Inicio de sesión + menú principal
2. `usuarios.py` → Funciones para validar login
3. `equipos.py` → Funciones para gestionar equipos
4. `prestamos.py` → Funciones para gestionar préstamos
5. `reportes.py` → Funciones para exportar reportes CSV

**Estructura que voy a usar:**
- Listas de diccionarios en memoria (como el proyecto anterior)
- Funciones para leer/escribir CSV
- Funciones para validar reglas de negocio

---

#### Paso 1.3: Dibujar el flujo principal (en papel)
```
1. Programa inicia
   ↓
2. Mostrar pantalla de login
   ↓
3. Pedir usuario y contraseña
   ↓
4. Validar contra usuarios.csv
   ↓
5. ¿Es válido? → Ir al menú
   ¿No es válido? → Intentar de nuevo (máx 3 veces)
   ↓
6. Menú principal:
   - Gestión de equipos
   - Gestión de préstamos
   - Historial
   - Reportes
   - Salir
```

---

### 📝 FASE 2: ESTRUCTURA DE DATOS (Pensar antes de codificar)

#### Paso 2.1: Diseñar estructuras de datos
**Equipo (diccionario):**
```python
equipo = {
    "equipo_id": "EQ001",
    "nombre_equipo": "Laptop Dell XPS",
    "categoria": "laptops",
    "estado_actual": "DISPONIBLE",  # o "PRESTADO" o "MANTENIMIENTO"
    "fecha_registro": "2025-01-15",
    "descripcion": "Laptop para desarrollo"
}
```

**Préstamo (diccionario):**
```python
prestamo = {
    "prestamo_id": "P001",
    "equipo_id": "EQ001",
    "nombre_equipo": "Laptop Dell XPS",
    "usuario_prestatario": "Juan Pérez",
    "tipo_usuario": "ESTUDIANTE",  # o "INSTRUCTOR" o "ADMINISTRATIVO"
    "fecha_solicitud": "2025-01-20",
    "fecha_prestamo": "2025-01-21",
    "fecha_devolucion": "",  # Vacío si no se ha devuelto
    "dias_autorizados": 3,
    "dias_reales_usados": 0,
    "retraso": "NO",
    "estado": "PENDIENTE",  # o "APROBADO", "RECHAZADO", "DEVUELTO"
    "mes": "01",
    "anio": "2025"
}
```

**Límites por tipo de usuario:**
```python
LIMITES_DIAS = {
    "ESTUDIANTE": 3,
    "INSTRUCTOR": 7,
    "ADMINISTRATIVO": 10
}
```

---

### 📝 FASE 3: CREAR ARCHIVOS CSV INICIALES

#### Paso 3.1: Crear usuarios.csv
**Archivo inicial:**
```
usuario,contrasena,rol
admin,admin123,ADMIN
```

**Nota:** Este archivo lo creo manualmente primero.

---

#### Paso 3.2: Crear equipos.csv (vacío inicialmente)
**Estructura:**
```
equipo_id,nombre_equipo,categoria,estado_actual,fecha_registro,descripcion
```

**Nota:** Lo inicializo vacío, los equipos se agregarán desde el programa.

---

#### Paso 3.3: Crear prestamos.csv (vacío inicialmente)
**Estructura:**
```
prestamo_id,equipo_id,nombre_equipo,usuario_prestatario,tipo_usuario,fecha_solicitud,fecha_prestamo,fecha_devolucion,dias_autorizados,dias_reales_usados,retraso,estado,mes,anio
```

**Nota:** Lo inicializo vacío, los préstamos se crearán desde el programa.

---

### 📝 FASE 4: IMPLEMENTACIÓN PASO A PASO

#### 🎯 COMMIT 1: Estructura base y login
**Objetivo:** Hacer que el programa inicie y valide login

**Qué voy a hacer:**
1. Crear `usuarios.csv` con usuario admin
2. Crear `usuarios.py` con función `validar_login(usuario, contrasena)`
   - Lee usuarios.csv
   - Compara usuario y contraseña
   - Retorna True/False
3. Crear `main.py` básico:
   - Carga usuarios.csv
   - Pide usuario y contraseña
   - Valida con función de usuarios.py
   - Permite 3 intentos máximo
   - Si es válido → muestra mensaje "Login exitoso" y termina (por ahora)

**Prueba:** Ejecutar y probar login con credenciales correctas e incorrectas.

---

#### 🎯 COMMIT 2: Menú principal
**Objetivo:** Mostrar menú después del login

**Qué voy a hacer:**
1. En `main.py`, después de login exitoso:
   - Crear función `mostrar_menu()`
   - Mostrar opciones:
     1. Gestión de equipos
     2. Gestión de préstamos
     3. Historial
     4. Reportes
     5. Salir
   - Usar while True para mantener el programa activo
   - Capturar opción del usuario
   - Por ahora solo mostrar mensaje "Opción X seleccionada"

**Prueba:** Login exitoso debe mostrar el menú.

---

#### 🎯 COMMIT 3: Cargar datos al inicio
**Objetivo:** Leer CSV y cargar en memoria al iniciar

**Qué voy a hacer:**
1. Crear funciones en cada módulo para cargar CSV:
   - `usuarios.py`: `cargar_usuarios()` → retorna lista de usuarios
   - `equipos.py`: `cargar_equipos()` → retorna lista de equipos
   - `prestamos.py`: `cargar_prestamos()` → retorna lista de préstamos
2. En `main.py`, al iniciar (después de login):
   - Cargar equipos.csv en `lista_equipos = []`
   - Cargar prestamos.csv en `lista_prestamos = []`
   - Guardar como variables globales o pasar como parámetros

**Prueba:** Crear CSV de prueba con datos y verificar que se cargan correctamente.

---

#### 🎯 COMMIT 4: Gestión de equipos - Agregar equipo
**Objetivo:** Poder registrar un nuevo equipo

**Qué voy a hacer:**
1. Crear `equipos.py` con función `registrar_equipo(lista_equipos, datos)`
   - Generar equipo_id único (ej: "EQ001", "EQ002")
   - Validar que nombre no esté vacío
   - Estado inicial = "DISPONIBLE"
   - Fecha actual automática
   - Agregar a lista
2. Crear función `guardar_equipos_csv(lista_equipos, ruta)`
   - Escribe lista completa a equipos.csv
3. En `main.py`, opción 1 del menú:
   - Submenú "Gestión de Equipos"
   - Opción 1.1: Registrar equipo
   - Pedir datos al usuario
   - Llamar a registrar_equipo()
   - Guardar en CSV inmediatamente

**Prueba:** Agregar un equipo y verificar que aparece en equipos.csv.

---

#### 🎯 COMMIT 5: Gestión de equipos - Listar y consultar
**Objetivo:** Ver lista de equipos y buscar uno específico

**Qué voy a hacer:**
1. En `equipos.py`:
   - `listar_equipos(lista_equipos)` → muestra todos
   - `buscar_equipo(lista_equipos, equipo_id)` → retorna equipo o None
2. En `main.py`, opción 1:
   - 1.2: Listar equipos
   - 1.3: Consultar equipo por ID

**Prueba:** Listar equipos y buscar uno por ID.

---

#### 🎯 COMMIT 6: Gestión de préstamos - Registrar solicitud
**Objetivo:** Crear solicitud de préstamo (estado PENDIENTE)

**Qué voy a hacer:**
1. Crear `prestamos.py` con función `registrar_solicitud_prestamo(lista_prestamos, datos)`
   - Validar que equipo existe y está DISPONIBLE
   - Validar días solicitados según tipo de usuario
   - Generar prestamo_id único
   - Estado inicial = "PENDIENTE"
   - Fecha actual para fecha_solicitud
   - Calcular mes y año
2. Función `validar_dias_por_tipo(tipo_usuario, dias_solicitados)`
   - ESTUDIANTE: máx 3 días
   - INSTRUCTOR: máx 7 días
   - ADMINISTRATIVO: máx 10 días
   - Retorna True/False
3. En `main.py`, opción 2:
   - Submenú "Gestión de Préstamos"
   - Opción 2.1: Registrar solicitud
   - Pedir: equipo_id, nombre usuario, tipo usuario, días
   - Validar antes de crear
   - Guardar en prestamos.csv

**Prueba:** Crear solicitud válida y otra que exceda límite de días.

---

#### 🎯 COMMIT 7: Gestión de préstamos - Aprobar/Rechazar
**Objetivo:** Administrador puede aprobar o rechazar solicitudes pendientes

**Qué voy a hacer:**
1. En `prestamos.py`:
   - `listar_prestamos_pendientes(lista_prestamos)` → filtra por estado PENDIENTE
   - `aprobar_prestamo(lista_prestamos, prestamo_id)`:
     - Cambiar estado a "APROBADO"
     - Poner fecha_prestamo = fecha actual
     - Actualizar estado del equipo a "PRESTADO" (necesito lista_equipos)
   - `rechazar_prestamo(lista_prestamos, prestamo_id)`:
     - Cambiar estado a "RECHAZADO"
2. En `main.py`, opción 2:
   - 2.2: Aprobar/Rechazar préstamo
   - Mostrar lista de pendientes
   - Pedir prestamo_id
   - Preguntar Aprobar o Rechazar
   - Llamar función correspondiente
   - Guardar CSV

**Prueba:** Aprobar y rechazar préstamos pendientes.

---

#### 🎯 COMMIT 8: Gestión de préstamos - Registrar devolución
**Objetivo:** Registrar devolución y calcular retraso

**Qué voy a hacer:**
1. En `prestamos.py`:
   - `listar_prestamos_activos(lista_prestamos)` → filtra por estado APROBADO sin fecha_devolucion
   - `registrar_devolucion(lista_prestamos, prestamo_id, fecha_devolucion, lista_equipos)`:
     - Calcular días reales usados (fecha_devolucion - fecha_prestamo)
     - Comparar con días autorizados
     - Si días reales > días autorizados → retraso = "SI"
     - Cambiar estado a "DEVUELTO"
     - Actualizar estado del equipo a "DISPONIBLE"
2. Necesito función para calcular diferencia de días entre fechas
3. En `main.py`, opción 2:
   - 2.3: Registrar devolución
   - Mostrar préstamos activos
   - Pedir prestamo_id y fecha_devolucion
   - Llamar a registrar_devolucion()
   - Guardar CSV

**Prueba:** Devolver equipo a tiempo y otro con retraso.

---

#### 🎯 COMMIT 9: Historial
**Objetivo:** Consultar historial por equipo o por usuario

**Qué voy a hacer:**
1. En `prestamos.py`:
   - `consultar_historial_equipo(lista_prestamos, equipo_id)`
   - `consultar_historial_usuario(lista_prestamos, nombre_usuario)`
2. En `main.py`, opción 3:
   - Submenú historial
   - Por equipo o por usuario
   - Mostrar toda la información

**Prueba:** Consultar historial de diferentes equipos y usuarios.

---

#### 🎯 COMMIT 10: Exportar reporte CSV
**Objetivo:** Generar reporte CSV de préstamos por mes y año

**Qué voy a hacer:**
1. Crear `reportes.py` con función `exportar_reporte_mes_anio(lista_prestamos, mes, anio, ruta)`
   - Filtrar préstamos DEVUELTOS del mes y año especificado
   - Crear CSV con columnas requeridas
   - Nombre archivo: `reporte_prestamos_2025_03.csv`
2. En `main.py`, opción 4:
   - Pedir mes y año
   - Llamar a exportar_reporte()
   - Mostrar mensaje de éxito o "No hay datos"

**Prueba:** Generar reporte de un mes con datos y otro sin datos.

---

### 📝 FASE 5: VALIDACIONES Y MANEJO DE ERRORES

#### 🎯 COMMIT 11: Validaciones adicionales
**Objetivo:** Mejorar validaciones y mensajes de error

**Qué voy a hacer:**
- Validar formato de fechas (YYYY-MM-DD)
- Validar que equipos.csv existe antes de cargar
- Manejar errores al leer/escribir CSV con try/except
- Validar que no se dupliquen IDs
- Mensajes claros en todos los casos

---

### 📝 FASE 6: DOCUMENTACIÓN Y PRUEBAS FINALES

#### Paso 6.1: Completar README.md
- Agregar instrucciones de ejecución
- Explicar estructura de archivos
- Documentar reglas de préstamo

#### Paso 6.2: Crear diagrama de flujo
- Dibujar en draw.io el flujo de préstamo completo
- Exportar a PNG/PDF

#### Paso 6.3: Pruebas finales
- Probar todo el flujo completo
- Verificar que todos los CSV se actualizan correctamente
- Probar casos límite (equipo no existe, préstamo duplicado, etc.)

---

## 🚀 Cómo Ejecutar el Programa

1. Asegúrate de tener Python instalado (versión 3.7 o superior)
2. Coloca todos los archivos .py en la misma carpeta
3. Asegúrate de tener `usuarios.csv` con el usuario administrador
4. Ejecuta: `python main.py`
5. Inicia sesión con:
   - Usuario: `admin`
   - Contraseña: `admin123`

---

## 📁 Estructura del Proyecto

```
techlab-inventario/
│
├── main.py              # Punto de entrada: login + menú principal
├── usuarios.py          # Funciones para autenticación
├── equipos.py           # Funciones para gestión de equipos
├── prestamos.py         # Funciones para gestión de préstamos
├── reportes.py          # Funciones para generar reportes CSV
│
├── usuarios.csv         # Datos de usuarios (solo admin)
├── equipos.csv          # Catálogo de equipos
├── prestamos.csv        # Historial de préstamos
│
└── README.md            # Este archivo
```

---

## 📋 Archivos CSV Necesarios

### usuarios.csv
```csv
usuario,contrasena,rol
admin,admin123,ADMIN
```

### equipos.csv (estructura)
```csv
equipo_id,nombre_equipo,categoria,estado_actual,fecha_registro,descripcion
```

### prestamos.csv (estructura)
```csv
prestamo_id,equipo_id,nombre_equipo,usuario_prestatario,tipo_usuario,fecha_solicitud,fecha_prestamo,fecha_devolucion,dias_autorizados,dias_reales_usados,retraso,estado,mes,anio
```

---

## 📐 Reglas de Préstamo

### Límites de Días por Tipo de Usuario:
- **ESTUDIANTE:** Máximo 3 días
- **INSTRUCTOR:** Máximo 7 días
- **ADMINISTRATIVO:** Máximo 10 días

### Estados de Equipos:
- **DISPONIBLE:** El equipo puede ser prestado
- **PRESTADO:** El equipo está actualmente en préstamo
- **MANTENIMIENTO:** El equipo no está disponible

### Estados de Préstamos:
- **PENDIENTE:** Solicitud creada, esperando aprobación
- **APROBADO:** Préstamo autorizado, equipo entregado
- **RECHAZADO:** Solicitud denegada
- **DEVUELTO:** Equipo regresado al inventario

### Cálculo de Retraso:
- Si `dias_reales_usados > dias_autorizados` → `retraso = "SI"`
- Si `dias_reales_usados <= dias_autorizados` → `retraso = "NO"`

---

## ⚠️ Limitaciones

- Solo un usuario administrador (no se pueden registrar nuevos usuarios)
- Fechas en formato YYYY-MM-DD
- IDs generados secuencialmente (no se valida duplicados de forma automática)
- No hay persistencia de sesión (al cerrar el programa, se pierden datos no guardados en CSV)

---

## 🔮 Mejoras Futuras

- Sistema de múltiples usuarios con diferentes roles
- Búsqueda avanzada de equipos por categoría
- Notificaciones de equipos próximos a vencer
- Interfaz gráfica (GUI)
- Base de datos en lugar de CSV
- Sistema de multas por retrasos

---

## 📝 Notas para el Estudiante

**Recuerda:**
- Este proyecto se desarrolla commit por commit para aprender paso a paso
- Cada commit debe tener un objetivo claro y funcionar independientemente
- Prueba cada funcionalidad antes de pasar a la siguiente
- Si algo no funciona, vuelve al commit anterior y revisa qué cambió
- Los commits te permiten ver cómo se construyó el proyecto paso a paso

**Orden recomendado de aprendizaje:**
1. Primero entiende cómo funciona el login (Commit 1)
2. Luego entiende el menú (Commit 2)
3. Después aprende a cargar datos (Commit 3)
4. Y así sucesivamente...

¡Buena suerte con tu proyecto! 🚀

