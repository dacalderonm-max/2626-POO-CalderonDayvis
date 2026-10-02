# Restaurante App — Semana 16 · Programación Orientada a Objetos · UEA

## Propósito de la Semana 16

La Semana 16 aplica el **manejo de eventos en Tkinter** dentro de la gestión de usuarios. A partir de la aplicación construida en la Semana 15 (ventas y productos), se evoluciona la sección de **Usuarios** para soportar el CRUD completo (registrar, consultar, actualizar, eliminar) con eventos de Treeview, teclado y Combobox.

---

## Evolución realizada sobre el proyecto anterior

| Semana | Incorporación |
|--------|--------------|
| S9–S12 | Modelos, servicios, persistencia JSON |
| S13–S14 | Interfaz gráfica Tkinter, Login, Productos |
| S15 | Sección de Ventas con `command=` y callbacks |
| **S16** | **Gestión completa de Usuarios: CRUD + bind() + eventos** |

Los cambios de la Semana 16 se concentran en:

- **`modelos/usuario.py`**: propiedad `es_administrador` y roles normalizados.
- **`servicios/archivo_servicio.py`**: nuevo método `guardar_usuarios()`.
- **`servicios/restaurante_servicio.py`**: métodos `registrar_usuario`, `actualizar_usuario`, `eliminar_usuario` con validaciones de negocio.
- **`ui/main_view.py`**: panel de Usuarios rediseñado con formulario + Treeview + 4 eventos.
- **`main.py`**: limpia `usuario_activo` al cerrar sesión.

---

## Gestión de Usuarios

El **Administrador** puede:
- Registrar nuevos usuarios de tipo **Empleado** o **Cliente**.
- Actualizar nombre, contraseña y rol de cualquier usuario.
- Eliminar usuarios (con confirmación previa).
- No puede eliminarse a sí mismo ni eliminar al único Administrador.

Los **Empleados** y **Clientes** solo pueden consultar la tabla de usuarios en modo de solo lectura.

---

## Roles

| Rol | Acceso |
|-----|--------|
| **Administrador** | Gestión completa: productos, ventas, usuarios |
| **Empleado** | Puede operar ventas y consultar productos |
| **Cliente** | Consulta de solo lectura |

Credenciales de prueba:
- `admin` / `1234` → Administrador
- `mesero` / `5678` → Empleado
- `cliente1` / `abc123` → Cliente

---

## Eventos implementados

### bind() — eventos registrados con enlace explícito

| Evento | Widget | Callback | Acción |
|--------|--------|----------|--------|
| `<<TreeviewSelect>>` | `tree_usuarios` | `_on_treeview_select_usuario` | Al seleccionar una fila, consulta el usuario en `RestauranteServicio` y carga sus datos en el formulario. La contraseña no se expone. |
| `<Return>` | `entry_usuario_id`, `entry_nombre_usuario`, `entry_password_usuario` | `_on_return_usuarios` | Confirma registro o actualización según el modo activo. Reutiliza el método correspondiente sin duplicar lógica. |
| `<Escape>` | Mismos Entry del formulario | `_on_escape_usuarios` | Limpia el formulario, cancela la selección y devuelve la interfaz a estado inicial. Reutiliza `_cb_limpiar_formulario_usuario`. |
| `<<ComboboxSelected>>` | `combo_rol_usuario` | `_on_rol_seleccionado` | Actualiza la etiqueta descriptiva del rol seleccionado. |

### command= — botones de acción principal

| Botón | Callback | Acción |
|-------|----------|--------|
| ✚ Registrar | `_cb_registrar_usuario` | Crea un nuevo usuario vía `RestauranteServicio.registrar_usuario()`. |
| ✎ Actualizar | `_cb_actualizar_usuario` | Modifica el usuario seleccionado vía `RestauranteServicio.actualizar_usuario()`. |
| ✖ Eliminar | `_cb_eliminar_usuario` | Elimina con confirmación vía `RestauranteServicio.eliminar_usuario()`. |
| ↺ Limpiar | `_cb_limpiar_formulario_usuario` | Limpia el formulario y cancela la selección (igual que `<Escape>`). |

---

## Diferencia entre `command=` y `bind()`

```
command=   → vincula directamente una función a la acción del widget (clic en botón).
             No recibe el objeto `event` como argumento.

bind()     → registra un callback para un evento específico (tecla, selección, etc.).
             El callback recibe el objeto `event` como primer parámetro.
```

### Ejemplo del proyecto:

```python
# command= en botón (Semana 15 y 16)
btn_registrar = tk.Button(frame, command=self._cb_registrar_usuario)

# bind() para evento de teclado (Semana 16)
self.entry_usuario_id.bind("<Return>", self._on_return_usuarios)

# bind() para evento de Treeview (Semana 16)
self.tree_usuarios.bind("<<TreeviewSelect>>", self._on_treeview_select_usuario)

# bind() para evento de Combobox (Semana 16)
self.combo_rol_usuario.bind("<<ComboboxSelected>>", self._on_rol_seleccionado)
```

---

## Flujo de interacción principal (Semana 16)

```
Inicio de la aplicación
        ↓
LoginView (validación con <Return> y botón Ingresar)
        ↓
RestauranteServicio.validar_acceso()
        ↓
MainView (Administrador navega a "Usuarios")
        ↓
Formulario + Treeview de usuarios
        ↓
Selecciona una fila → <<TreeviewSelect>> → bind() → callback
        ↓
RestauranteServicio.buscar_usuario_por_id()
        ↓
Datos cargados en el formulario (sin exponer contraseña)
        ↓
Modifica datos → Actualizar (command=) o Enter (<Return> via bind())
        ↓
RestauranteServicio.actualizar_usuario() → guardar_usuarios() → usuarios.json
        ↓
Actualización del Treeview + respuesta visual
```

---

## Persistencia

Los datos se almacenan en archivos JSON dentro de `datos/`:

- `productos.json` — catálogo del menú
- `usuarios.json` — usuarios con su identificador, nombre, rol y contraseña
- `ventas.json` — historial de transacciones

La interfaz **nunca** lee ni escribe directamente los archivos JSON. Toda operación pasa por `RestauranteServicio`, que delega la persistencia a `ArchivoServicio`.

---

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py          ← rol + es_administrador (S16)
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py ← guardar_usuarios() (S16)
│   └── restaurante_servicio.py ← CRUD usuarios (S16)
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py        ← Eventos Semana 16
├── assets/
│   ├── logo_restaurante.png
│   ├── icono_productos.png
│   ├── icono_usuarios.png
│   ├── icono_ventas.png
│   ├── icono_logout.png
│   └── icono_registrar.png
└── main.py
```

---

## Ejecución

### Requisitos

```bash
pip install pillow
```

### Iniciar la aplicación

```bash
cd restaurante_app
python main.py
```

### Credenciales de prueba

| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| `admin` | `1234` | Administrador |
| `mesero` | `5678` | Empleado |
| `cliente1` | `abc123` | Cliente |

---

## Verificación de funcionalidades

- [ ] `python main.py` inicia sin errores
- [ ] Login con `admin`/`1234` funciona (Administrador)
- [ ] Secciones Productos y Ventas continúan operando
- [ ] Administrador accede a gestión completa de Usuarios
- [ ] Empleado y Cliente ven la tabla en solo lectura
- [ ] Registrar un nuevo usuario → aparece en el Treeview
- [ ] `<<TreeviewSelect>>` carga los datos en el formulario
- [ ] Actualizar un usuario → cambio persiste en `usuarios.json`
- [ ] Eliminar usuario → confirmación previa, no puede eliminarse a sí mismo
- [ ] `<Return>` en formulario ejecuta registro o actualización
- [ ] `<Escape>` limpia el formulario y cancela la selección
- [ ] `<<ComboboxSelected>>` actualiza la descripción del rol
- [ ] Reiniciar la app → usuarios recuperados desde `usuarios.json`

---

*Programación Orientada a Objetos · Semana 16 · Universidad Estatal Amazónica*
