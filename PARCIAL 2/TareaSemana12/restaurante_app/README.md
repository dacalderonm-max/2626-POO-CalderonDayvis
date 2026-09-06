# Restaurante App - Semana 12

## Objetivo
Mejorar el rendimiento del sistema de restaurante aplicando colecciones auxiliares para búsquedas frecuentes por clave, sin perder la estructura de listas principales para almacenar, recorrer y persistir objetos.

## Mejoras implementadas
Se mantuvieron las colecciones principales de productos, usuarios y ventas para conservar la lógica funcional y la persistencia JSON. Adicionalmente, se incorporaron índices en memoria con `dict` para optimizar las consultas más repetitivas:

- `producto_por_codigo`: búsqueda directa de un producto por su código.
- `usuario_por_identificacion`: búsqueda directa de un usuario por su identificación.
- `ventas_por_usuario`: consulta rápida de las ventas asociadas a un usuario.

Estas estructuras se reconstruyen al iniciar el programa y se mantienen sincronizadas cuando se registran, eliminan o cargan datos, evitando recorrer la colección completa en cada operación.

## Estructura principal
- `modelos/producto.py`: representa un producto con stock y validaciones.
- `modelos/usuario.py`: representa un usuario con identificación, nombre y correo.
- `modelos/venta.py`: relaciona usuario, producto y cantidad vendida.
- `servicios/restaurante.py`: lógica de negocio, validaciones y manejo de índices.
- `servicios/archivo_servicio.py`: lectura y escritura de datos JSON.
- `main.py`: menú principal del sistema.

## Funcionalidades conservadas
- Registrar productos con stock disponible.
- Registrar usuarios con identificación, nombre y correo.
- Registrar ventas validando usuario, producto, cantidad y stock.
- Reducir stock del producto al realizar una venta.
- Consultar ventas por usuario.
- Buscar productos y usuarios por clave única.
- Persistir y recuperar datos desde `datos/productos.json`, `datos/usuarios.json` y `datos/ventas.json`.

## Colecciones utilizadas
- `list`: almacena los objetos principales para recorrido, serialización y visualización.
- `dict`: optimiza búsquedas por código e identificación y agrupa ventas por usuario.
- Se evitó el uso excesivo de `set`, porque la mejora real se obtuvo con índices por clave y no con reemplazar la lista principal.

## Ejecución
```bash
cd restaurante_app
python main.py
```

## Validaciones principales realizadas
- Registro de productos y usuarios.
- Búsqueda por código de producto e identificación de usuario.
- Consulta de ventas por usuario sin recorrer toda la lista.
- Venta con actualización de stock.
- Reconstrucción de índices tras cargar datos desde JSON.
- Verificación de coherencia al limpiar y volver a cargar información.
