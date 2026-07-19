# Sistema de Restaurante - Aplicación de Principios SOLID

## Información del Estudiante
**Nombre:** Calderón Dayvis  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 8  
**Tema:** Aplicación de Principios SOLID en Proyectos Modulares

---

## Descripción del Sistema

El **Sistema de Restaurante** es una aplicación de consola que demuestra la aplicación práctica de los principios SOLID en Python. El sistema permite registrar y gestionar productos, bebidas y clientes de un restaurante mediante un menú interactivo.

El proyecto mantiene una arquitectura modular clara que separa responsabilidades entre modelos (representación de datos) y servicios (lógica de negocio), siendo la interacción con el usuario responsabilidad de `main.py`.

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase base Producto
│   ├── bebida.py            # Clase Bebida (hereda de Producto)
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante (servicio principal)
└── main.py                  # Punto de entrada y menú interactivo
```

---

## Responsabilidad de Cada Clase

### 📦 **modelos/producto.py**
- **Clase:** `Producto`
- **Responsabilidad:** Representar un producto genérico del restaurante
- **Atributos:** `codigo`, `nombre`, `categoria`, `precio`
- **Métodos principales:**
  - `mostrar_informacion()`: Retorna información formateada del producto
  - `obtener_codigo()`: Retorna el código único del producto

### 🥤 **modelos/bebida.py**
- **Clase:** `Bebida` (hereda de `Producto`)
- **Responsabilidad:** Representar una bebida con atributos específicos
- **Atributos adicionales:** `tamaño`, `tipo_envase`
- **Métodos principales:**
  - `mostrar_informacion()`: Sobrescribe el método base para incluir información de bebida

### 👤 **modelos/cliente.py**
- **Clase:** `Cliente`
- **Responsabilidad:** Representar la información de un cliente registrado
- **Atributos:** `identificacion`, `nombre`, `correo`
- **Métodos principales:**
  - `mostrar_informacion()`: Retorna información formateada del cliente
  - `obtener_identificacion()`: Retorna la identificación del cliente

### 🍽️ **servicios/restaurante.py**
- **Clase:** `Restaurante`
- **Responsabilidad:** Administrar colecciones de productos y clientes
- **Funcionalidades principales:**
  - Registrar productos y bebidas en una misma lista
  - Validar códigos duplicados
  - Registrar y validar clientes
  - Listar productos usando polimorfismo
  - Aplicar políticas de negocio (validaciones)

### 🎮 **main.py**
- **Responsabilidad:** Interacción con el usuario y coordinación del programa
- **Funcionalidades:**
  - Mostrar el menú interactivo
  - Solicitar información del usuario mediante `input()`
  - Crear objetos basados en los datos ingresados
  - Llamar a métodos del servicio Restaurante
  - Mostrar resultados al usuario

---

## Relación entre Producto y Bebida

### Herencia y Composición

```
Producto (clase base)
    ↓
    └─→ Bebida (especialización)
```

La clase `Bebida` hereda de `Producto` porque conceptualmente una bebida **ES UN** tipo de producto. Esta relación permite:

1. **Reutilizar código:** Bebida hereda atributos como `codigo`, `nombre`, `categoria` y `precio`
2. **Especialización:** Bebida agrega atributos específicos como `tamaño` y `tipo_envase`
3. **Polimorfismo:** Ambas pueden almacenarse en la misma lista y llamar a `mostrar_informacion()`

### Ventajas de esta Arquitectura

- ✅ No se requieren listas separadas para productos y bebidas
- ✅ El servicio no necesita condicionales `if isinstance()` para distinguir tipos
- ✅ Nuevos tipos de productos pueden agregarse sin modificar código existente
- ✅ El comportamiento es coherente y predecible

---

## Principios SOLID Aplicados

### **S — Single Responsibility Principle (Responsabilidad Única)**

Cada clase tiene una única razón para cambiar:

| Clase | Responsabilidad |
|-------|-----------------|
| `Producto` | Representar datos de un producto |
| `Bebida` | Extender Producto con información específica de bebidas |
| `Cliente` | Representar datos de un cliente |
| `Restaurante` | Administrar colecciones y validaciones |
| `main.py` | Interacción con el usuario |

**Ejemplo:** Si cambia el formato de mostrar precios, solo modificamos `Producto.mostrar_informacion()`, no toda la aplicación.

### **O — Open/Closed Principle (Abierto/Cerrado)**

El sistema está:
- **Abierto para extensión:** Se puede crear `Platillo`, `Postre`, etc. heredando de `Producto` sin modificar clases existentes
- **Cerrado para modificación:** Agregar `Bebida` no requirió cambiar `Producto`, `Restaurante` ni `main.py`

**Ejemplo de extensión futura:**
```python
class Platillo(Producto):
    def __init__(self, codigo, nombre, categoria, precio, ingredientes, tiempo_preparacion):
        super().__init__(codigo, nombre, categoria, precio)
        self.ingredientes = ingredientes
        self.tiempo_preparacion = tiempo_preparacion
    
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} | Tiempo: {self.tiempo_preparacion} min"
```

Sin modificar el `Restaurante`, este simplemente aceptaría `Platillo` en `registrar_producto()`.

### **L — Liskov Substitution Principle (Sustitución de Liskov)**

Cualquier `Bebida` puede ser usado donde se espera un `Producto` sin alterar el comportamiento:

```python
# En Restaurante.registrar_producto()
def registrar_producto(self, producto: Producto) -> tuple[bool, str]:
    # Este método acepta Producto O Bebida transparentemente
    # porque Bebida cumple el contrato de Producto
    if self._codigo_existe(producto.obtener_codigo()):
        return False, f"Error: El código '{producto.obtener_codigo()}' ya existe."
    
    self.productos.append(producto)
    return True, f"Producto registrado exitosamente: {producto.nombre}"
```

```python
# En Restaurante.listar_productos()
def listar_productos(self) -> List[str]:
    # Mismo método, sin condicionales para distinguir tipos
    resultado = []
    for producto in self.productos:
        # Polimorfismo: cada objeto ejecuta su propia versión
        resultado.append(producto.mostrar_informacion())
    return resultado
```

**Ventaja:** Si reemplazamos `Bebida` con cualquier otra subclase de `Producto`, todo sigue funcionando.

---

## Menú Interactivo

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Salir
========================================
```

### Opciones del Menú

| Opción | Función | Descripción |
|--------|---------|-------------|
| 1 | `registrar_producto()` | Crea y registra un Producto |
| 2 | `registrar_bebida()` | Crea y registra una Bebida |
| 3 | `registrar_cliente()` | Crea y registra un Cliente |
| 4 | `listar_productos()` | Muestra todos los productos usando polimorfismo |
| 5 | `listar_clientes()` | Muestra todos los clientes |
| 6 | N/A | Cierra el programa |

---

## Validaciones Implementadas

### Productos y Bebidas
- ✅ Los códigos deben ser únicos
- ✅ No se permiten campos vacíos
- ✅ Los precios deben ser números válidos y no negativos

### Clientes
- ✅ Las identificaciones deben ser únicas
- ✅ No se permiten campos vacíos

---

## Instrucciones de Ejecución

### Requisitos
- Python 3.7 o superior
- No requiere dependencias externas

### Pasos para Ejecutar

1. **Navegar a la carpeta del proyecto:**
   ```bash
   cd restaurante_app
   ```

2. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

3. **Interactuar con el menú:**
   - Ingresar el número de la opción deseada
   - Seguir las instrucciones en pantalla
   - Ingresar datos cuando se solicite
   - Seleccionar opción 6 para salir

### Ejemplo de Uso

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
...

Ingrese su opción: 1

--- Registrar Producto ---
Código del producto: P001
Nombre del producto: Hamburguesa
Categoría del producto: Comida Rápida
Precio del producto ($): 8.50
Producto registrado exitosamente: Hamburguesa

Ingrese su opción: 2

--- Registrar Bebida ---
Código de la bebida: B001
Nombre de la bebida: Refresco de Cola
Categoría de la bebida: Bebidas
Precio de la bebida ($): 2.00
Tamaño (pequeño/mediano/grande): mediano
Tipo de envase (vaso/botella/lata): vaso
Bebida registrada exitosamente: Refresco de Cola

Ingrese su opción: 4

--- Productos Registrados ---
Código: P001 | Nombre: Hamburguesa | Categoría: Comida Rápida | Precio: $8.50
Código: B001 | Nombre: Refresco de Cola | Categoría: Bebidas | Precio: $2.00 | Tamaño: mediano | Envase: vaso

Total de productos: 2
```

---

## Reflexión sobre Diseño Modular y Mantenibilidad

### Importancia de Proyectos Mantenibles

Un proyecto mantenible es aquel que puede ser:

1. **Modificado sin efectos secundarios:** Cambiar una clase no rompe otras
2. **Extendido fácilmente:** Agregar nuevas funcionalidades no requiere reescribir código existente
3. **Entendido rápidamente:** Nombres claros y responsabilidades definidas facilitan la comprensión
4. **Testeado efectivamente:** Código modular se puede probar en unidades pequeñas

### Beneficios en Este Proyecto

- **Responsabilidad Clara:** Cada clase tiene un propósito único y bien definido
- **Bajo Acoplamiento:** Las clases no dependen directamente unas de otras innecesariamente
- **Alto Cohesión:** El código relacionado está agrupado en módulos lógicos
- **Reutilización:** `Bebida` reutiliza código de `Producto` sin duplicación
- **Escalabilidad:** Agregar `Platillo`, `Postre`, etc. es sencillo

### Diferencia: Código Monolítico vs. Modular

#### ❌ Malo (Monolítico)
```python
# todo en un archivo
class Sistema:
    def __init__(self):
        self.productos = []
        self.clientes = []
    
    def registrar_producto(self, codigo, nombre, categoria, precio):
        # validaciones
        # agregar a lista
        pass
    
    def mostrar_productos(self):
        # mostrar productos y bebidas
        for p in self.productos:
            if p.tipo == "bebida":
                # código específico para bebidas
            else:
                # código genérico
        pass
```

#### ✅ Bueno (Modular)
```
modelos/
├── producto.py     # Responsabilidad: representar producto
├── bebida.py       # Responsabilidad: extender producto
└── cliente.py      # Responsabilidad: representar cliente

servicios/
└── restaurante.py  # Responsabilidad: administrar colecciones

main.py            # Responsabilidad: interacción
```

### Conclusión

Un proyecto bien diseñado es una inversión en el futuro. Aunque requiere más tiempo inicial, los beneficios en mantenibilidad, reutilización y escalabilidad justifican ampliamente el esfuerzo.

---

## Características Adicionales

- ✅ **Anotaciones de tipos:** Todos los métodos incluyen anotaciones de tipos (`str`, `float`, `List`, etc.)
- ✅ **Docstrings completos:** Cada clase y método está documentado
- ✅ **Validación de entrada:** Se validan todos los datos ingresados por el usuario
- ✅ **Prevención de duplicados:** Códigos de productos e identificaciones de clientes son únicos
- ✅ **Polimorfismo en acción:** El listado de productos usa polimorfismo sin condicionales

---

## Pruebas Recomendadas

1. Registrar varios productos sin bebidas
2. Registrar bebidas verificando que se mezclen con productos
3. Intentar duplicar códigos y verificar el error
4. Intentar duplicar identificaciones de clientes y verificar el error
5. Listar productos cuando la lista está vacía
6. Listar clientes cuando la lista está vacía
7. Ingresar datos inválidos (precios negativos, campos vacíos)

---

## Conclusión

Este proyecto demuestra cómo aplicar principios SOLID en una aplicación real. La combinación de una arquitectura modular clara, responsabilidades bien definidas y el uso apropiado de herencia y polimorfismo resulta en un código que es fácil de mantener, extender y entender.

---

*Último actualizado: Julio 2026*

