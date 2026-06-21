# Sistema de Gestión de Restaurante - Programación Orientada a Objetos (POO)

## Índice
1. [Descripción General](#descripción-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Análisis de Clases](#análisis-de-clases)
4. [Conceptos de POO Aplicados](#conceptos-de-poo-aplicados)
5. [Flujo de Ejecución](#flujo-de-ejecución)
6. [Cómo Ejecutar](#cómo-ejecutar)

---

## Descripción General

Este proyecto implementa un **sistema básico de gestión de restaurante** utilizando Programación Orientada a Objetos en Python. El sistema demuestra conceptos fundamentales como:

- **Organización modular**: Separación de responsabilidades en carpetas `modelos/` y `servicios/`
- **Clases y objetos**: Representación de entidades del negocio
- **Métodos especiales**: Uso de `__init__()` y `__str__()`
- **Importaciones**: Comunicación entre módulos

El sistema permite:
- ✓ Registrar productos disponibles en el restaurante
- ✓ Registrar clientes
- ✓ Realizar pedidos de productos
- ✓ Consultar inventario y estadísticas

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del paquete de modelos
│   ├── producto.py           # Clase Producto
│   └── cliente.py            # Clase Cliente
├── servicios/
│   ├── __init__.py           # Inicializador del paquete de servicios
│   └── restaurante.py        # Clase Restaurante (gestor del sistema)
└── main.py                   # Punto de entrada de la aplicación
```

### Responsabilidad de cada carpeta

| Carpeta | Descripción |
|---------|------------|
| `modelos/` | Contiene las clases que representan las **entidades** del sistema (Producto y Cliente) |
| `servicios/` | Contiene la clase que **gestiona** las operaciones del sistema (Restaurante) |
| `main.py` | **Punto de entrada** del programa donde se crean objetos y se ejecutan las operaciones |

---

## Análisis de Clases

### 1. Clase `Producto` (modelos/producto.py)

**Propósito**: Representa un artículo disponible en el restaurante (platos, bebidas, etc.)

#### Atributos
```python
- id_producto (int)          # Identificador único
- nombre (str)               # Nombre del producto
- descripcion (str)          # Descripción breve
- precio (float)             # Precio unitario
- cantidad_disponible (int)  # Unidades en inventario
```

#### Métodos Principales
```python
__init__(...)                      # Constructor: inicializa los atributos

__str__()                          # Método especial: representación en texto del producto

obtener_informacion()              # Retorna un diccionario con los detalles del producto

actualizar_disponibilidad(cantidad) # Modifica el inventario al realizar un pedido

obtener_precio()                   # Retorna el precio del producto
```

#### Ejemplo de Uso
```python
# Crear un producto
hamburguesa = Producto(1, "Hamburguesa", "Hamburguesa con queso", 8.99, 50)

# Acceder a información
print(hamburguesa)  # Usa __str__()
# Output: Producto: Hamburguesa | Descripción: Hamburguesa con queso | Precio: $8.99 | Disponibles: 50

# Actualizar inventario
hamburguesa.actualizar_disponibilidad(2)  # Resta 2 unidades
```

---

### 2. Clase `Cliente` (modelos/cliente.py)

**Propósito**: Representa a un cliente que realiza pedidos en el restaurante

#### Atributos
```python
- id_cliente (int)           # Identificador único
- nombre (str)               # Nombre completo
- email (str)                # Correo electrónico
- telefono (str)             # Número telefónico
- pedidos_realizados (list)  # Historial de pedidos
- monto_total_gastado (float)# Dinero total gastado
```

#### Métodos Principales
```python
__init__(...)                       # Constructor: inicializa los atributos básicos

__str__()                           # Método especial: representación en texto del cliente

obtener_informacion()               # Retorna diccionario con detalles del cliente

registrar_pedido(pedido)            # Añade un pedido al historial y actualiza el monto gastado

obtener_pedidos()                   # Retorna la lista de pedidos realizados

obtener_monto_total_gastado()       # Retorna el dinero total gastado

obtener_nombre()                    # Retorna el nombre del cliente
```

#### Ejemplo de Uso
```python
# Crear un cliente
cliente = Cliente(101, "Juan Pérez", "juan@email.com", "+593-1234567")

# Registrar un pedido
pedido = {
    "productos": ["2x Hamburguesa", "1x Pizza"],
    "monto": 30.00
}
cliente.registrar_pedido(pedido)

# Obtener información
print(cliente)  # Usa __str__()
# Output: Cliente: Juan Pérez | Email: juan@email.com | Teléfono: +593-1234567 | Monto gastado: $30.00
```

---

### 3. Clase `Restaurante` (servicios/restaurante.py)

**Propósito**: Gestiona los productos y clientes del restaurante, coordinando las operaciones principales

#### Atributos
```python
- nombre_restaurante (str)  # Nombre del restaurante
- productos (list)          # Lista de productos disponibles
- clientes (list)           # Lista de clientes registrados
```

#### Métodos Principales
```python
__init__(nombre)                          # Constructor: inicializa el restaurante

__str__()                                 # Método especial: representación en texto

agregar_producto(producto)                # Añade un producto al catálogo (valida duplicados)

obtener_producto(id_producto)             # Busca un producto por ID

agregar_cliente(cliente)                  # Registra un cliente (valida duplicados)

obtener_cliente(id_cliente)               # Busca un cliente por ID

realizar_pedido(id_cliente, productos)   # Procesa un pedido validando disponibilidad

listar_productos()                        # Muestra el catálogo formateado

listar_clientes()                         # Muestra los clientes registrados formateado

obtener_resumen_estadisticas()            # Calcula e imprime estadísticas del restaurante
```

#### Ejemplo de Uso
```python
# Crear restaurante
restaurante = Restaurante("La Mesa Feliz")

# Agregar productos
restaurante.agregar_producto(Producto(1, "Hamburguesa", "Desc", 8.99, 50))

# Agregar clientes
restaurante.agregar_cliente(Cliente(101, "Juan", "juan@email.com", "+593-1234567"))

# Realizar pedido (id_cliente, [(id_producto, cantidad), ...])
restaurante.realizar_pedido(101, [(1, 2), (3, 1)])

# Ver información
print(restaurante.listar_productos())
print(restaurante.listar_clientes())
print(restaurante.obtener_resumen_estadisticas())
```

---

## Conceptos de POO Aplicados

### 1. **Clases y Objetos**
Las clases definen la estructura de los datos y sus comportamientos:
```python
class Producto:
    def __init__(self, id_producto, nombre, ...):
        self.id_producto = id_producto  # Atributo
        ...
    
    def obtener_precio(self):  # Método
        return self.precio

# Crear un objeto (instancia)
hamburguesa = Producto(1, "Hamburguesa", ...)
```

### 2. **Constructor (`__init__`)**
Inicializa los atributos cuando se crea un objeto:
```python
def __init__(self, id_cliente, nombre, email, telefono):
    self.id_cliente = id_cliente      # Estos atributos se inicializan
    self.nombre = nombre               # automáticamente al crear el objeto
    self.email = email
    self.telefono = telefono
```

### 3. **Método Especial `__str__()`**
Retorna una representación legible del objeto en texto:
```python
def __str__(self):
    return f"Cliente: {self.nombre} | Email: {self.email} | Monto gastado: ${self.monto_total_gastado:.2f}"

# Al usar print() o str(), se llama automáticamente
print(cliente)  # Usa __str__()
```

### 4. **Encapsulación**
Cada clase gestiona sus propios datos y comportamientos:
- `Producto`: gestiona información del producto
- `Cliente`: gestiona información del cliente
- `Restaurante`: gestiona la colección de productos y clientes

### 5. **Organización Modular**
Separación de responsabilidades:
- **Modelos**: definen las estructuras de datos (Producto, Cliente)
- **Servicios**: realizan las operaciones (Restaurante gestiona todo)
- **Main**: coordina la ejecución

### 6. **Importaciones**
Permite reutilizar clases de diferentes módulos:
```python
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Ahora podemos usar estas clases en main.py
```

---

## Flujo de Ejecución

### Paso 1: Inicialización
```python
restaurante = Restaurante("La Mesa Feliz")
```
- Se crea una nueva instancia de `Restaurante`
- Se inicializan listas vacías para productos y clientes

### Paso 2: Creación de Productos
```python
producto1 = Producto(1, "Hamburguesa", "Descripción", 8.99, 50)
producto2 = Producto(2, "Pizza", "Descripción", 12.50, 30)
...
```
- Se crean objetos `Producto`
- Se especifican atributos: id, nombre, descripción, precio, disponibilidad

### Paso 3: Registro de Productos
```python
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
...
```
- Se añaden productos al catálogo del restaurante
- El método valida que no existan duplicados

### Paso 4: Creación de Clientes
```python
cliente1 = Cliente(101, "Juan Pérez", "juan@email.com", "+593-999-1234")
cliente2 = Cliente(102, "María García", "maria@email.com", "+593-998-5678")
...
```
- Se crean objetos `Cliente`
- Se inicializan con datos de contacto

### Paso 5: Registro de Clientes
```python
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)
...
```
- Se registran clientes en el sistema
- El método valida que no existan duplicados

### Paso 6: Realización de Pedidos
```python
restaurante.realizar_pedido(101, [(1, 2), (3, 1)])
```
- Se procesa el pedido del cliente con ID 101
- Se valida disponibilidad de productos
- Se actualiza el inventario
- Se registra el pedido en el cliente

### Paso 7: Consulta de Información
```python
print(restaurante.listar_productos())
print(restaurante.listar_clientes())
print(restaurante.obtener_resumen_estadisticas())
```
- Se muestra información formateada del sistema
- Se demuestran los métodos `__str__()` de las clases

---

## Validaciones Implementadas

El sistema incluye validaciones para garantizar la integridad de datos:

| Validación | Ubicación | Descripción |
|-----------|-----------|-------------|
| ID duplicado de producto | `agregar_producto()` | No permite dos productos con el mismo ID |
| ID duplicado de cliente | `agregar_cliente()` | No permite dos clientes con el mismo ID |
| Producto inexistente | `realizar_pedido()` | Verifica que el producto exista |
| Inventario insuficiente | `realizar_pedido()` | Verifica que haya suficientes unidades |
| Cliente inexistente | `realizar_pedido()` | Verifica que el cliente exista |
| Cantidad negativa | `actualizar_disponibilidad()` | No permite inventario negativo |

---

## Cómo Ejecutar

### Requisitos
- Python 3.6 o superior
- Sistema operativo: Windows, macOS o Linux

### Pasos

1. **Abrir una terminal** en el directorio del proyecto:
```bash
cd restaurante_app
```

2. **Ejecutar el programa**:
```bash
python main.py
```

3. **Ver la salida**:
El programa mostrará:
- ✓ Creación del restaurante y productos
- ✓ Registro de clientes
- ✓ Catálogo de productos
- ✓ Realización de pedidos
- ✓ Información de clientes
- ✓ Inventario actual
- ✓ Estadísticas del restaurante

### Ejemplo de Salida
```
======================================================================
SISTEMA DE GESTIÓN DE RESTAURANTE - POO
======================================================================

✓ Restaurante creado: Restaurante: La Mesa Feliz | Productos: 0 | Clientes: 0

----------------------------------------------------------------------
CREANDO PRODUCTOS
----------------------------------------------------------------------
✓ Producto 'Hamburguesa Clásica' agregado exitosamente.
✓ Producto 'Pizza Margherita' agregado exitosamente.
...

======================================================================
CLIENTES REGISTRADOS - La Mesa Feliz
======================================================================
• Cliente: Juan Pérez | Email: juan.perez@email.com | Teléfono: +593-999-1234 | Monto gastado: $29.47
• Cliente: María García | Email: maria.garcia@email.com | Teléfono: +593-998-5678 | Monto gastado: $27.99
...

======================================================================
ESTADÍSTICAS - La Mesa Feliz
======================================================================
Total de Productos: 5
Total de Clientes: 3
Ingresos Totales: $57.46
======================================================================
```

---

## Aprendizajes Clave

Este proyecto demuestra:

✅ **Organización Modular**: Separación clara de modelos y servicios
✅ **POO Fundamentales**: Clases, objetos, constructores, atributos y métodos
✅ **Método Especial `__str__()`**: Representación legible de objetos
✅ **Importaciones**: Comunicación efectiva entre módulos
✅ **Validación de Datos**: Integridad en operaciones críticas
✅ **Responsabilidad Simple**: Cada clase tiene un propósito específico
✅ **Reutilización de Código**: Las clases se utilizan en múltiples contextos

---

## Extensiones Posibles

Algunas mejoras que podrían agregarse:

- Agregar una clase `Pedido` separada
- Implementar persistencia de datos (archivos JSON o base de datos)
- Crear una interfaz gráfica (GUI)
- Agregar herencia (clase base de Entidad)
- Implementar excepciones personalizadas
- Añadir métodos de búsqueda avanzada
- Crear un sistema de reportes más completo

---

**Autor**: Estudiante de Programación Orientada a Objetos  
**Fecha**: Semana 4  
**Objetivo**: Demostración de organización modular y POO en Python

