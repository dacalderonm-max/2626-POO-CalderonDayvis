# Sistema de Restaurante - Tarea Semana 7

**Autor:** Dayvis Calderón  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 7  
**Fecha:** 2026

---

## Descripción del Sistema

Este proyecto implementa un **Sistema de Gestión de Restaurante** que permite registrar, listar y buscar productos y clientes de un restaurante mediante un menú interactivo ejecutado desde consola.

El sistema demuestra la aplicación de conceptos fundamentales de Programación Orientada a Objetos (POO) en Python, tales como:

- **Constructores tradicionales** (`__init__`)
- **Decoradores** (`@property`, `@setter`)
- **Clases de datos** (`@dataclass`)
- **Encapsulación** mediante atributos privados (`_atributo`)
- **Arquitectura modular por capas** (modelos, servicios, main)
- **Creación dinámica de objetos** a partir de datos ingresados por el usuario

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto con constructor, @property, @setter
│   └── cliente.py           # Clase Cliente con @dataclass
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante (servicio)
└── main.py                  # Menú interactivo principal
```

### Responsabilidad de cada módulo

**modelos/producto.py**
- Contiene la clase `Producto` implementada con constructor tradicional `__init__()`
- Define atributos: `nombre`, `categoría`, `precio`, `disponible`
- Implementa validaciones mediante `@property` y `@setter`
- Incluye el método `mostrar_informacion()` para presentar datos legibles

**modelos/cliente.py**
- Contiene la clase `Cliente` implementada mediante `@dataclass`
- Define atributos: `nombre`, `correo`, `id_cliente`
- Incluye validaciones en `__post_init__()`
- Implementa el método `mostrar_informacion()`

**servicios/restaurante.py**
- Contiene la clase `Restaurante` que funciona como servicio
- Administra dos listas: `_productos` y `_clientes`
- Implementa métodos para registrar, listar y buscar registros
- Proporciona métodos de consulta como `contar_productos()` y `contar_clientes()`

**main.py**
- Punto de entrada del programa
- Implementa un menú interactivo que solicita datos al usuario
- Transforma inputs en objetos mediante los constructores
- Ejecuta métodos del servicio `Restaurante`

---

## Constructor en la Clase Producto

La clase `Producto` utiliza un **constructor tradicional** que recibe los datos necesarios para crear una instancia:

```python
def __init__(self, nombre, categoria, precio, disponible=True):
    self._nombre = nombre
    self._categoria = categoria
    self._precio = precio
    self._disponible = disponible
```

**Importancia:** El constructor establece el estado inicial del objeto y permite que se cree a partir de valores proporcionados, ya sea de forma directa en el código o a través de entrada del usuario.

---

## Uso de @property y @setter

La clase `Producto` implementa decoradores `@property` y `@setter` para controlar el acceso y modificación de atributos con validaciones:

### Ejemplo: Propiedad `nombre`

```python
@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, valor):
    if not valor or not valor.strip():
        raise ValueError("El nombre del producto no puede estar vacío")
    self._nombre = valor.strip()
```

### Validaciones Implementadas

| Atributo | Validación |
|----------|-----------|
| `nombre` | No puede estar vacío |
| `categoria` | No puede estar vacía |
| `precio` | Debe ser mayor que cero |
| `disponible` | Se convierte a booleano |

**Beneficio:** Los `@property` y `@setter` permiten encapsular la lógica de validación, evitando que datos inválidos se asignen a los atributos.

---

## Uso de @dataclass en la Clase Cliente

La clase `Cliente` implementa el decorador `@dataclass` para simplificar la definición de clases que almacenan datos:

```python
from dataclasses import dataclass, field

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str = field(default_factory=lambda: "")
    
    def __post_init__(self):
        # Validaciones
        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío")
```

**Ventajas de @dataclass:**
- Genera automáticamente el método `__init__()`
- Simplifica la definición de atributos
- Incluye implementaciones automáticas de `__repr__()` y `__eq__()`
- Permite usar `__post_init__()` para validaciones adicionales

---

## Menú Interactivo

El menú principal presenta las siguientes opciones:

```
========================================
        SISTEMA DE RESTAURANTE
========================================

--- MENÚ PRINCIPAL ---
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Ver resumen del restaurante
8. Salir
```

### Flujo de Funcionamiento

1. El usuario selecciona una opción
2. El sistema solicita datos mediante `input()`
3. Los datos ingresados se validan
4. Se crea un objeto usando el constructor correspondiente
5. El objeto se registra en el servicio `Restaurante`
6. Se muestra el resultado al usuario

---

## Importancia de Crear Objetos a partir de Datos Ingresados

### Principios Demostrados

**1. Separación de Responsabilidades**
- El `main.py` se encarga de la interacción con el usuario
- Los `modelos` definen la estructura de datos
- El `servicio` administra colecciones de objetos

**2. Validación en Tiempo de Creación**
- Los datos ingresan como strings
- El constructor valida y transforma los datos
- Solo objetos válidos se almacenan en el servicio

**3. Reutilización de Código**
- La misma clase `Producto` se puede usar en diferentes contextos
- Los datos pueden venir del usuario, archivos o bases de datos
- El comportamiento del objeto es consistente

**4. Comprensión del Ciclo de Vida**
- **Entrada:** `input()` del usuario
- **Procesamiento:** Constructor del modelo
- **Almacenamiento:** Registro en la clase Restaurante
- **Consulta:** Listado o búsqueda de registros

**5. Aplicación Práctica de POO**
- Los objetos no son estáticos ni quemados en el código
- Se crean dinámicamente según necesidades del usuario
- Cada objeto es independiente e identificable
- El sistema es flexible y escalable

---

## Cómo Ejecutar el Programa

1. Navegar a la carpeta del proyecto:
   ```bash
   cd restaurante_app
   ```

2. Ejecutar el archivo principal:
   ```bash
   python main.py
   ```

3. Seguir las instrucciones del menú interactivo.

---

## Ejemplos de Uso

### Ejemplo 1: Registrar un Producto
```
1. Registrar producto
Nombre del producto: Pasta Carbonara
Categoría del producto: Platos Principales
Precio del producto: 12.50
¿Está disponible? (s/n, default: s): s
✅ Producto 'Pasta Carbonara' registrado exitosamente
```

### Ejemplo 2: Registrar un Cliente
```
4. Registrar cliente
Nombre del cliente: Juan Pérez
Correo del cliente: juan@email.com
ID del cliente (opcional): C001
✅ Cliente 'Juan Pérez' registrado exitosamente
```

### Ejemplo 3: Listar Productos
```
2. Listar productos
Total de productos: 1

1. Pasta Carbonara - $12.50 (Platos Principales)
   Información detallada:
   Nombre: Pasta Carbonara
   Categoría: Platos Principales
   Precio: $12.50
   Estado: Disponible
```

---

## Validaciones Implementadas

El sistema implementa validaciones robustas:

- ✅ Nombres no vacíos
- ✅ Categorías no vacías
- ✅ Precios mayores a cero
- ✅ Correos no vacíos
- ✅ Búsquedas con coincidencia parcial (case-insensitive)
- ✅ Manejo de excepciones para datos inválidos

---

## Conclusión

Este proyecto demuestra la importancia de:

1. **Estructura modular:** Facilita el mantenimiento y escalabilidad
2. **Constructores efectivos:** Garantizan objetos bien inicializados
3. **Decoradores (@property, @setter, @dataclass):** Proporcionan seguridad y claridad
4. **Creación dinámica de objetos:** Permite que el sistema sea flexible y responsivo
5. **Validación de datos:** Asegura la integridad del sistema

La arquitectura implementada es profesional, reutilizable y sigue las mejores prácticas de Programación Orientada a Objetos en Python.

---

**Fin del documento**

