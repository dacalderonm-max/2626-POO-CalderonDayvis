# Sistema de Restaurante - TareaSemana9

## Descripción

Sistema de gestión de restaurante con capacidad de **persistencia de datos en archivos JSON**. 

Este proyecto clona y mejora el software de TareaSemana8, enfocándose en la **serialización de datos** usando una estructura tipo **diccionario** (JSON) para guardar y cargar:
- **Productos** en `datos/productos.json`
- **Clientes** en `datos/clientes.json`

## Características Principales

✅ **Registro de Productos**: Agregar nuevos productos con código, nombre, categoría y precio  
✅ **Registro de Clientes**: Agregar nuevos clientes con identificación, nombre y correo  
✅ **Persistencia en JSON**: Guardar y cargar datos automáticamente  
✅ **Estructura de Diccionarios**: Conversión bidireccional entre objetos Python y diccionarios JSON  
✅ **Validación de Duplicados**: Previene códigos de producto e identificaciones duplicadas  
✅ **Gestión de Datos**: Opciones para guardar, cargar y limpiar datos en memoria  

## Estructura del Proyecto

```
restaurante_app/
├── __init__.py
├── main.py                          # Interfaz principal interactiva
├── modelos/
│   ├── __init__.py
│   ├── cliente.py                   # Clase Cliente con métodos JSON
│   └── producto.py                  # Clase Producto con métodos JSON
├── servicios/
│   ├── __init__.py
│   ├── restaurante.py               # Servicio de gestión
│   └── gestor_datos.py              # Gestor de persistencia JSON
└── datos/                           # Se crea automáticamente
    ├── productos.json
    └── clientes.json
```

## Estructura de Datos JSON

### productos.json
```json
[
    {
        "codigo": "P001",
        "nombre": "Pizza Margarita",
        "categoria": "Platos Principales",
        "precio": 12.50,
        "tipo": "Producto"
    },
    {
        "codigo": "P002",
        "nombre": "Ensalada César",
        "categoria": "Ensaladas",
        "precio": 8.50,
        "tipo": "Producto"
    }
]
```

### clientes.json
```json
[
    {
        "identificacion": "1234567890",
        "nombre": "Juan Pérez",
        "correo": "juan@example.com"
    },
    {
        "identificacion": "0987654321",
        "nombre": "María García",
        "correo": "maria@example.com"
    }
]
```

## Uso del Sistema

### 1. Ejecutar el Programa

```bash
python main.py
```

### 2. Opciones del Menú

```
1. Registrar producto       - Agregar un nuevo producto
2. Registrar cliente        - Agregar un nuevo cliente
3. Listar productos         - Ver todos los productos en memoria
4. Listar clientes          - Ver todos los clientes en memoria
5. Guardar datos en JSON    - Persistir datos a archivos JSON
6. Cargar datos desde JSON  - Cargar datos desde archivos JSON
7. Limpiar datos en memoria - Borrar datos en memoria (no afecta JSON)
8. Salir                    - Terminar el programa
```

## Principios de Diseño Aplicados

### Principio de Responsabilidad Única (SRP)

- **Modelos (Cliente, Producto)**: Solo representan entidades
- **Restaurante**: Solo gestiona colecciones
- **GestorDatos**: Solo maneja persistencia JSON
- **Main.py**: Solo presenta interfaz y orquesta

### Estructura de Diccionarios

Cada modelo tiene dos métodos especiales:
- `a_diccionario()`: Convierte el objeto a diccionario para JSON
- `desde_diccionario()`: Crea un objeto a partir de un diccionario

```python
# Ejemplo: Producto
producto = Producto("P001", "Pizza", "Platos", 12.50)
diccionario = producto.a_diccionario()  # Convertir a dict
producto_recuperado = Producto.desde_diccionario(diccionario)  # Recuperar de dict
```

## Flujo de Persistencia

```
┌─────────────────────────────────────────────┐
│        ENTRADA DE USUARIO (Main.py)         │
└────────────────┬────────────────────────────┘
                 │
                 ▼
    ┌────────────────────────────┐
    │  CREAR OBJETOS (Modelos)   │
    └────────┬───────────────────┘
             │
             ▼
    ┌────────────────────────────┐
    │  GESTIONAR EN MEMORIA      │
    │    (Restaurante)           │
    └────────┬───────────────────┘
             │
             ▼
    ┌────────────────────────────┐
    │  PERSISTIR EN JSON         │
    │  (GestorDatos)             │
    │  - a_diccionario()         │
    │  - json.dump()             │
    └────────────────────────────┘
             │
             ▼
    ┌────────────────────────────┐
    │  ARCHIVOS JSON EN DISCO    │
    │  datos/productos.json      │
    │  datos/clientes.json       │
    └────────────────────────────┘
```

## Ejemplo de Uso

```python
# Crear instancias
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
from servicios.gestor_datos import GestorDatos

# Inicializar servicios
restaurante = Restaurante()
gestor = GestorDatos()

# Registrar datos
producto = Producto("P001", "Pizza", "Platos", 12.50)
restaurante.registrar_producto(producto)

cliente = Cliente("123456", "Juan", "juan@email.com")
restaurante.registrar_cliente(cliente)

# Guardar a JSON
gestor.guardar_productos(restaurante.obtener_productos())
gestor.guardar_clientes(restaurante.obtener_clientes())

# Cargar desde JSON
_, productos, _ = gestor.cargar_productos()
_, clientes, _ = gestor.cargar_clientes()
```

## Mejoras Realizadas sobre TareaSemana8

| Aspecto | TareaSemana8 | TareaSemana9 |
|--------|------------|------------|
| **Persistencia** | Solo en memoria | ✅ JSON en disco |
| **Estructura JSON** | No aplica | ✅ Diccionarios estructurados |
| **Gestor de Datos** | No existe | ✅ GestorDatos.py |
| **Serialización** | No existe | ✅ a_diccionario() / desde_diccionario() |
| **Menú** | 6 opciones | ✅ 8 opciones (incluye guardar/cargar) |
| **Recuperación de Datos** | No | ✅ Carga automática de JSON |

## Archivos Generados

Al usar el sistema, se crea automáticamente:
```
restaurante_app/
└── datos/
    ├── productos.json        (Se genera al guardar)
    └── clientes.json         (Se genera al guardar)
```

## Próximas Mejoras Sugeridas

- [ ] Agregar búsqueda de productos por categoría
- [ ] Agregar actualización/eliminación de registros
- [ ] Exportar datos a CSV
- [ ] Agregar validación de email
- [ ] Implementar sistema de pedidos

## Autor

Dayvis Calderón - Programación Orientada a Objetos

## Fecha

2026-08-14

