# Restaurante App - Semana 13 (versión base GUI)

Breve adaptación de la práctica docente: una versión mínima basada en Tkinter que muestra un flujo de acceso (login) y una interfaz principal para visualizar productos y usuarios cargados desde JSON.

Estructura principal
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

Propósito
- Mantener responsabilidades: modelos para entidades, servicios para acceso a datos y lógica, vistas (ui/) para la interfaz.
- Leer datos desde JSON exclusivamente en ArchivoServicio.
- Usar una única ventana Tkinter y permitir cambiar entre LoginView y MainView.

Flujo de la aplicación
1. Ejecutar main.py
2. Aparece LoginView (usuario + contraseña)
3. Ingresar credenciales (simulación educativa, compara con usuarios en datos/usuarios.json)
4. Si son válidas, mostrar MainView con botones Productos y Usuarios
5. Visualizar listados cargados desde JSON
6. Cerrar sesión vuelve a LoginView en la misma ventana

Notas y limitaciones
- Ventana única (una instancia de Tk()).
- Las ventas se muestran como funcionalidad pendiente (botón deshabilitado).
- No se implementó autenticación real ni persistencia desde la UI; los datos son cargados al iniciar desde datos/*.json.

Ejecución
- Desde la carpeta `restaurante_app` ejecute:

```bash
python main.py
```

Credenciales de prueba
- admin / 1234
- mesero / 5678

Comprobación rápida
- Al iniciar la app debería mostrarse la pantalla de acceso.
- Credenciales válidas muestran la interfaz principal con Productos y Usuarios.
- Las vistas solicitan información a RestauranteServicio (no leen archivos directamente).

