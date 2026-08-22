Proyecto: Semana 10 - Restaurante App (Persistencia JSON)

Estudiante: Dayvis Aly Calderon Mendoza

Descripción
Se continuó la evolución del proyecto restaurante_app añadiendo persistencia de productos en formato JSON, manejo básico de excepciones y separación de responsabilidades. La persistencia permite guardar y recuperar la colección de productos entre ejecuciones manteniendo el uso de objetos Producto.

Estructura principal
restaurante_app/
├── datos/ (almacena productos.json)
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── gestor_datos.py (manejo JSON)
│   └── restaurante.py (lógica de negocio)
└── main.py

Flujo de carga y guardado
- main.py crea GestorDatos y Restaurante.
- Al iniciar, GestorDatos.cargar_productos() intenta leer datos/productos.json.
  - FileNotFoundError -> inicia con lista vacía.
  - json.JSONDecodeError -> mensaje de error controlado.
- Los registros válidos se convierten en objetos Producto mediante Producto.desde_diccionario().
- Al registrar, actualizar o eliminar productos, llamar a GestorDatos.guardar_productos(productos) para actualizar datos/productos.json.

Excepciones controladas
- FileNotFoundError: se maneja iniciando con colección vacía.
- json.JSONDecodeError: se informa y no se detiene la aplicación.
- PermissionError: detectado al leer/escribir (se informa).
- KeyError/ValueError: manejados al reconstruir o validar objetos Producto.

Ejecución
Desde la carpeta restaurante_app:
python main.py

Prueba rápida de persistencia
1) Ejecutar main.py y registrar un producto.
2) Seleccionar "Guardar datos en JSON" o salir para que guarde automáticamente.
3) Cerrar y volver a ejecutar main.py.
4) Listar productos: los previamente guardados deben aparecer.

Notas
- La persistencia se concentra en servicios/gestor_datos.py.
- Mantener la estructura modular y no sustituir la clase Producto por diccionarios en la lógica del sistema.

Contacto
- Estudiante: Dayvis Aly Calderon Mendoza
- Repositorio: (submódulo actualizado localmente)