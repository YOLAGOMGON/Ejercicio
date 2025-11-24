# 📚 Guía de Aprendizaje - Cómo Recrear Este Proyecto

## 🎯 Método Recomendado para Aprendices

Esta guía te ayudará a entender el proyecto paso a paso, como si lo estuvieras creando por primera vez.

---

## 🛠️ COMANDOS ÚTILES DE GIT (Guía Rápida)

### Ver el historial de commits
```bash
cd techlab-inventario
git log --oneline
```
**Resultado:** Lista todos los commits con números y mensajes

---

### Ver un commit específico completo
```bash
git show 775173e
```
**Resultado:** Muestra TODOS los cambios de ese commit (qué se agregó, qué se eliminó)

**Nota:** Reemplaza `775173e` con el número del commit que quieras ver

---

### Ver el código completo de un commit
```bash
git checkout 775173e
```
**Resultado:** Cambia todos los archivos al estado de ese commit. ¡Puedes ejecutar el programa y ver cómo funcionaba en ese momento!

**⚠️ IMPORTANTE:** Después de ver el commit, vuelve al estado actual:
```bash
git checkout master
```

---

### Comparar dos commits (ver diferencias)
```bash
git diff 775173e f7b3532
```
**Resultado:** Muestra qué cambió entre el commit 1 y el commit 2

---

### Ver todos los commits en una línea con fecha
```bash
git log --oneline --graph --all
```
**Resultado:** Muestra el historial completo de forma visual

---

### Ver qué archivos cambiaron en un commit
```bash
git show --stat 775173e
```
**Resultado:** Muestra solo los nombres de archivos que cambiaron, sin el código

---

### Navegar por commits (como un libro)
```bash
# Ver el siguiente commit
git log --oneline | head -1  # Primer commit (más antiguo)
git log --oneline | tail -1  # Último commit (más reciente)

# Ir al commit anterior al actual
git checkout HEAD~1

# Ir al commit anterior a ese
git checkout HEAD~2

# Volver al más reciente (master)
git checkout master
```

---

### Números de commits importantes

Para referencia rápida, estos son los números de los commits principales:

- `a9b04cc` - Plan de desarrollo (documentación inicial)
- `775173e` - COMMIT 1 - Estructura base y login
- `f7b3532` - COMMIT 2 - Menú principal
- `0a84fbe` - COMMIT 3 - Cargar datos al inicio
- `0de3269` - COMMIT 4 - Gestión equipos - Agregar
- `48fe040` - COMMIT 5 - Gestión equipos - Listar y consultar
- `8d67365` - COMMIT 6 - Gestión préstamos - Registrar solicitud
- `9c32532` - COMMIT 7 - Gestión préstamos - Aprobar/Rechazar
- `1ec859e` - COMMIT 8 - Gestión préstamos - Registrar devolución
- `d4f4fa5` - COMMIT 9 - Historial
- `ef3b2cc` - COMMIT 10 - Exportar reporte CSV
- `66354e6` - COMMIT 11 - Validaciones y manejo de errores

**💡 Tip:** Para ver los números actuales en tu repositorio, usa:
```bash
git log --oneline
```

---

---

## 📋 PASO 1: Preparación (30 minutos)

### 1.1 Leer el PLAN_PASO_A_PASO.txt
**¿Por qué?** Para entender el "qué" antes del "cómo"

**Qué hacer:**
- Abre `PLAN_PASO_A_PASO.txt`
- Lee las secciones FASE 1, FASE 2 y FASE 3
- **NO leas aún las fases de implementación (COMMIT 1, 2, etc.)**
- Solo entiende:
  - ¿Qué problema resuelve el programa?
  - ¿Qué archivos necesito?
  - ¿Qué datos guardo?

**Preguntas que debes responder:**
- ✅ ¿Qué hace este sistema?
- ✅ ¿Qué son los equipos y préstamos?
- ✅ ¿Qué archivos CSV necesito?
- ✅ ¿Cómo funciona el login?

---

## 📋 PASO 2: Estudiar COMMIT 1 (45 minutos)

### 2.1 Ver qué hace COMMIT 1
```bash
cd techlab-inventario
git log --oneline
git show 775173e  # Ver COMMIT 1 completo
```

### 2.2 Leer el plan de COMMIT 1 en PLAN_PASO_A_PASO.txt
Busca la sección "COMMIT 1: Estructura base y login"

**Lee:**
- Qué hace este commit
- Qué archivos crea
- Qué funciones implementa

### 3.3 Ver el código del COMMIT 1
```bash
git checkout 775173e
```

**Ahora tienes el código completo del COMMIT 1**

**Qué hacer:**
1. Abre `usuarios.py` y lee cada línea
2. Abre `main.py` y lee cada línea
3. **Pregúntate:**
   - ¿Qué hace cada función?
   - ¿Por qué está ahí ese código?
   - ¿Cómo funciona el login?

### 3.4 Probar el COMMIT 1
```bash
python main.py
```

**Prueba:**
- Login correcto: `admin` / `admin123`
- Login incorrecto: credenciales falsas
- 3 intentos fallidos

**Pregúntate:**
- ¿Por qué solo permite 3 intentos?
- ¿Cómo valida las credenciales?

---

## 📋 PASO 3: Recrear COMMIT 1 (1-2 horas)

### 3.1 Crear tu propia carpeta
```bash
cd ..
mkdir techlab-mi-proyecto
cd techlab-mi-proyecto
git init
```

### 3.2 Crear archivos manualmente
**NO copies código, escríbelo tú mismo**

1. **Crea `usuarios.csv`**:
   - Escribe manualmente el contenido
   - Entiende qué campos tiene

2. **Crea `usuarios.py`**:
   - Escribe la función `cargar_usuarios()` tú mismo
   - Escribe la función `validar_login()` tú mismo
   - Si te trabas, mira el código original, entiéndelo, y vuelve a escribirlo

3. **Crea `main.py`**:
   - Escribe el código del login paso a paso
   - Prueba frecuentemente

### 3.3 Probar tu código
```bash
python main.py
```

**Debe funcionar igual que el COMMIT 1 original**

### 3.4 Hacer tu primer commit
```bash
git add .
git commit -m "feat: COMMIT 1 - Estructura base y sistema de login"
```

**🎉 ¡Felicitaciones! Tu primer commit está listo**

---

## 📋 PASO 4: Estudiar COMMIT 2 (30 minutos)

### 4.1 Ver qué cambió en COMMIT 2
```bash
cd techlab-inventario
git checkout master  # Volver al estado actual
git show f7b3532  # Ver COMMIT 2
```

### 4.2 Comparar COMMIT 1 vs COMMIT 2
```bash
git diff 775173e f7b3532
```

**Pregúntate:**
- ¿Qué archivos cambiaron?
- ¿Qué código se agregó?
- ¿Por qué se agregó ese código?

### 4.3 Ver el código del COMMIT 2
```bash
git checkout f7b3532
python main.py  # Probar cómo funciona
```

**Entiende:**
- ¿Cómo funciona el menú?
- ¿Por qué usa un `while True`?
- ¿Cómo captura la opción del usuario?

---

## 📋 PASO 5: Recrear COMMIT 2 (1 hora)

### 5.1 Volver a tu proyecto
```bash
cd ../techlab-mi-proyecto
```

### 5.2 Agregar el menú
- Modifica `main.py` para agregar la función `mostrar_menu()`
- Escribe el código tú mismo
- Prueba frecuentemente

### 5.3 Probar
```bash
python main.py
```

**Debe:**
- Hacer login
- Mostrar el menú
- Permitir elegir opciones

### 5.4 Hacer commit
```bash
git add main.py
git commit -m "feat: COMMIT 2 - Menú principal"
```

---

## 📋 PASO 6: Repetir para cada COMMIT

### Proceso para cada COMMIT (3-7):

**Para COMMIT N:**
1. **Estudiar** (30-45 min):
   - Ver qué hace en PLAN_PASO_A_PASO.txt
   - Ver el código con `git show`
   - Entender cada línea
   
2. **Probar** (10 min):
   - `git checkout <commit-N>`
   - Ejecutar y ver cómo funciona
   
3. **Recrear** (1-3 horas):
   - Volver a tu proyecto
   - Escribir el código tú mismo
   - NO copiar y pegar
   - Si te trabas, mira el original, entiéndelo, y vuelve a escribirlo
   
4. **Probar** (15 min):
   - Ejecutar tu código
   - Comparar con el original
   - Asegurarte de que funciona igual
   
5. **Commit** (2 min):
   - `git add .`
   - `git commit -m "feat: COMMIT N - ..."`

---

## 🎓 Estrategia de Aprendizaje por Commit

### COMMIT 3: Cargar datos al inicio
**Qué aprender:**
- Cómo leer archivos CSV
- Cómo estructurar datos en listas y diccionarios
- Por qué se cargan datos al inicio

**Preguntas clave:**
- ¿Qué hace `csv.DictReader()`?
- ¿Por qué uso diccionarios en lugar de listas simples?
- ¿Qué pasa si el CSV está vacío?

---

### COMMIT 4: Gestión equipos - Agregar
**Qué aprender:**
- Cómo generar IDs únicos
- Cómo validar entrada del usuario
- Cómo guardar datos en CSV
- Cómo usar `datetime` para fechas

**Preguntas clave:**
- ¿Cómo genero IDs como EQ001, EQ002?
- ¿Por qué valido que nombre no esté vacío?
- ¿Cómo escribo un diccionario en CSV?

---

### COMMIT 6: Gestión préstamos - Registrar solicitud
**Qué aprender:**
- Cómo validar reglas de negocio (límites de días)
- Cómo verificar estado de equipos
- Lógica de negocio compleja

**Preguntas clave:**
- ¿Por qué cada tipo de usuario tiene límite diferente?
- ¿Cómo verifico que un equipo esté disponible?
- ¿Qué pasa si alguien intenta pedir más días de los permitidos?

---

### COMMIT 8: Gestión préstamos - Registrar devolución
**Qué aprender:**
- Cómo calcular diferencias de fechas
- Cómo determinar retrasos
- Actualizar múltiples entidades (préstamo Y equipo)

**Preguntas clave:**
- ¿Cómo calculo días entre dos fechas?
- ¿Cuándo hay retraso?
- ¿Por qué actualizo tanto el préstamo como el equipo?

---

## ⚠️ Errores Comunes y Cómo Evitarlos

### ❌ Error 1: Copiar y pegar sin entender
**Problema:** Copias código sin entender por qué está ahí

**Solución:**
- Lee el código original
- Entiende cada línea
- Escribe el código tú mismo
- Si no entiendes algo, búscalo en documentación de Python

---

### ❌ Error 2: Avanzar sin probar
**Problema:** Agregas código sin probarlo frecuentemente

**Solución:**
- Prueba después de cada función
- Prueba después de cada cambio pequeño
- No esperes a terminar todo para probar

---

### ❌ Error 3: Saltar commits
**Problema:** Intentas hacer COMMIT 7 sin haber hecho COMMIT 6

**Solución:**
- Haz los commits en orden
- Cada commit construye sobre el anterior
- No puedes entender COMMIT 7 sin COMMIT 6

---

### ❌ Error 4: No leer el código completo
**Problema:** Solo miras el diff, no el código completo

**Solución:**
- Usa `git checkout <commit>` para ver el código completo
- Lee TODO el archivo, no solo las líneas que cambiaron
- Entiende el contexto completo

---

## 📚 Recursos Adicionales

### Cuando no entiendas algo:

1. **Python básico:**
   - `list`, `dict`, `tuple`
   - `for`, `while`, `if`
   - Funciones con `def`
   - Módulos con `import`

2. **CSV en Python:**
   - `csv.DictReader()` - leer CSV
   - `csv.DictWriter()` - escribir CSV
   - Documentación oficial: https://docs.python.org/3/library/csv.html

3. **Fechas en Python:**
   - `datetime.datetime.now()` - fecha actual
   - `datetime.strptime()` - convertir string a fecha
   - `strftime()` - formatear fecha

4. **Debugging:**
   - Usa `print()` para ver valores
   - Usa `type()` para ver tipos de datos
   - Lee mensajes de error cuidadosamente

---

## ✅ Checklist de Aprendizaje

Antes de pasar al siguiente commit, asegúrate de:

- [ ] Entiendo qué hace este commit
- [ ] Puedo explicar cada función en mis propias palabras
- [ ] Mi código funciona igual que el original
- [ ] Probé todos los casos posibles (exitoso y errores)
- [ ] Hice el commit con un mensaje descriptivo
- [ ] Si hubo errores, los arreglé y entendí por qué ocurrieron

---

## 🎯 Tiempo Estimado Total

- **COMMIT 1:** 2-3 horas
- **COMMIT 2:** 1-2 horas
- **COMMIT 3:** 1-2 horas
- **COMMIT 4:** 2-3 horas
- **COMMIT 5:** 1 hora
- **COMMIT 6:** 2-3 horas
- **COMMIT 7:** 2-3 horas
- **COMMIT 8:** 2-3 horas
- **COMMIT 9:** 1-2 horas
- **COMMIT 10:** 1-2 horas
- **COMMIT 11:** 1 hora

**Total: 18-25 horas** de aprendizaje estructurado

---

## 💡 Consejo Final

**"No entiendas el código, entiéndelo ejecutándolo"**

- Lee el código
- Escríbelo tú mismo
- Ejecútalo
- Módi fícalo
- Rómpelo y arréglalo
- Repite

**¡Buena suerte con tu aprendizaje!** 🚀

