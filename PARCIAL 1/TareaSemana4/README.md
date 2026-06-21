# Sistema de Gestión de Restaurante - Semana 4

## Introducción

Este proyecto es una implementación de un **sistema de gestión de restaurante** utilizando Programación Orientada a Objetos (POO) en Python. El objetivo es demostrar la comprensión de conceptos fundamentales como clases, objetos, herencia conceptual, encapsulación, modularidad e integración de módulos.

## Características

- ✅ **Arquitectura Modular**: Separación clara entre modelos, servicios y lógica de presentación
- ✅ **Clases Bien Definidas**: Producto, Cliente y Restaurante con responsabilidades claras
- ✅ **Métodos Especiales**: Implementación de `__str__()` para representación de objetos
- ✅ **Gestión de Productos**: Registro, búsqueda, listado categorizado y aplicación de descuentos
- ✅ **Gestión de Clientes**: Registro, búsqueda, estado activo/inactivo e historial de pedidos
- ✅ **Creación de Pedidos**: Sistema completo de pedidos con validación y cálculo de totales
- ✅ **Importaciones Correctas**: Comunicación adecuada entre módulos

## Estructura del Proyecto

```
TareaSemana4/
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py      # Clase Producto
│   │   └── cliente.py       # Clase Cliente
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py   # Clase Restaurante (gestor central)
│   └── main.py              # Programa principal de ejecución
├── TareaSemana4_explicacion.md  # Explicación detallada del proyecto
└── README.md                # Este archivo
```

## Descrición de Clases

### Clase `Producto` (modelos/producto.py)
Representa un artículo disponible en el restaurante.

**Atributos:**
- `nombre`: Nombre del producto
- `descripcion`: Descripción detallada
- `precio`: Precio en dólares
- `categoria`: Categoría (plato_principal, bebida, postre, etc)
- `disponible`: Estado de disponibilidad

**Métodos:**
- `__init__()`: Constructor
- `__str__()`: Representación textual
- `cambiar_disponibilidad()`: Alterna el estado
- `aplicar_descuento(porcentaje)`: Aplica descuento porcentual

### Clase `Cliente` (modelos/cliente.py)
Representa a un cliente del restaurante.

**Atributos:**
- `nombre`: Nombre completo
- `email`: Correo electrónico (identificador único)
- `telefono`: Número de teléfono
- `direccion`: Domicilio
- `activo`: Estado en el sistema
- `historial_pedidos`: Registro de pedidos

**Métodos:**
- `__init__()`: Constructor
- `__str__()`: Representación textual
- `cambiar_estado()`: Alterna estado activo/inactivo
- `registrar_pedido()`: Agrega pedido al historial
- `obtener_total_gastado()`: Calcula total gastado

### Clase `Restaurante` (servicios/restaurante.py)
Gestor central del sistema que coordina todas las operaciones.

**Atributos:**
- `nombre`: Nombre del restaurante
- `ubicacion`: Ubicación geográfica
- `productos`: Lista de productos
- `clientes`: Lista de clientes
- `contador_pedidos`: Contador para IDs de pedidos

**Métodos:**
- `registrar_producto()`: Añade nuevo producto
- `registrar_cliente()`: Añade nuevo cliente
- `obtener_producto_por_nombre()`: Busca producto
- `obtener_cliente_por_email()`: Busca cliente
- `crear_pedido()`: Crea nuevo pedido
- `listar_productos()`: Muestra menú categorizado
- `listar_clientes()`: Muestra clientes registrados

## Cómo Ejecutar

### Requisitos
- Python 3.6 o superior
- No se requieren dependencias externas

### Instrucciones

1. **Navegue al directorio del proyecto:**
```bash
cd "restaurante_app"
```

2. **Ejecute el programa principal:**
```bash
python main.py
```

### Salida Esperada
El programa mostrará:
1. Información del restaurante
2. Confirmación de registro de productos y clientes
3. Menú del restaurante organizado por categorías
4. Listado de clientes registrados
5. Creación de pedidos con totales
6. Demostración de métodos especiales `__str__()`
7. Aplicación de descuentos

## Ejemplo de Uso

```python
# Crear un restaurante
restaurante = Restaurante("El Sabor Amazónico", "Puyo, Ecuador")

# Crear y registrar un producto
producto = Producto(
    "Ceviche de Tilapia",
    "Ceviche fresco preparado con tilapia del río",
    25.00,
    "platos_principales"
)
restaurante.registrar_producto(producto)

# Crear y registrar un cliente
cliente = Cliente(
    "Juan Pérez García",
    "juan.perez@email.com",
    "0987654321",
    "Av. 10 de Agosto, Puyo"
)
restaurante.registrar_cliente(cliente)

# Crear un pedido
pedido = restaurante.crear_pedido(
    cliente,
    [("Ceviche de Tilapia", 2)]
)

# Mostrar información
print(restaurante.listar_productos())
print(cliente)
```

## Conceptos de POO Implementados

| Concepto | Implementación |
|----------|----------------|
| **Clases** | Producto, Cliente, Restaurante |
| **Objetos** | Instancias de las clases creadas en main.py |
| **Constructor** | `__init__()` en cada clase |
| **Atributos** | Datos de cada objeto (nombre, precio, email, etc) |
| **Métodos** | Comportamientos (registrar, obtener, crear pedido, etc) |
| **Método Especial** | `__str__()` para representación textual |
| **Importaciones** | Entre modelos y servicios |
| **Modularidad** | Carpetas modelos y servicios con responsabilidades claras |
| **Separación** | Responsabilidades distribuidas entre clases |

## Diferencias con el Ejemplo Docente

Este proyecto **NO copia** el ejemplo de biblioteca proporcionado por el docente. En cambio:

- **Contexto diferente**: Restaurante en lugar de biblioteca
- **Entidades propias**: Producto, Cliente, Restaurante (no Libro, Usuario, Biblioteca)
- **Operaciones específicas**: Gestión de menú, creación de pedidos, aplicación de descuentos
- **Categorización distinta**: Por tipo de alimento/bebida en lugar de género/tipo de libro
- **Funcionalidades adicionales**: Historial de pedidos, cálculo de gastos totales, descuentos

## Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `restaurante_app/main.py` | Programa principal que demuestra el sistema |
| `restaurante_app/modelos/producto.py` | Definición de la clase Producto |
| `restaurante_app/modelos/cliente.py` | Definición de la clase Cliente |
| `restaurante_app/servicios/restaurante.py` | Definición de la clase Restaurante |
| `TareaSemana4_explicacion.md` | Explicación técnica detallada del proyecto |

## Validación del Programa

✅ El programa se ejecuta sin errores  
✅ Todas las importaciones funcionan correctamente  
✅ Los objetos se crean y manipulan correctamente  
✅ El método `__str__()` funciona en todas las clases  
✅ La salida se muestra de forma organizada  
✅ Se demuestra comprensión de modularidad  
✅ Se respetan todas las restricciones de la actividad  

## Observaciones

- El código está totalmente comentado y documentado
- Se utiliza docstrings para documentar clases y métodos
- La organización modular facilita el mantenimiento y la extensión
- El sistema es fácil de entender para alguien nuevo en POO
- Se demuestra claramente la separación de responsabilidades

## Conclusión

Este proyecto exitosamente demuestra la aplicación práctica de los conceptos fundamentales de Programación Orientada a Objetos en Python, con énfasis en organización modular, separación de responsabilidades y correcta integración de módulos independientes.

---

**Estudiante**: Dayvis Calderón  
**Asignatura**: Programación Orientada a Objetos  
**Semana**: 4  
**Fecha**: 2026

