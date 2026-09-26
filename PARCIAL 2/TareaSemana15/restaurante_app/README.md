# Restaurante App — Semana 15

## Propósito

La Semana 15 tiene como objetivo comprender los **fundamentos básicos del manejo de eventos** en una aplicación con interfaz gráfica. Se utiliza la operación de **venta** como contexto práctico para demostrar cómo un botón activa un callback y cómo este coordina una operación sin concentrar toda la lógica dentro de la interfaz.

## Evolución respecto a semanas anteriores

Esta versión **conserva y extiende** el trabajo desarrollado previamente:

- **Login** (Semana 13): autenticación contra `usuarios.json` mediante `RestauranteServicio`.
- **Productos y Usuarios** (Semana 14): consulta de datos desde JSON con arquitectura modular.
- **Ventas** (Semana 15 — nuevo): registro de ventas que relaciona un usuario con un producto, con persistencia en `ventas.json`.

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          ← Productos del menú con stock
│   ├── usuarios.json           ← Credenciales y datos de usuarios
│   └── ventas.json             ← Ventas registradas (persistencia)
├── modelos/
│   ├── __init__.py
│   ├── cliente.py              ← Compatibilidad con versiones anteriores
│   ├── producto.py             ← Modelo Producto (código, nombre, categoría, precio, stock)
│   ├── usuario.py              ← Modelo Usuario (usuario, password, nombre, rol)
│   └── venta.py                ← Modelo Venta (usuario_id, producto_codigo, cantidad, fecha)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     ← Lectura y escritura de archivos JSON
│   ├── gestor_datos.py         ← Compatibilidad con versiones anteriores
│   └── restaurante_servicio.py ← Lógica de negocio: login, productos, usuarios, ventas
├── ui/
│   ├── __init__.py
│   ├── login_view.py           ← Pantalla de inicio de sesión (tema oscuro)
│   └── main_view.py            ← Panel principal con Productos, Usuarios y Ventas
├── assets/                     ← Íconos y logotipo del sistema
│   ├── logo_restaurante.png
│   ├── icono_productos.png
│   ├── icono_usuarios.png
│   ├── icono_ventas.png
│   ├── icono_logout.png
│   └── icono_registrar.png
└── main.py                     ← Punto de entrada de la aplicación
```

## Gestión de Ventas (nuevo en Semana 15)

La sección de Ventas permite:

1. **Seleccionar un usuario** registrado mediante un `Combobox`.
2. **Seleccionar un producto** registrado mediante un `Combobox`.
3. **Indicar la cantidad** deseada con un `Spinbox`.
4. **Registrar la venta** mediante un botón que usa `command=callback`.

### Flujo de eventos implementado

```
USUARIO
   ↓
realiza una acción (clic en "Registrar venta")
   ↓
BOTÓN / COMPONENTE
   ↓
command=self._callback_registrar_venta  (sin paréntesis)
   ↓
CALLBACK (_callback_registrar_venta)
   ↓
RestauranteServicio.registrar_venta()
   ↓
PERSISTENCIA (ventas.json y productos.json actualizados)
   ↓
RESPUESTA EN LA INTERFAZ (tabla actualizada + mensaje de resultado)
```

### Uso de `command=` y callbacks

- El botón "Registrar venta" se vincula con `command=self._callback_registrar_venta`.
- **Importante**: se usa `command=callback` y **no** `command=callback()`, para que Tkinter ejecute el método al hacer clic, en lugar de ejecutarlo inmediatamente al construir el botón.
- El callback obtiene los datos de la interfaz (Combobox y Spinbox), pero **delega** la validación y el registro a `RestauranteServicio`.
- El servicio valida que el usuario y el producto existan, verifica el stock disponible, crea el objeto `Venta`, descuenta el stock y persiste los cambios en `ventas.json`.

### Persistencia en `ventas.json`

Cada venta registrada se almacena automáticamente en `datos/ventas.json` con la siguiente estructura:

```json
{
    "usuario_id": "admin",
    "producto_codigo": "P001",
    "cantidad": 2,
    "fecha": "2026-09-26 09:30:00"
}
```

Las ventas se recuperan al reiniciar la aplicación, demostrando la persistencia de datos.

## Ejecución

Desde la carpeta `restaurante_app`:

```bash
python main.py
```

### Dependencia adicional

La interfaz utiliza `Pillow` para cargar imágenes PNG. Si no está instalado:

```bash
pip install Pillow
```

## Credenciales de prueba

| Usuario | Contraseña | Rol           |
|---------|------------|---------------|
| admin   | 1234       | administrador |
| mesero  | 5678       | mesero        |

## Comprobación de funcionamiento

1. Ejecutar `main.py` → aparece la pantalla de login.
2. Ingresar credenciales válidas → se muestra el panel principal.
3. Navegar por las secciones: **Productos**, **Usuarios**, **Ventas**.
4. En Ventas: seleccionar usuario, producto y cantidad.
5. Clic en **Registrar venta** → el callback delega a `RestauranteServicio`.
6. La venta se almacena en `ventas.json` y aparece en la tabla.
7. Cerrar y reabrir la aplicación → las ventas previas se recuperan.
8. El botón "Cerrar sesión" regresa al login.

## Uso de assets/

La carpeta `assets/` contiene el logotipo y los íconos utilizados en la interfaz:
- **Logo**: se muestra en el login y en la barra superior del panel principal.
- **Íconos**: acompañan los botones de navegación (Productos, Usuarios, Ventas) y las acciones (Registrar venta, Cerrar sesión).

## Nota

Este proyecto es una evolución progresiva del mismo sistema desarrollado desde semanas anteriores. No se copió literalmente el proyecto docente; los nombres, métodos, entidades y mensajes representan correctamente la lógica del restaurante.
