# Documentación Técnica - TareaSemana9

## Descripción del Proyecto

El objetivo de **TareaSemana9** es clonar el software de **TareaSemana8** e implementar **persistencia de datos en archivos JSON** usando una estructura tipo **diccionario**.

## Requisitos Completados

### ✅ Clonación de TareaSemana8
- Se copió la estructura base del sistema de restaurante
- Se mantuvieron los modelos Producto y Cliente
- Se conservó la lógica de validación y gestión

### ✅ Adición de Persistencia JSON
- Implementación de métodos de serialización (`a_diccionario()`)
- Implementación de métodos de deserialización (`desde_diccionario()`)
- Creación del módulo `GestorDatos` para manejar I/O de JSON

### ✅ Estructura de Diccionarios
Los datos se guardan como diccionarios con la siguiente estructura:

**Productos**
```python
{
    "codigo": "P001",           # Identificador único
    "nombre": "Pizza",          # Nombre del producto
    "categoria": "Platos",      # Categoría
    "precio": 12.50,            # Precio numérico
    "tipo": "Producto"          # Tipo de documento
}
```

**Clientes**
```python
{
    "identificacion": "1234567890",  # ID único
    "nombre": "Juan Pérez",          # Nombre completo
    "correo": "juan@example.com"     # Email
}
```

## Arquitectura del Sistema

### 1. Capa de Modelos (`modelos/`)

**producto.py**
```python
class Producto:
    - codigo (str)
    - nombre (str)
    - categoria (str)
    - precio (float)
    
    Métodos especiales:
    - a_diccionario() → dict
    - desde_diccionario(dict) → Producto
```

**cliente.py**
```python
class Cliente:
    - identificacion (str)
    - nombre (str)
    - correo (str)
    
    Métodos especiales:
    - a_diccionario() → dict
    - desde_diccionario(dict) → Cliente
```

### 2. Capa de Servicios (`servicios/`)

**restaurante.py**
```python
class Restaurante:
    - productos: List[Producto]
    - clientes: List[Cliente]
    
    Métodos:
    - registrar_producto(Producto) → (bool, str)
    - registrar_cliente(Cliente) → (bool, str)
    - listar_productos() → List[str]
    - listar_clientes() → List[str]
    - obtener/establecer para persistencia
```

**gestor_datos.py** (NUEVO)
```python
class GestorDatos:
    - ruta_productos: str
    - ruta_clientes: str
    
    Métodos de Productos:
    - guardar_productos(List[Producto]) → (bool, str)
    - cargar_productos() → (bool, List[Producto], str)
    
    Métodos de Clientes:
    - guardar_clientes(List[Cliente]) → (bool, str)
    - cargar_clientes() → (bool, List[Cliente], str)
    
    Métodos Generales:
    - eliminar_archivos() → (bool, str)
```

### 3. Capa de Presentación (`main.py`)

Interfaz interactiva con:
- Menú principal con 8 opciones
- Funciones de entrada/validación
- Integración con servicios
- Gestión de persistencia JSON

## Flujo de Datos

```
ENTRADA (Usuario)
        ↓
    VALIDACIÓN
        ↓
CREAR OBJETOS (Producto/Cliente)
        ↓
    GESTIONAR EN MEMORIA (Restaurante)
        ↓
OPCION: ¿GUARDAR?
        ├→ SI: Convertir a diccionario → JSON → Archivo
        └→ NO: Mantener en memoria
```

## Métodos de Serialización

### Serialización (Objeto → JSON)

```python
# 1. Crear objeto
producto = Producto("P001", "Pizza", "Platos", 12.50)

# 2. Convertir a diccionario
diccionario = producto.a_diccionario()
# Resultado: {"codigo": "P001", "nombre": "Pizza", ...}

# 3. Guardar con GestorDatos
gestor = GestorDatos()
gestor.guardar_productos([producto])
# Escribe en datos/productos.json
```

### Deserialización (JSON → Objeto)

```python
# 1. Cargar desde gestor
gestor = GestorDatos()
exito, productos, msg = gestor.cargar_productos()

# 2. GestorDatos convierte:
# - Lee JSON
# - Parsea diccionarios
# - Llama Producto.desde_diccionario()

# 3. Resultado: List[Producto] en memoria
for producto in productos:
    print(producto.mostrar_informacion())
```

## Archivos del Proyecto

```
TareaSemana9/
│
├── restaurante_app/
│   ├── __init__.py
│   ├── main.py                      # Interfaz principal
│   ├── pruebas.py                   # Script de pruebas
│   ├── README.md                    # Documentación de uso
│   │
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py              # Modelo con serialización
│   │   └── cliente.py               # Modelo con serialización
│   │
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── restaurante.py           # Servicio de negocio
│   │   └── gestor_datos.py          # Servicio de persistencia (NUEVO)
│   │
│   └── datos/                       # Se crea automáticamente
│       ├── productos.json           # Productos guardados
│       └── clientes.json            # Clientes guardados
│
└── README.md                        # Este archivo

```

## Principios SOLID Aplicados

### Single Responsibility Principle (SRP)
- **Modelos**: Solo representan datos
- **Restaurante**: Solo gestiona lógica de negocio
- **GestorDatos**: Solo maneja persistencia
- **Main**: Solo coordina interfaz

### Open/Closed Principle (OCP)
- Se puede extender con nuevos tipos de datos sin modificar existentes
- Métodos `a_diccionario()` y `desde_diccionario()` permiten extensión

### Dependency Inversion Principle (DIP)
- Las clases dependen de abstracciones (métodos)
- No de implementaciones específicas

## Pruebas Realizadas

✅ **Prueba 1**: Creación de modelos y conversión a diccionarios  
✅ **Prueba 2**: Persistencia de datos en JSON  
✅ **Prueba 3**: Carga de datos desde JSON  
✅ **Prueba 4**: Validación de duplicados  
✅ **Prueba 5**: Estructura JSON correcta  

Ejecutar: `python pruebas.py`

## Diferencias con TareaSemana8

| Característica | Semana 8 | Semana 9 |
|---|---|---|
| Almacenamiento | Solo en memoria | Memoria + JSON |
| Persistencia | ❌ No | ✅ Sí |
| Método guardar | ❌ No | ✅ gestor.guardar_productos() |
| Método cargar | ❌ No | ✅ gestor.cargar_productos() |
| Serialización | ❌ No | ✅ a_diccionario() |
| Deserialización | ❌ No | ✅ desde_diccionario() |
| GestorDatos | ❌ No | ✅ Nuevo módulo |
| Opciones menú | 6 | 8 |

## Cómo Usar

### Ejecutar el programa interactivo
```bash
cd restaurante_app
python main.py
```

### Ejecutar pruebas
```bash
cd restaurante_app
python pruebas.py
```

### Usar la librería en otro proyecto
```python
from modelos.producto import Producto
from servicios.restaurante import Restaurante
from servicios.gestor_datos import GestorDatos

# Crear datos
r = Restaurante()
g = GestorDatos()

p = Producto("P001", "Pizza", "Platos", 12.50)
r.registrar_producto(p)

# Guardar
g.guardar_productos(r.obtener_productos())

# Cargar
_, productos, _ = g.cargar_productos()
```

## Notas Técnicas

- **Codificación**: UTF-8 para caracteres especiales
- **Indentación JSON**: 4 espacios para legibilidad
- **Validación**: Duplicados prevenidos por código/identificación
- **Ruta JSON**: `datos/` relativa al script ejecutable

## Mejoras Futuras Sugeridas

1. **Búsqueda avanzada**: Filtrar por categoría
2. **CRUD completo**: Actualizar y eliminar registros
3. **Historial**: Guardar cambios anteriores
4. **Validación email**: Verificar formato de correo
5. **Exportar CSV**: Alternativa a JSON
6. **Interfaz web**: Usando Flask o Django
7. **Base de datos**: Migrar a SQLite/PostgreSQL

## Contacto / Autor

Dayvis Calderón  
Programación Orientada a Objetos  
Universidad Estatal Amazónica  
Agosto 2026

---

**Estado del Proyecto**: ✅ COMPLETADO


