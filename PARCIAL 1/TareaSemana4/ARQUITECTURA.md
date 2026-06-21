# Diagrama de Clases y Arquitectura - Sistema de Restaurante

## 📊 Diagrama de Clases

```
┌─────────────────────────────────────────────────────────────────────┐
│                           SISTEMA DE RESTAURANTE                    │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────┐  ┌──────────────────────┐
│         PRODUCTO             │  │     CLIENTE          │
├──────────────────────────────┤  ├──────────────────────┤
│ - nombre: str                │  │ - nombre: str        │
│ - descripcion: str           │  │ - email: str         │
│ - precio: float              │  │ - telefono: str      │
│ - categoria: str             │  │ - direccion: str     │
│ - disponible: bool           │  │ - activo: bool       │
│                              │  │ - historial_pedidos: │
├──────────────────────────────┤  │   list               │
│ + __init__()                 │  ├──────────────────────┤
│ + __str__()                  │  │ + __init__()         │
│ + cambiar_disponibilidad()   │  │ + __str__()          │
│ + aplicar_descuento()        │  │ + cambiar_estado()   │
│                              │  │ + registrar_pedido() │
│                              │  │ + obtener_total_()   │
└──────────────────────────────┘  └──────────────────────┘
         │                                  │
         │                                  │
         └──────────────┬───────────────────┘
                        │
                        │ utilizadas por
                        ▼
        ┌──────────────────────────────────┐
        │        RESTAURANTE               │
        ├──────────────────────────────────┤
        │ - nombre: str                    │
        │ - ubicacion: str                 │
        │ - productos: list                │
        │ - clientes: list                 │
        │ - contador_pedidos: int          │
        ├──────────────────────────────────┤
        │ + __init__()                     │
        │ + __str__()                      │
        │ + registrar_producto()           │
        │ + registrar_cliente()            │
        │ + obtener_producto_()            │
        │ + obtener_cliente_()             │
        │ + crear_pedido()                 │
        │ + listar_productos()             │
        │ + listar_clientes()              │
        └──────────────────────────────────┘
```

## 📁 Arquitectura de Carpetas

```
restaurante_app/
│
├── modelos/                    ← Capa de Datos (Entity Layer)
│   ├── __init__.py
│   ├── producto.py            → Define clase Producto
│   └── cliente.py             → Define clase Cliente
│
├── servicios/                  ← Capa de Lógica (Business Logic Layer)
│   ├── __init__.py
│   └── restaurante.py         → Define clase Restaurante (gestor central)
│
├── main.py                     ← Capa de Presentación (Presentation Layer)
│
├── casos_avanzados.py          ← Casos de uso adicionales
│
└── __init__.py
```

## 🔄 Flujo de Interacción

```
main.py
   │
   ├─► Importa Producto desde modelos
   │
   ├─► Importa Cliente desde modelos
   │
   └─► Importa Restaurante desde servicios
          │
          └─► servicios/restaurante.py
               │
               └─► Importa Producto y Cliente desde modelos
```

## 📝 Secuencia de Ejecución

```
1. Crear Restaurante
   ↓
2. Registrar Productos
   ├── Producto 1: Ceviche
   ├── Producto 2: Bebida
   └── Producto N: ...
   ↓
3. Registrar Clientes
   ├── Cliente 1: Juan
   ├── Cliente 2: María
   └── Cliente N: ...
   ↓
4. Listar Menú (productos disponibles)
   ↓
5. Listar Clientes
   ↓
6. Crear Pedidos
   ├── Obtener cliente
   ├── Validar disponibilidad de productos
   ├── Calcular total
   └── Registrar en historial del cliente
   ↓
7. Mostrar información detallada
```

## 🔑 Relaciones entre Clases

### Producto ↔ Restaurante
```
RELACIÓN: "Un Restaurante tiene MUCHOS Productos"

- Restaurante.productos: list[Producto]
- Restaurante.registrar_producto(producto): bool
- Restaurante.obtener_producto_por_nombre(nombre): Producto
- Restaurante.listar_productos(): str
```

### Cliente ↔ Restaurante
```
RELACIÓN: "Un Restaurante tiene MUCHOS Clientes"

- Restaurante.clientes: list[Cliente]
- Restaurante.registrar_cliente(cliente): bool
- Restaurante.obtener_cliente_por_email(email): Cliente
- Restaurante.listar_clientes(): str
```

### Producto ↔ Cliente (a través de Pedidos)
```
RELACIÓN: "Un Cliente realiza MUCHOS Pedidos con MUCHOS Productos"

- Cliente.historial_pedidos: list[dict]
- Cliente.registrar_pedido(id_pedido, monto_total)
- Restaurante.crear_pedido(cliente, productos): dict
```

## 📊 Ciclo de Vida de Objetos

### Producto
```
Creación → Registro en Restaurante → Consulta en Menú → 
Aplicación de Descuentos → Cambio de Disponibilidad → 
Utilización en Pedidos
```

### Cliente
```
Creación → Registro en Restaurante → Consulta → 
Realización de Pedidos → Actualización de Historial →
Cálculo de Gastos Totales
```

### Restaurante
```
Creación → Registro de Productos → Registro de Clientes →
Consultas y Listados → Creación de Pedidos → 
Gestión Completa del Sistema
```

## 🎯 Responsabilidades por Módulo

### modelos/producto.py
- ✓ Definir estructura de un producto
- ✓ Gestionar atributos del producto
- ✓ Mostrar información formateada (__str__())
- ✓ Cambiar disponibilidad
- ✓ Aplicar descuentos

### modelos/cliente.py
- ✓ Definir estructura de un cliente
- ✓ Gestionar atributos del cliente
- ✓ Mostrar información formateada (__str__())
- ✓ Cambiar estado activo/inactivo
- ✓ Registrar pedidos
- ✓ Calcular total gastado

### servicios/restaurante.py
- ✓ Gestionar colección de productos
- ✓ Gestionar colección de clientes
- ✓ Validar información única (sin duplicados)
- ✓ Buscar productos y clientes
- ✓ Crear y gestionar pedidos
- ✓ Mostrar información completa del restaurante

### main.py
- ✓ Crear instancias de objetos
- ✓ Demonstrar funcionalidades del sistema
- ✓ Presentar información en consola
- ✓ Ejecutar el programa

## 💡 Patrones de Diseño Utilizados

### 1. **Patrón Modelo-Servicio**
- **Modelos** (producto.py, cliente.py): Representan entidades
- **Servicios** (restaurante.py): Gestión de lógica de negocio

### 2. **Patrón Repository**
- La clase Restaurante actúa como repositorio central
- Gestiona colecciones de productos y clientes

### 3. **Patrón Facade**
- La clase Restaurante proporciona interfaz simple
- Oculta complejidad de búsquedas y validaciones

## 🔍 Ejemplos de Implementación

### Creación de Objetos
```python
# Crear producto
producto = Producto("Ceviche", "Fresco", 25.00, "platos_principales")

# Crear cliente
cliente = Cliente("Juan", "juan@email.com", "0987654321", "Puyo")

# Crear restaurante
restaurante = Restaurante("El Sabor", "Puyo")
```

### Registros
```python
restaurante.registrar_producto(producto)  # Retorna True/False
restaurante.registrar_cliente(cliente)    # Retorna True/False
```

### Búsquedas
```python
prod = restaurante.obtener_producto_por_nombre("Ceviche")
cli = restaurante.obtener_cliente_por_email("juan@email.com")
```

### Creación de Pedidos
```python
pedido = restaurante.crear_pedido(
    cliente,
    [("Ceviche", 2), ("Bebida", 1)]
)
```

## 📌 Características Destacadas

| Característica | Implementación |
|----------------|----------------|
| **Validación de Duplicados** | Búsqueda en listas antes de registrar |
| **Case-Insensitive** | Convertir a minúsculas en búsquedas |
| **Generación de IDs** | Contador automático para pedidos (PED-0001, PED-0002...) |
| **Cálculo de Totales** | Multiplica cantidad × precio por cada item |
| **Historial de Pedidos** | Lista de diccionarios en cada cliente |
| **Estado Activo/Inactivo** | Control de acceso a pedidos |
| **Métodos Especiales** | __str__() para representación legible |
| **Organización Modular** | Separación clara de responsabilidades |

## 🚀 Cómo Extender el Sistema

Para agregar nuevas funcionalidades:

1. **Agregar Atributo a Producto**
   - Editar `__init__()` en producto.py
   - Actualizar `__str__()`

2. **Agregar Método a Cliente**
   - Implementar en cliente.py
   - Utilizar en restaurante.py si es necesario

3. **Agregar Operación en Restaurante**
   - Implementar en servicios/restaurante.py
   - Importar en main.py si es necesario

## ⚙️ Validaciones Implementadas

```
PRODUCTO
├─ Verificar nombre único (case-insensitive)
├─ Validar precio > 0
└─ Validar disponibilidad antes de usar en pedido

CLIENTE
├─ Verificar email único (case-insensitive)
├─ Validar estado activo antes de crear pedido
└─ Mantener historial de pedidos

RESTAURANTE
├─ No permitir productos duplicados
├─ No permitir clientes con email duplicado
└─ Validar que productos estén disponibles en pedidos
```

---

**Documento generado para: Programación Orientada a Objetos - Semana 4**

