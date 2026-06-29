# Sistema de Gestión de Restaurante "El Sabor Zapotillano"

## Información del Estudiante

**Nombre Completo:** Dayvis Calderón  
**Asignatura:** Programación Orientada a Objetos (POO)  
**Semana:** 5  
**Tema:** Aplicación de Identificadores y Tipos de Datos en Proyecto Modular Python

---

## Descripción del Sistema

Este proyecto implementa un sistema básico de gestión de restaurante denominado **"El Sabor Zapotillano"**, ubicado en Loja-Zapotillo, Ecuador. El sistema demuestra el uso correcto de identificadores descriptivos, tipos de datos básicos, listas como tipo compuesto, y organización modular en Python.

El sistema permite:
- **Registrar productos** (platos, bebidas y postres) con información detallada
- **Registrar clientes** del restaurante con información de contacto
- **Gestionar disponibilidad** de productos
- **Calcular precios** con IVA incluido
- **Gestionar descuentos** para clientes frecuentes
- **Mostrar información** de forma organizada en consola

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py              # Exporta Producto y Cliente
│   ├── producto.py              # Clase Producto
│   └── cliente.py               # Clase Cliente
├── servicios/
│   ├── __init__.py              # Exporta Restaurante
│   └── restaurante.py           # Clase Restaurante
└── main.py                      # Punto de entrada del programa
```

### Responsabilidad de cada módulo

**modelos/producto.py**
- Clase `Producto`: Representa artículos disponibles en el restaurante
- Almacena información sobre platos, bebidas y postres

**modelos/cliente.py**
- Clase `Cliente`: Representa personas registradas en el sistema
- Gestiona información de contacto y estado de membresía

**servicios/restaurante.py**
- Clase `Restaurante`: Administra listas de productos y clientes
- Proporciona métodos para registrar, buscar y listar entidades

**main.py**
- Punto de entrada del programa
- Crea instancias de objetos y demuestra la funcionalidad del sistema

---

## Tipos de Datos Utilizados

### En la clase Producto:
- **`nombre: str`** - Nombre descriptivo del producto
- **`descripcion: str`** - Descripción detallada
- **`precio: float`** - Precio en dólares (con decimales)
- **`categoria: str`** - Categoría del producto (e.g., "Platos Principales")
- **`disponible: bool`** - Estado de disponibilidad (True/False)

### En la clase Cliente:
- **`nombre_completo: str`** - Nombre completo de la persona
- **`email: str`** - Correo electrónico único
- **`numero_telefono: str`** - Número de teléfono
- **`es_miembro_frecuente: bool`** - Estado de membresía
- **`numero_ordenes: int`** - Cantidad de órdenes realizadas

### En la clase Restaurante:
- **`nombre: str`** - Nombre del restaurante
- **`ubicacion: str`** - Ubicación geográfica
- **`productos: list[Producto]`** - Lista de productos disponibles
- **`clientes: list[Cliente]`** - Lista de clientes registrados
- **`contador_pedidos: int`** - Contador de pedidos totales

---

## Convenciones de Nombres Aplicadas

### PascalCase (Clases)
- `Producto`
- `Cliente`
- `Restaurante`

### snake_case (Variables, atributos, métodos)
- `nombre_completo`
- `es_miembro_frecuente`
- `registrar_producto()`
- `listar_clientes()`
- `obtener_descuento()`

---

## Métodos Especiales Implementados

### Método `__init__()` (Constructor)
Presente en todas las clases principales para inicializar atributos.

### Método `__str__()` (Representación en texto)
- **Producto**: Retorna información formateada del producto
- **Cliente**: Retorna datos personales y estadísticas
- **Restaurante**: Retorna resumen del restaurante

---

## Funcionalidades Principales

### Clase Producto
- `cambiar_disponibilidad()` - Modifica el estado del producto
- `obtener_precio_con_iva()` - Calcula precio con IVA (12%)

### Clase Cliente
- `registrar_orden()` - Incrementa contador de órdenes
- `promover_a_miembro_frecuente()` - Cambia estado de membresía
- `obtener_descuento()` - Retorna descuento aplicable (10% si es frecuente)

### Clase Restaurante
- `registrar_producto()` - Agrega producto a la lista
- `registrar_cliente()` - Agrega cliente a la lista
- `obtener_producto_por_nombre()` - Busca producto por nombre
- `obtener_cliente_por_email()` - Busca cliente por email
- `listar_productos()` - Muestra productos organizados por categoría
- `listar_clientes()` - Muestra información de clientes

---

## Importaciones Utilizadas

El proyecto utiliza importaciones de forma correcta entre módulos:

```python
# En servicios/restaurante.py
from modelos import Cliente, Producto

# En main.py
from modelos import Producto, Cliente
from servicios import Restaurante
```

---

## Reflexión: Importancia de Identificadores, Tipos de Datos y Listas

### Identificadores Descriptivos
El uso de identificadores claros y significativos es fundamental para la comprensión y mantenimiento del código. Por ejemplo:
- `es_miembro_frecuente` es mucho más claro que `miembro` o `flag`
- `numero_ordenes` comunica claramente qué se está contando
- `registrar_cliente()` es más explícito que `agregar()` o `add()`

Esto facilita el trabajo en equipo, la depuración y la evolución futura del código.

### Tipos de Datos Adecuados
Seleccionar tipos de datos correctos es crucial:
- **`float`** para precios (no `int`) asegura precisión con decimales
- **`bool`** para disponibilidad evita ambigüedad ("1" vs "sí" vs `True`)
- **`int`** para contadores garantiza operaciones matemáticas corrrectas
- **`str`** para nombres y descripciones es la elección natural

Esto previene errores de lógica, reduce bugs y mejora el rendimiento.

### Listas como Tipo Compuesto
Las listas permiten:
- **Gestionar múltiples objetos** de forma eficiente
- **Iterar fácilmente** sobre colecciones de productos y clientes
- **Mantener orden** de los elementos registrados
- **Aplicar operaciones colectivas** como búsquedas y filtrados

Sin listas, este sistema sería impracticable con una estructura manual.

### Conclusión
La combinación de identificadores descriptivos, tipos de datos apropiados y estructuras de datos como listas, forma la base de código profesional, mantenible y escalable. Python facilita esto con su sintaxis clara y tipado dinámico con anotaciones opcionales.

---

## Requisitos Cumplidos

✓ Estructura modular respetada (modelos, servicios, main.py)  
✓ Dos clases en modelos (Producto, Cliente)  
✓ Una clase en servicios (Restaurante)  
✓ Constructores `__init__()` en todas las clases  
✓ Identificadores descriptivos en todo el código  
✓ Convenciones Python: PascalCase para clases, snake_case para variables  
✓ Tipos de datos básicos: str, int, float, bool  
✓ Listas como tipo compuesto para productos y clientes  
✓ Anotaciones de tipo en atributos y parámetros  
✓ Métodos `__str__()` para representación de objetos  
✓ Importaciones correctas entre módulos  
✓ Dos objetos de cada modelo creados en main.py  
✓ Objetos agregados a listas del servicio principal  
✓ Información mostrada de forma organizada en consola  
✓ Comentarios explicativos en el código  

---

## Instrucciones de Ejecución

1. Navegar a la carpeta del proyecto:
   ```bash
   cd restaurante_app
   ```

2. Ejecutar el programa:
   ```bash
   python main.py
   ```

3. Se mostrará en consola:
   - Información del restaurante
   - Catálogo de productos por categoría
   - Lista de clientes registrados
   - Información adicional sobre descuentos y precios

---

## Autor

**Dayvis Calderón**  
Estudiante de Programación Orientada a Objetos  
Universidad Estatal Amazónica  
2026

