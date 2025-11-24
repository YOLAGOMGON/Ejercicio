# 📖 Instrucciones Diarias - Guía Paso a Paso

## 🎯 Tu Objetivo Final

**Al terminar todo este proceso tendrás:**
1. ✅ Tu propio proyecto TechLab funcionando completamente
2. ✅ Entendimiento completo de cómo se construyó paso a paso
3. ✅ Experiencia escribiendo código Python funcional
4. ✅ Conocimiento de cómo trabajar con Git y commits
5. ✅ Capacidad de explicar qué hace cada parte del código

---

## 📋 Cómo Usar Esta Guía

**Esta guía es tu "mapa" diario:**
- Sigue cada paso en orden
- No saltes pasos
- Completa cada día antes de pasar al siguiente
- Si tienes dudas, revisa el código original del proyecto

---

## 🗓️ PLAN DE ESTUDIO (11 días - 11 commits)

### DÍA 1: Preparación y COMMIT 1
### DÍA 2: COMMIT 2
### DÍA 3: COMMIT 3
### DÍA 4: COMMIT 4
### DÍA 5: COMMIT 5
### DÍA 6: COMMIT 6
### DÍA 7: COMMIT 7
### DÍA 8: COMMIT 8
### DÍA 9: COMMIT 9
### DÍA 10: COMMIT 10
### DÍA 11: COMMIT 11 (Final)

---

## 📚 DÍA 1: Preparación y COMMIT 1 - Sistema de Login

### ✅ PASO 1: Preparar tu espacio de trabajo (10 min)

**1.1 Crear tu carpeta de proyecto:**
```bash
cd c:\projects\yottiz-desarrollo\programacion\1
mkdir techlab-mi-proyecto
cd techlab-mi-proyecto
git init
```

**1.2 Abrir ambos proyectos:**
- **Proyecto original** (techlab-inventario): Para ver cómo está hecho
- **Tu proyecto** (techlab-mi-proyecto): Para escribir tu código

---

### ✅ PASO 2: Entender qué vas a construir (30 min)

**2.1 Leer el plan:**
- Abre `techlab-inventario/PLAN_PASO_A_PASO.txt`
- Lee SOLO las secciones:
  - FASE 1: ANÁLISIS
  - FASE 2: ESTRUCTURAS DE DATOS
  - FASE 3: ARCHIVOS CSV INICIALES

**2.2 Entender el COMMIT 1:**
- Busca la sección "COMMIT 1: Estructura base y login" en PLAN_PASO_A_PASO.txt
- Lee qué hace este commit:
  - Crea archivos CSV iniciales
  - Crea usuarios.py con funciones de login
  - Crea main.py con el flujo de inicio de sesión

---

### ✅ PASO 3: Ver el código del COMMIT 1 (30 min)

**3.1 Ver qué archivos se crearon:**
```bash
cd ../techlab-inventario
git log --oneline
git show 775173e --stat
```
**Resultado:** Verás qué archivos se agregaron/modificaron

**3.2 Ver el código completo del COMMIT 1:**
```bash
git checkout 775173e
```

**3.3 Leer cada archivo del COMMIT 1:**

**a) Leer usuarios.csv:**
- Abre el archivo
- Entiende qué datos guarda
- Formato: `usuario,contrasena,rol`

**b) Leer usuarios.py:**
- Abre el archivo
- Lee función por función:
  - `cargar_usuarios()` - ¿Qué hace?
  - `validar_login()` - ¿Qué hace?
- Pregúntate: ¿Por qué se usan diccionarios? ¿Cómo se lee el CSV?

**c) Leer main.py:**
- Abre el archivo
- Lee línea por línea:
  - ¿Cómo funciona el bucle de login?
  - ¿Por qué máximo 3 intentos?
  - ¿Cómo se valida el login?

**3.4 Probar el código del COMMIT 1:**
```bash
python main.py
```

**Pruebas a hacer:**
- ✅ Login correcto: `admin` / `admin123`
- ✅ Login incorrecto: credenciales falsas
- ✅ 3 intentos fallidos → debe cerrar el programa

---

### ✅ PASO 4: Recrear el COMMIT 1 (1-2 horas)

**IMPORTANTE:** Escribe el código tú mismo, NO copies y pegues.

**4.1 Volver a tu proyecto:**
```bash
cd ../techlab-mi-proyecto
```

**4.2 Crear usuarios.csv:**
1. Crea el archivo `usuarios.csv`
2. Escribe manualmente:
```csv
usuario,contrasena,rol
admin,admin123,ADMIN
```
3. Guarda el archivo

**4.3 Crear usuarios.py:**
1. Crea el archivo `usuarios.py`
2. Escribe la función `cargar_usuarios()`:
   - Piensa: ¿Cómo leo un CSV en Python?
   - Usa `csv.DictReader()`
   - Retorna una lista de diccionarios
   - Si te trabas, vuelve a ver el original, entiéndelo, y escríbelo tú

3. Escribe la función `validar_login()`:
   - Recibe usuario y contraseña
   - Carga los usuarios
   - Compara con las credenciales
   - Retorna True o False

4. **Prueba frecuentemente:**
```bash
python -c "from usuarios import cargar_usuarios, validar_login; print(cargar_usuarios())"
```

**4.4 Crear main.py:**
1. Crea el archivo `main.py`
2. Importa las funciones de usuarios.py
3. Escribe la función `main()`:
   - Muestra mensaje de bienvenida
   - Bucle para intentos de login (máximo 3)
   - Pide usuario y contraseña
   - Valida con `validar_login()`
   - Si es válido → mensaje de éxito
   - Si no es válido → muestra error y cuenta intentos
   - Si 3 intentos fallidos → cierra el programa

4. Agrega `if __name__ == "__main__": main()`

**4.5 Probar tu código:**
```bash
python main.py
```

**Debe funcionar igual que el COMMIT 1 original:**
- ✅ Login correcto funciona
- ✅ Login incorrecto muestra error
- ✅ 3 intentos fallidos cierra el programa

---

### ✅ PASO 5: Hacer tu primer commit (5 min)

**5.1 Verificar qué archivos creaste:**
```bash
git status
```

**5.2 Agregar archivos al commit:**
```bash
git add usuarios.csv usuarios.py main.py
```

**5.3 Hacer el commit:**
```bash
git commit -m "feat: COMMIT 1 - Estructura base y sistema de login

- Crear archivos CSV iniciales (usuarios.csv)
- Implementar usuarios.py con funciones cargar_usuarios() y validar_login()
- Implementar main.py con flujo de inicio de sesión
- Validación de credenciales con máximo 3 intentos"
```

**5.4 Verificar tu commit:**
```bash
git log --oneline
```

**🎉 ¡Felicitaciones! Completaste el DÍA 1**

---

## 📚 DÍA 2: COMMIT 2 - Menú Principal

### ✅ PASO 1: Volver al proyecto original (5 min)

```bash
cd ../techlab-inventario
git checkout master  # Volver al estado más reciente
```

### ✅ PASO 2: Estudiar COMMIT 2 (30 min)

**2.1 Ver qué cambió en COMMIT 2:**
```bash
git show f7b3532 --stat
```
**Resultado:** Verás que solo cambió `main.py`

**2.2 Ver los cambios completos:**
```bash
git show f7b3532
```
**Resultado:** Verás qué código se agregó

**2.3 Ver el código completo del COMMIT 2:**
```bash
git checkout f7b3532
```

**2.4 Leer main.py:**
- Abre `main.py`
- Ve la nueva función `mostrar_menu()`
- Entiende:
  - ¿Por qué usa `while True`?
  - ¿Cómo captura la opción del usuario?
  - ¿Qué pasa cuando eliges opción 1, 2, 3, etc.?

**2.5 Probar el código del COMMIT 2:**
```bash
python main.py
```

**Pruebas:**
- ✅ Login exitoso
- ✅ Muestra el menú
- ✅ Puedes elegir opciones 1-5
- ✅ Opción 5 (Salir) cierra el programa

**2.6 Leer el plan del COMMIT 2:**
- Busca "COMMIT 2: Menú principal" en PLAN_PASO_A_PASO.txt
- Lee qué debía hacer este commit

---

### ✅ PASO 3: Recrear el COMMIT 2 (1 hora)

**3.1 Volver a tu proyecto:**
```bash
cd ../techlab-mi-proyecto
```

**3.2 Modificar main.py:**

1. **Después del login exitoso**, agrega la llamada a `mostrar_menu()`

2. **Crea la función `mostrar_menu()`:**
   - Usa `while True` para mantener el programa activo
   - Muestra el menú con opciones 1-5
   - Captura la opción del usuario con `input()`
   - Usa `if/elif` para manejar cada opción
   - Por ahora, cada opción solo muestra un mensaje
   - Opción 5 debe hacer `break` para salir

**3.3 Probar:**
```bash
python main.py
```

**Debe:**
- ✅ Mostrar menú después de login
- ✅ Responder a cada opción
- ✅ Opción 5 cierra el programa

---

### ✅ PASO 4: Hacer commit (5 min)

```bash
git add main.py
git commit -m "feat: COMMIT 2 - Menú principal

- Agregar función mostrar_menu() con opciones 1-5
- Implementar bucle while True para mantener programa activo
- Opciones: Gestión equipos, Préstamos, Historial, Reportes, Salir"
```

**🎉 ¡Completaste el DÍA 2!**

---

## 📚 DÍA 3: COMMIT 3 - Cargar Datos al Inicio

### ✅ PASO 1: Estudiar COMMIT 3 (30 min)

```bash
cd ../techlab-inventario
git checkout master
git show 0a84fbe  # Ver COMMIT 3
git checkout 0a84fbe  # Ver código completo
```

**1.1 Leer los nuevos archivos:**
- `equipos.py` - función `cargar_equipos()`
- `prestamos.py` - función `cargar_prestamos()`

**1.2 Leer cambios en main.py:**
- Ve cómo se cargan los datos después del login
- Ve cómo se pasan las listas al menú

**1.3 Probar:**
```bash
python main.py
```

---

### ✅ PASO 2: Recrear COMMIT 3 (1-2 horas)

**2.1 Crear equipos.csv vacío:**
```
equipo_id,nombre_equipo,categoria,estado_actual,fecha_registro,descripcion
```

**2.2 Crear prestamos.csv vacío:**
```
prestamo_id,equipo_id,nombre_equipo,usuario_prestatario,tipo_usuario,fecha_solicitud,fecha_prestamo,fecha_devolucion,dias_autorizados,dias_reales_usados,retraso,estado,mes,anio
```

**2.3 Crear equipos.py:**
- Función `cargar_equipos()` que lee equipos.csv
- Retorna lista de diccionarios

**2.4 Crear prestamos.py:**
- Función `cargar_prestamos()` que lee prestamos.csv
- Retorna lista de diccionarios

**2.5 Modificar main.py:**
- Después de login exitoso, cargar datos
- Pasar listas a `mostrar_menu(lista_equipos, lista_prestamos)`

**2.6 Probar y hacer commit**

**🎉 ¡Completaste el DÍA 3!**

---

## 📚 DÍAS 4-11: Continuar con el mismo proceso

### Para cada COMMIT (4-11):

1. **ESTUDIAR** (30-45 min):
   - Ver el commit con `git show <numero>`
   - Ver código completo con `git checkout <numero>`
   - Leer el plan en PLAN_PASO_A_PASO.txt
   - Probar el código del commit

2. **RECREAR** (1-3 horas):
   - Volver a tu proyecto
   - Escribir el código tú mismo
   - Probar frecuentemente

3. **COMMIT** (5 min):
   - `git add .`
   - `git commit -m "mensaje descriptivo"`

---

## 📝 Números de Commits para Referencia

```bash
# Ver todos los commits
cd techlab-inventario
git log --oneline
```

**Números importantes:**
- `775173e` - COMMIT 1
- `f7b3532` - COMMIT 2
- `0a84fbe` - COMMIT 3
- `0de3269` - COMMIT 4
- `48fe040` - COMMIT 5
- `8d67365` - COMMIT 6
- `9c32532` - COMMIT 7
- `1ec859e` - COMMIT 8
- `d4f4fa5` - COMMIT 9
- `ef3b2cc` - COMMIT 10
- `66354e6` - COMMIT 11

---

## ✅ Checklist Diario

Al final de cada día, asegúrate de:

- [ ] Entiendo qué hace este commit
- [ ] Vi el código original completo
- [ ] Probé el código original
- [ ] Escribí el código yo mismo (no copié)
- [ ] Mi código funciona igual que el original
- [ ] Hice el commit correctamente
- [ ] Puedo explicar qué hace cada función

---

## 🆘 Si Te Trabaste

1. **Vuelve al código original:**
   ```bash
   cd ../techlab-inventario
   git checkout <numero-commit>
   ```

2. **Lee el código línea por línea**

3. **Entiende qué hace cada línea**

4. **Vuelve a tu proyecto y escríbelo tú mismo**

5. **Si aún no entiendes, busca en documentación de Python**

---

## 🎯 Al Finalizar Todos los Días

Tendrás:
- ✅ Tu proyecto completo funcionando
- ✅ Entendimiento de cada commit
- ✅ Experiencia escribiendo código Python
- ✅ Conocimiento de Git
- ✅ Capacidad de explicar todo el proyecto

---

## 💡 Recuerda

**"No aprendas el código, aprende escribiéndolo"**

- Lee → Entiende → Escribe → Prueba → Aprende

**¡Buena suerte con tu aprendizaje!** 🚀

