# Restaurante App - Semana 14

Esta versión evoluciona la aplicación del restaurante para separar de forma más clara la interfaz, las reglas de negocio y la persistencia. La estructura modular se conserva y se fortalece con una vista principal organizada por contenedores y con operaciones reales sobre productos y usuarios.

## Propósito
La aplicación mantiene un flujo de acceso por login y, tras autenticarse, presenta una interfaz de gestión con navegación, formulario y visualización de información. En esta semana se incorporan componentes de Tkinter/ttk para mejorar la organización visual y la experiencia del usuario.

## Estructura del proyecto
- restaurante_app/
  - datos/
    - productos.json
    - usuarios.json
  - modelos/
    - producto.py
    - usuario.py
  - servicios/
    - archivo_servicio.py
    - restaurante_servicio.py
  - ui/
    - login_view.py
    - main_view.py
  - main.py
  - README.md

## Componentes y contenedores utilizados
- `tk.Frame`: contenedores principales para la ventana y el contenido.
- `ttk.Frame`: organización de panels y botones.
- `ttk.LabelFrame`: agrupación de los formularios de productos y usuarios.
- `ttk.Entry`: captación de datos del usuario y del producto.
- `ttk.Button`: acciones de registro, consulta, actualización, eliminación y limpieza.
- `ttk.Treeview`: presentación tabular de los productos registrados.
- `tk.Text`: consulta y visualización de usuarios.

## Mejoras respecto a la Semana 13
- La vista principal ya no es solo un listbox general; ahora cuenta con navegación lateral y contenido dividido por secciones.
- Los formularios de productos y usuarios están organizados visualmente para facilitar la captura y edición de datos.
- La interfaz muestra usuarios y productos en áreas separadas para mejorar claridad.
- Las operaciones sobre productos y usuarios se ejecutan desde botones con `command=` y se actualizan en tiempo real.
- La capa de negocio queda en `RestauranteServicio` y no se dispersa en la UI.
- La persistencia se mantiene en `datos/productos.json` y `datos/usuarios.json` mediante el servicio de archivos.

## Operaciones implementadas sobre productos y usuarios
La gestión de productos incluye:
1. Registro de nuevos productos.
2. Consulta por código para cargar el producto en el formulario.
3. Actualización de nombre, categoría, precio y stock.
4. Eliminación mediante el código del producto.

La gestión de usuarios incluye:
1. Registro de nuevos usuarios.
2. Consulta del usuario por nombre de usuario.
3. Actualización de contraseña, nombre y rol.
4. Eliminación del usuario.

Todas las validaciones se realizan dentro de `RestauranteServicio`, evitando que los botones o las vistas manejen directamente reglas del negocio.

## Persistencia
Los datos se guardan en `datos/productos.json` y `datos/usuarios.json` a través de `ArchivoServicio`, manteniendo la misma arquitectura modular de la versión anterior. La carga inicial se hace desde JSON al iniciar la aplicación.

## Ejecutar la aplicación
Desde la carpeta `restaurante_app` ejecute:

```bash
python main.py
```

## Credenciales de prueba
- Usuario: `dayvis2002`
- Contraseña: `Calderon`
- Usuario: `admin`
- Contraseña: `1234`
- Usuario: `mesero`
- Contraseña: `5678`

## Cambios aplicados en esta versión
- Se corrigió la clase `Usuario` y su carga desde JSON.
- Se agregaron las operaciones de registro, consulta, actualización y eliminación de usuarios dentro de `RestauranteServicio`.
- Se añadió persistencia de usuarios en `ArchivoServicio`.
- Se incorporó en la interfaz principal un formulario para manejar usuarios desde la GUI.
- Se mantuvo la gestión de productos con registro, consulta, actualización y eliminación mediante botones `command=`.
- Se documentó la versión final y se dejó la estructura modular intacta.

## Validación funcional esperada
- La app inicia sin errores.
- El login valida correctamente los usuarios registrados.
- La interfaz principal se muestra luego del acceso.
- La sección de Usuarios presenta la información disponible y permite registrar, consultar, actualizar y eliminar usuarios.
- La sección de Productos presenta un formulario organizado con acciones de gestión.
- Los cambios sobre productos y usuarios se reflejan en la interfaz y se conservan en los archivos JSON.