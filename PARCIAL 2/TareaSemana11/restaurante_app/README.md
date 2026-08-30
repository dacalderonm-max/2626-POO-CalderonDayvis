# Restaurante App - Semana 11

## Objetivo
Continuar el proyecto de restaurante_app incorporando colecciones relacionales, ventas y persistencia JSON para productos, usuarios y ventas.

## Estructura principal
- `modelos/producto.py`: producto con stock y validaciones.
- `modelos/usuario.py`: registro de usuarios que pueden comprar.
- `modelos/venta.py`: relación entre usuario, producto y cantidad vendida.
- `servicios/restaurante.py`: lógica de negocio y validaciones.
- `servicios/archivo_servicio.py`: carga y guardado de datos JSON.
- `main.py`: menú principal del sistema.

## Funcionalidades
- Registrar productos con stock disponible.
- Registrar usuarios con identificación, nombre y correo.
- Registrar ventas validando usuario, producto, cantidad y stock.
- Reducir stock del producto al realizar una venta.
- Consultar ventas por usuario.
- Persistir y recuperar datos desde `datos/productos.json`, `datos/usuarios.json` y `datos/ventas.json`.

## Ejecución
```bash
cd restaurante_app
python main.py
```

## Validaciones principales
- No se aceptan cantidades menores o iguales a cero.
- No se permite vender más unidades de las disponibles.
- El stock nunca puede quedar negativo.
- Si alguno de los archivos no existe, la aplicación inicia con colecciones vacías.
