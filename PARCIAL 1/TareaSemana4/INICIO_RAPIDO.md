# 🍽️ SISTEMA DE GESTIÓN DE RESTAURANTE - INICIO RÁPIDO

## 📁 Proyecto Finalizado

Tu proyecto está completamente listo en:
```
C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4\
```

---

## 🚀 Instrucciones de Uso

### Para Ejecutar la Versión Interactiva (RECOMENDADO ⭐)

#### En Windows (PowerShell):
```powershell
cd "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4"
python main_interactivo.py
```

#### En macOS o Linux:
```bash
cd TareaSemana4
python main_interactivo.py
```

---

### Para Ejecutar la Versión de Demostración

#### En Windows (PowerShell):
```powershell
cd "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4"
python main.py
```

---

## 📋 Contenido del Proyecto

### Archivos Principales

#### 1. **main_interactivo.py** ⭐ VERSION INTERACTIVA
- Versión con menú interactivo
- Permite agregar datos manualmente
- 10,024 bytes de código

#### 2. **main.py** - Demostración
- Versión de demostración automática
- Crea datos de ejemplo
- 5,123 bytes de código

#### 3. **modelos/** - Carpeta de Clases:
- **producto.py** (2,629 bytes) - Clase Producto
- **cliente.py** (2,904 bytes) - Clase Cliente
- **__init__.py** - Inicializador del paquete

#### 4. **servicios/** - Carpeta de Servicios:
- **restaurante.py** (6,694 bytes) - Clase Restaurante (Gestor del sistema)
- **__init__.py** - Inicializador del paquete

### Documentación

#### 📖 **README.md** (14,266 bytes)
- Guía completa del proyecto
- Análisis detallado de cada clase
- Conceptos de POO explicados
- Flujo de ejecución
- Validaciones implementadas

#### 📖 **GUIA_PROGRAMA_INTERACTIVO.md** (11,885 bytes)
- Guía de uso del programa interactivo
- Explicación de cada menú
- Ejemplos de uso
- Casos de uso prácticos

#### 📖 **RESUMEN_PROYECTO.md** (4,457 bytes)
- Resumen ejecutivo
- Requisitos cumplidos
- Total de líneas de código

#### 📖 **entrada_ejemplo.txt** (180 bytes)
- Archivo de entrada de ejemplo para pruebas automatizadas

---

## 🎯 Características del Programa Interactivo

### ✅ Menú Principal - 8 Opciones

```
1. Gestionar Productos
   └─ Agregar producto
   └─ Ver productos
   └─ Volver

2. Gestionar Clientes
   └─ Agregar cliente
   └─ Ver clientes
   └─ Volver

3. Realizar Pedido
   └─ Seleccionar cliente
   └─ Agregar productos al pedido
   └─ Procesar pedido

4. Ver Catálogo de Productos
   └─ Muestra todos los productos

5. Ver Clientes Registrados
   └─ Muestra todos los clientes

6. Ver Estadísticas
   └─ Ingresos totales
   └─ Total de clientes
   └─ Total de productos

7. Ver Inventario
   └─ Disponibilidad de cada producto

8. Salir
   └─ Cierra el programa
```

---

## 💼 Cómo Usar el Programa

### Paso 1: Ejecutarlo

```bash
python main_interactivo.py
```

### Paso 2: Crear el Restaurante

```
¿Cuál es el nombre de su restaurante? Mi Restaurante Favorito
✓ Restaurante 'Mi Restaurante Favorito' creado exitosamente.
```

### Paso 3: Agregar Productos

Opción 1 → Gestionar Productos → 1 → Agregar

```
Ingrese el ID del producto: 1
Ingrese el nombre del producto: Hamburguesa
Ingrese la descripción del producto: Hamburguesa con queso y lechuga
Ingrese el precio del producto: $8.99
Ingrese la cantidad disponible: 50
✓ Producto 'Hamburguesa' agregado exitosamente.
```

### Paso 4: Registrar Clientes

Opción 2 → Gestionar Clientes → 1 → Agregar

```
Ingrese el ID del cliente: 101
Ingrese el nombre del cliente: Juan Pérez
Ingrese el email del cliente: juan@email.com
Ingrese el teléfono del cliente: +593-999-1234
✓ Cliente 'Juan Pérez' registrado exitosamente.
```

### Paso 5: Realizar Pedidos

Opción 3 → Realizar Pedido

```
Ingrese el ID del cliente: 101

✓ Cliente: Juan Pérez

Productos disponibles:
  ID: 1 | Hamburguesa - $8.99 (Disponibles: 50)

Ingrese el ID del producto (o 'fin' para terminar): 1
¿Cuántas unidades desea de este producto? 2
✓ Producto agregado al pedido.

Ingrese el ID del producto (o 'fin' para terminar): fin
✓ Pedido realizado exitosamente.
```

### Paso 6: Consultar Información

```
Opción 4 → Ver Catálogo
Opción 5 → Ver Clientes
Opción 6 → Ver Estadísticas
Opción 7 → Ver Inventario
```

### Paso 7: Salir

```
Opción 8 → Salir
¡Gracias por usar el Sistema de Gestión de Restaurante!
```

---

## 📊 Ejemplo de Salida

### Catálogo de Productos
```
======================================================================
CATÁLOGO DE PRODUCTOS - Mi Restaurante
======================================================================
• Producto: Hamburguesa | Descripción: Con queso y lechuga | Precio: $8.99 | Disponibles: 50
• Producto: Pizza | Descripción: Margherita fresca | Precio: $12.99 | Disponibles: 30
======================================================================
```

### Clientes Registrados
```
======================================================================
CLIENTES REGISTRADOS - Mi Restaurante
======================================================================
• Cliente: Juan Pérez | Email: juan@email.com | Teléfono: +593-999-1234 | Monto gastado: $25.48
• Cliente: María García | Email: maria@email.com | Teléfono: +593-998-5678 | Monto gastado: $28.50
======================================================================
```

### Estadísticas
```
======================================================================
ESTADÍSTICAS - Mi Restaurante
======================================================================
Total de Productos: 2
Total de Clientes: 2
Ingresos Totales: $53.98
======================================================================
```

---

## 🔧 Requisitos Técnicos

- **Python**: 3.6 o superior
- **SO Compatible**: Windows, macOS, Linux
- **Dependencias**: Ninguna (solo librerías estándar de Python)

---

## ✨ Características Destacadas

✅ **Organización Modular**
- Separación clara entre modelos y servicios
- Código reutilizable y mantenible

✅ **POO Completa**
- Clases bien definidas
- Constructores inicializados
- Métodos especiales `__str__()`

✅ **Interfaz Amigable**
- Menú intuitivo
- Mensajes claros
- Validación de datos

✅ **Validaciones Robustas**
- Control de duplicados
- Verificación de inventario
- Manejo de errores

✅ **Documentación Completa**
- Docstrings en todo el código
- 4 archivos de guía y documentación
- Ejemplos de uso

---

## 📚 Documentación Disponible

1. **README.md** - Análisis completo del proyecto
2. **GUIA_PROGRAMA_INTERACTIVO.md** - Manual de uso del programa
3. **RESUMEN_PROYECTO.md** - Resumen ejecutivo
4. **Este archivo** - Instrucciones de inicio rápido

---

## 🎓 Conceptos de POO Demostrados

✓ **Clases y Objetos**
```python
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
```

✓ **Constructor __init__()**
✓ **Atributos de Instancia**
✓ **Métodos de Instancia**
✓ **Método Especial __str__()**
✓ **Importaciones y Módulos**
✓ **Encapsulación**
✓ **Responsabilidad Simple**

---

## 🐛 Solución de Problemas

### El programa no inicia
```bash
# Verifica que estés en el directorio correcto
cd "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4"

# Verifica la versión de Python
python --version

# Intenta ejecutar
python main_interactivo.py
```

### No reconoce las importaciones
```bash
# Verifica que los archivos __init__.py existan
# Deben estar en:
# - modelos/__init__.py
# - servicios/__init__.py
```

---

## 📞 Archivos del Proyecto

```
TareaSemana4/
├── main_interactivo.py          ⭐ EJECUTAR ESTE ARCHIVO
├── main.py                      (Demostración automática)
├── README.md                    (Documentación completa)
├── GUIA_PROGRAMA_INTERACTIVO.md (Manual de uso)
├── RESUMEN_PROYECTO.md          (Resumen ejecutivo)
├── INICIO_RAPIDO.md             (Este archivo)
├── entrada_ejemplo.txt          (Entrada de ejemplo)
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── modelos/__pycache__/
    └── (archivos compilados - ignorar)
```

---

## 🎉 ¡Listo para Usar!

**Ahora puedes ejecutar:**

```bash
python main_interactivo.py
```

**Y comenzar a gestionar tu restaurante de forma interactiva.**

---

**Última actualización**: Junio 18, 2026  
**Estado**: ✅ Completamente Funcional  
**Versión**: 1.0 (Con Menú Interactivo)

