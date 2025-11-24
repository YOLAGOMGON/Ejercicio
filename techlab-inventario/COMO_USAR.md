# 📖 Cómo Usar Este Proyecto - Guía para Estudiantes

## 🎯 ¿Qué se ha hecho hasta ahora?

### ✅ COMMIT 1: Estructura base y login
**Estado:** ✅ Completado

**Qué hace:**
- El programa inicia y pide usuario y contraseña
- Valida las credenciales contra `usuarios.csv`
- Permite máximo 3 intentos
- Si el login es exitoso, muestra mensaje de bienvenida

**Archivos creados:**
- `main.py` - Punto de entrada del programa
- `usuarios.py` - Funciones para validar login
- `usuarios.csv` - Usuario administrador (admin/admin123)
- `equipos.csv` - Archivo vacío para equipos
- `prestamos.csv` - Archivo vacío para préstamos

---

## 🧪 Cómo Probar el COMMIT 1

1. **Abre una terminal en la carpeta del proyecto:**
   ```bash
   cd techlab-inventario
   ```

2. **Ejecuta el programa:**
   ```bash
   python main.py
   ```

3. **Prueba con credenciales correctas:**
   - Usuario: `admin`
   - Contraseña: `admin123`
   - Debe mostrar: "✓ Login exitoso"

4. **Prueba con credenciales incorrectas:**
   - Usuario: `admin`
   - Contraseña: `contraseña_incorrecta`
   - Debe mostrar error y permitir 3 intentos máximo

5. **Prueba el límite de intentos:**
   - Ingresa credenciales incorrectas 3 veces
   - El programa debe cerrarse después del 3er intento

---

## 📚 Cómo Ver el Progreso en Git

### Ver todos los commits:
```bash
git log --oneline
```

### Ver qué cambió en un commit específico:
```bash
git show <numero-commit>
```

### Ver el estado actual:
```bash
git status
```

### Volver a un commit anterior (para aprender):
```bash
git checkout <numero-commit>
```

**Ejemplo:** Si quieres volver al COMMIT 1 después de avanzar:
```bash
git log --oneline  # Ver el número del commit
git checkout a9b04cc  # Volver al commit inicial
```

**Para volver al estado más reciente:**
```bash
git checkout master
```

---

## 🚀 Próximos Pasos (Completar el Proyecto)

### COMMIT 2: Menú principal
**Qué hará:**
- Después del login exitoso, mostrar un menú con opciones:
  1. Gestión de equipos
  2. Gestión de préstamos
  3. Historial
  4. Reportes
  5. Salir

**Cómo hacerlo:**
1. Abre `main.py`
2. Después de `login_exitoso = True`, agrega una función `mostrar_menu()`
3. Usa un bucle `while True` para mantener el menú activo
4. Por ahora, cada opción solo debe mostrar un mensaje

**Para hacer el commit:**
```bash
git add main.py
git commit -m "feat: COMMIT 2 - Menú principal

- Agregar función mostrar_menu()
- Bucle while para mantener programa activo
- Opciones 1-5 del menú principal"
```

---

### COMMIT 3: Cargar datos al inicio
**Qué hará:**
- Al iniciar (después de login), cargar equipos.csv y prestamos.csv en memoria
- Crear funciones para leer CSV en cada módulo

**Archivos a crear/modificar:**
- `equipos.py` - Crear función `cargar_equipos()`
- `prestamos.py` - Crear función `cargar_prestamos()`
- `main.py` - Modificar para cargar datos después de login

---

## 📝 Consejos para Aprender

### 1. Prueba cada commit antes de pasar al siguiente
- No avances si algo no funciona
- Arregla los problemas antes de continuar

### 2. Usa git log para ver tu progreso
```bash
git log --oneline --graph
```
Esto te muestra todos tus commits de forma visual.

### 3. Si algo no funciona, vuelve atrás
```bash
git checkout <commit-anterior>
```
Esto te permite ver cómo estaba antes.

### 4. Lee el PLAN_PASO_A_PASO.txt
- Tiene todos los pasos detallados
- Sigue el plan en orden
- No saltes pasos

### 5. Haz commits descriptivos
- Cada commit debe tener un objetivo claro
- Usa mensajes como: "feat: agregar función X" o "fix: corregir error Y"

---

## 🎓 Estructura de Commits Recomendada

Cada commit debe seguir este formato:

```
feat: COMMIT X - [Título descriptivo]

- [Cambio 1]
- [Cambio 2]
- [Cambio 3]
```

**Ejemplo:**
```
feat: COMMIT 4 - Gestión equipos - Agregar equipo

- Crear equipos.py con función registrar_equipo()
- Agregar función guardar_equipos_csv()
- Implementar opción 1.1 en menú para registrar equipos
```

---

## ❓ Preguntas Frecuentes

### ¿Puedo hacer varios commits a la vez?
No es recomendable. Cada commit debe ser una funcionalidad completa pero pequeña. Esto te permite:
- Ver tu progreso paso a paso
- Volver atrás fácilmente si algo falla
- Entender mejor cómo se construyó el proyecto

### ¿Qué hago si cometo un error?
1. Identifica el error
2. Arréglalo
3. Haz un commit con `fix:` al inicio:
   ```bash
   git commit -m "fix: corregir error en función X"
   ```

### ¿Debo guardar los CSV en cada cambio?
Sí, según los requisitos, cada cambio debe guardarse inmediatamente en CSV. Esto asegura que los datos no se pierdan.

---

## 🔄 Orden de Commits

1. ✅ COMMIT 1: Estructura base y login
2. ⏳ COMMIT 2: Menú principal
3. ⏳ COMMIT 3: Cargar datos al inicio
4. ⏳ COMMIT 4: Gestión equipos - Agregar
5. ⏳ COMMIT 5: Gestión equipos - Listar y consultar
6. ⏳ COMMIT 6: Gestión préstamos - Registrar solicitud
7. ⏳ COMMIT 7: Gestión préstamos - Aprobar/Rechazar
8. ⏳ COMMIT 8: Gestión préstamos - Registrar devolución
9. ⏳ COMMIT 9: Historial
10. ⏳ COMMIT 10: Exportar reporte CSV
11. ⏳ COMMIT 11: Validaciones y manejo de errores

---

## 📞 Ayuda

Si necesitas ayuda con algún commit:
1. Lee el PLAN_PASO_A_PASO.txt en la sección correspondiente
2. Revisa el README.md para entender el contexto general
3. Prueba el código paso a paso
4. Usa `print()` para ver qué valores tienen las variables

---

¡Buena suerte con tu proyecto! 🚀

Recuerda: **Un commit a la vez, prueba cada uno, y no tengas prisa.**

