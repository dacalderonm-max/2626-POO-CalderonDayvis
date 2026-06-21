# Explicación del Sistema de Gestión de Restaurante - Semana 4

## Descripción General

El presente proyecto corresponde a la **Semana 4 de Programación Orientada a Objetos**. Se ha desarrollado un sistema de gestión de restaurante que demuestra la aplicación práctica de los conceptos fundamentales de POO, tales como:

- **Clases y Objetos**: Representación de entidades del dominio (Producto, Cliente, Restaurante)
- **Constructor (`__init__()`)**: Inicialización de atributos en cada clase
- **Atributos**: Datos que caracterizan cada objeto
- **Métodos**: Operaciones que pueden realizar los objetos
- **Método especial `__str__()`**: Representación en string de los objetos
- **Importaciones**: Comunicación entre módulos del proyecto
- **Organización Modular**: Separación de responsabilidades en carpetas y archivos

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── __init__.py
```

### Descripción de cada carpeta:

#### **modelos/** - Capas de Datos
Contiene las clases que representan las entidades principales del sistema:

- **`producto.py`**: Define la clase `Producto` que representa un artículo disponible en el restaurante (platos, bebidas, postres, etc)
- **`cliente.py`**: Define la clase `Cliente` que representa una persona que realiza pedidos en el restaurante
- **`__init__.py`**: Facilita las importaciones desde el módulo

#### **servicios/** - Capas de Lógica de Negocio
Contiene las clases que implementan la lógica central del sistema:

- **`restaurante.py`**: Define la clase `Restaurante` que actúa como gestor central del sistema, coordinando productos, clientes y pedidos
- **`__init__.py`**: Facilita las importaciones desde el módulo

#### **main.py** - Punto de Entrada
Es el archivo principal de ejecución. Aquí se crean objetos, se invocan métodos y se demuestra el funcionamiento completo del sistema.

---

## Análisis de las Clases

### **1. Clase `Producto`** (modelos/producto.py)

#### Responsabilidad:
Modelar un artículo disponible en el restaurante con toda su información relevante.

#### Atributos:
- `nombre` (str): Nombre del producto
- `descripcion` (str): Descripción detallada
- `precio` (float): Precio en dólares
- `categoria` (str): Categoría del producto (plato_principal, bebida, postre, etc)
- `disponible` (bool): Estado de disponibilidad para venta

#### Métodos principales:
- `__init__(nombre, descripcion, precio, categoria, disponible=True)`: Constructor que inicializa todos los atributos
- `__str__()`: Retorna una representación legible del producto en formato de string
- `cambiar_disponibilidad()`: Alterna el estado del producto entre disponible e indisponible
- `aplicar_descuento(porcentaje)`: Aplica un descuento porcentual al precio

#### Ejemplo de uso:
```python
producto = Producto(
    "Ceviche de Tilapia",
    "Ceviche fresco preparado con tilapia del río",
    25.00,
    "platos_principales"
)
print(producto)  # Usa el método __str__()
```

---

### **2. Clase `Cliente`** (modelos/cliente.py)

#### Responsabilidad:
Modelar a un cliente del restaurante y registrar su información así como su historial de pedidos.

#### Atributos:
- `nombre` (str): Nombre completo del cliente
- `email` (str): Correo electrónico (identificador único)
- `telefono` (str): Número de teléfono
- `direccion` (str): Domicilio del cliente
- `activo` (bool): Estado del cliente en el sistema
- `historial_pedidos` (list): Lista de pedidos realizados para análisis

#### Métodos principales:
- `__init__(nombre, email, telefono, direccion, activo=True)`: Constructor que inicializa los atributos principales
- `__str__()`: Retorna una representación legible del cliente mostrando toda su información
- `cambiar_estado()`: Alterna el estado del cliente entre activo e inactivo
- `registrar_pedido(id_pedido, monto_total)`: Agrega un nuevo pedido al historial
- `obtener_total_gastado()`: Calcula el monto total gastado por el cliente en todos sus pedidos

#### Ejemplo de uso:
```python
cliente = Cliente(
    "Juan Pérez García",
    "juan.perez@email.com",
    "0987654321",
    "Av. 10 de Agosto, Puyo"
)
print(cliente)  # Usa el método __str__()
total = cliente.obtener_total_gastado()
```

---

### **3. Clase `Restaurante`** (servicios/restaurante.py)

#### Responsabilidad:
Actuar como gestor central del sistema, coordinando todas las operaciones entre productos, clientes y pedidos.

#### Atributos:
- `nombre` (str): Nombre del restaurante
- `ubicacion` (str): Ubicación geográfica del restaurante
- `productos` (list): Lista de productos registrados
- `clientes` (list): Lista de clientes registrados
- `contador_pedidos` (int): Contador para generar IDs únicos de pedidos

#### Métodos principales:

**Gestión de Productos:**
- `registrar_producto(producto)`: Agrega un nuevo producto al catálogo, evitando duplicados
- `obtener_producto_por_nombre(nombre)`: Busca un producto por nombre (case-insensitive)
- `listar_productos()`: Retorna un listado formateado de todos los productos disponibles, organizados por categoría

**Gestión de Clientes:**
- `registrar_cliente(cliente)`: Agrega un nuevo cliente, evitando duplicados de email
- `obtener_cliente_por_email(email)`: Busca un cliente por correo electrónico (case-insensitive)
- `listar_clientes()`: Retorna un listado formateado de todos los clientes registrados

**Gestión de Pedidos:**
- `crear_pedido(cliente, productos_pedido)`: Crea un nuevo pedido para un cliente, validando disponibilidad y calculando totales

**Información General:**
- `__str__()`: Retorna información general del restaurante

#### Ejemplo de uso:
```python
restaurante = Restaurante("El Sabor Amazónico", "Puyo, Ecuador")
restaurante.registrar_producto(producto)
restaurante.registrar_cliente(cliente)
pedido = restaurante.crear_pedido(cliente, [("Ceviche de Tilapia", 2)])
print(restaurante.listar_productos())
```

---

## Características Implementadas de POO

### **1. Clases y Objetos**
Se definieron tres clases principales: `Producto`, `Cliente` y `Restaurante`. Cada clase representa una entidad del dominio y encapsula datos y comportamientos relacionados.

```python
class Producto:
    """Clase que modela un producto del restaurante"""
    
class Cliente:
    """Clase que modela un cliente del restaurante"""
    
class Restaurante:
    """Clase que gestiona las operaciones del restaurante"""
```

### **2. Constructor (`__init__`)**
Cada clase implementa un constructor que inicializa los atributos necesarios:

```python
def __init__(self, nombre, descripcion, precio, categoria, disponible=True):
    self.nombre = nombre
    self.descripcion = descripcion
    self.precio = precio
    self.categoria = categoria
    self.disponible = disponible
```

### **3. Atributos**
Cada objeto posee atributos que caracterzan su estado:
- `Producto`: nombre, descripción, precio, categoría, disponibilidad
- `Cliente`: nombre, email, teléfono, dirección, estado, historial de pedidos
- `Restaurante`: nombre, ubicación, lista de productos, lista de clientes, contador de pedidos

### **4. Métodos**
Cada clase implementa métodos que definen su comportamiento:
- `Producto`: cambiar_disponibilidad(), aplicar_descuento()
- `Cliente`: cambiar_estado(), registrar_pedido(), obtener_total_gastado()
- `Restaurante`: registrar_producto(), registrar_cliente(), obtener_producto_por_nombre(), crear_pedido(), listar_productos(), listar_clientes()

### **5. Método Especial `__str__()`**
Se implementó en todas las clases principales para proporcionar una representación legible del objeto:

```python
def __str__(self):
    return (f"[{self.categoria.upper()}] {self.nombre} - ${self.precio:.2f}\n"
            f"    Descripción: {self.descripcion}\n"
            f"    Estado: {'Disponible' if self.disponible else 'No disponible'}")
```

### **6. Importaciones**
Se utilizaron importaciones modulares para comunicar los archivos del proyecto:

En `servicios/restaurante.py`:
```python
from modelos import Producto, Cliente
```

En `main.py`:
```python
from modelos import Producto, Cliente
from servicios import Restaurante
```

### **7. Organización Modular**
El proyecto está organizado en carpetas con responsabilidades claras:
- **modelos/**: Define las entidades del sistema
- **servicios/**: Implementa la lógica de negocio
- **main.py**: Punto de entrada que demuestra el funcionamiento

---

## Diferencias con el Ejemplo de Biblioteca

Este sistema de restaurante se diferencia del ejemplo docente de biblioteca en los siguientes aspectos:

| Aspecto | Biblioteca (Docente) | Restaurante (Este Proyecto) |
|--------|---------------------|----------------------------|
| **Contexto** | Gestión de libros y préstamos | Gestión de menú y pedidos |
| **Entidades Principales** | Libro, Usuario, Biblioteca | Producto, Cliente, Restaurante |
| **Atributos Ejemplo** | titelo, autor, ISBN | nombre, descripción, precio, categoría |
| **Operaciones** | Prestar, devolver, registrar | Registrar productos, crear pedidos, aplicar descuentos |
| **Categorización** | Por género/tipo de libro | Por categoría de alimento/bebida |
| **Funcionalidad Adicional** | Préstamos y devoluciones | Pedidos, historial de gastos, descuentos |

---

## Flujo de Ejecución del Programa

El programa `main.py` demuestra el funcionamiento completo del sistema en los siguientes pasos:

### 1. **Creación del Restaurante**
Se instancia un objeto `Restaurante` con nombre y ubicación.

### 2. **Registro de Productos**
Se crean varios objetos `Producto` y se registran en el restaurante usando `registrar_producto()`.

### 3. **Registro de Clientes**
Se crean objetos `Cliente` y se registran usando `registrar_cliente()`.

### 4. **Consulta del Menú**
Se muestra el menú del restaurante usando `listar_productos()`, organizado por categorías y con precios.

### 5. **Consulta de Clientes**
Se muestra la información de todos los clientes registrados.

### 6. **Creación de Pedidos**
Se crean pedidos para clientes específicos usando `crear_pedido()`, especificando los productos y cantidades.

### 7. **Demostración de Métodos Especiales**
Se utiliza `__str__()` para mostrar información detallada de productos y clientes de forma legible.

### 8. **Aplicación de Descuentos**
Se demuestra cómo aplicar descuentos a productos modificando el precio.

---

## Salida Esperada

Al ejecutar `python main.py`, el programa genera una salida organizada que muestra:

1. Información del restaurante
2. Confirmación del registro de productos y clientes
3. Menú formateado por categorías
4. Listado de clientes registrados
5. Creación exitosa de pedidos con cálculo de totales
6. Representación textual de objetos usando `__str__()`
7. Cálculo de totales gastados por cliente
8. Aplicación de descuentos

---

## Conceptos de POO Demostrados

✓ **Encapsulación**: Los atributos están protegidos dentro de las clases  
✓ **Abstracción**: Se ocultan detalles complejos de implementación  
✓ **Modularidad**: El proyecto está organizado en módulos independientes  
✓ **Reutilización**: Los objetos se crean una sola vez y se reutilizan  
✓ **Comunicación**: Los módulos se comunican mediante importaciones  
✓ **Separación de Responsabilidades**: Cada clase tiene un propósito específico  

---

## Ejecución del Programa

Para ejecutar el programa, navegue a la carpeta del proyecto y ejecute:

```bash
cd restaurante_app
python main.py
```

El programa se ejecutará sin errores y mostrará toda la información del sistema en consola.

---

## Conclusiones

Este proyecto demuestra una comprensión sólida de los conceptos fundamentales de Programación Orientada a Objetos en Python, con énfasis en:

- La organización modular de proyectos
- La separación clara de responsabilidades
- El uso correcto de importaciones
- La implementación de métodos especiales como `__str__()`
- La creación y gestión de objetos
- La comunicación entre módulos

El sistema es lo suficientemente simple para ser comprensible, pero lo suficientemente completo para demostrar todas las características requeridas de POO.

