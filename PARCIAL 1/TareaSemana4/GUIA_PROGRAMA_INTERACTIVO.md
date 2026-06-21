# Guía de Uso - Programa Interactivo del Sistema de Gestión de Restaurante

## 📋 Descripción

El programa `main_interactivo.py` es una versión interactiva del sistema de gestión de restaurante que permite al usuario:

- ✅ Crear un restaurante con nombre personalizado
- ✅ Agregar productos manualmente
- ✅ Registrar clientes manualmente
- ✅ Realizar pedidos
- ✅ Consultar información
- ✅ Ver estadísticas

## 🚀 Cómo Ejecutar

### En Windows (PowerShell)
```powershell
cd "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4"
python main_interactivo.py
```

### En macOS o Linux
```bash
cd TareaSemana4
python main_interactivo.py
```

## 📊 Menú Principal

Al ejecutar el programa, verás el siguiente menú:

```
======================================================================
SISTEMA DE GESTIÓN DE RESTAURANTE - MENÚ PRINCIPAL
======================================================================
1. Gestionar Productos
2. Gestionar Clientes
3. Realizar Pedido
4. Ver Catálogo de Productos
5. Ver Clientes Registrados
6. Ver Estadísticas
7. Ver Inventario
8. Salir
======================================================================
```

### Explicación de cada opción:

| Opción | Descripción |
|--------|------------|
| **1** | Accede al menú para agregar o ver productos |
| **2** | Accede al menú para registrar o ver clientes |
| **3** | Permite realizar un nuevo pedido |
| **4** | Muestra el catálogo completo de productos |
| **5** | Muestra la lista de clientes registrados |
| **6** | Muestra estadísticas del restaurante (ingresos, total de clientes, etc.) |
| **7** | Muestra el inventario actual de todos los productos |
| **8** | Cierra el programa |

---

## 1️⃣ Gestionar Productos

### Opción 1.1: Agregar un nuevo producto

Al seleccionar esta opción, se te pedirá:

```
AGREGAR NUEVO PRODUCTO
----------------------------------------------------------------------
Ingrese el ID del producto: 1
Ingrese el nombre del producto: Hamburguesa Clásica
Ingrese la descripción del producto: Hamburguesa jugosa con queso
Ingrese el precio del producto: $8.99
Ingrese la cantidad disponible: 50
```

**Campos a completar:**
- **ID**: Número único del producto (ej: 1, 2, 3)
- **Nombre**: Nombre del producto (ej: Hamburguesa Clásica)
- **Descripción**: Descripción breve (ej: Hamburguesa jugosa con queso)
- **Precio**: Precio en USD (ej: 8.99)
- **Cantidad**: Número de unidades disponibles (ej: 50)

**Ejemplo de entrada:**
```
1
Pizza Margherita
Pizza tradicional con tomate y queso
12.50
30
```

**Validaciones:**
- ❌ El ID debe ser único (no puede haber dos productos con el mismo ID)
- ❌ El nombre y descripción no pueden estar vacíos
- ❌ El precio debe ser mayor a 0
- ❌ La cantidad no puede ser negativa

### Opción 1.2: Ver todos los productos

Muestra una lista formateada de todos los productos registrados:

```
======================================================================
CATÁLOGO DE PRODUCTOS - Mi Restaurante
======================================================================
• Producto: Pizza Margherita | Descripción: Pizza tradicional... | Precio: $12.50 | Disponibles: 30
• Producto: Hamburguesa Clásica | Descripción: Hamburguesa jugosa... | Precio: $8.99 | Disponibles: 50
======================================================================
```

### Opción 1.3: Volver al menú principal

Regresa al menú principal.

---

## 2️⃣ Gestionar Clientes

### Opción 2.1: Agregar un nuevo cliente

Al seleccionar esta opción, se te pedirá:

```
AGREGAR NUEVO CLIENTE
----------------------------------------------------------------------
Ingrese el ID del cliente: 101
Ingrese el nombre del cliente: Juan Pérez
Ingrese el email del cliente: juan@email.com
Ingrese el teléfono del cliente: +593-999-1234
```

**Campos a completar:**
- **ID**: Número único del cliente (ej: 101, 102)
- **Nombre**: Nombre completo (ej: Juan Pérez)
- **Email**: Correo electrónico (ej: juan@email.com)
- **Teléfono**: Número de teléfono (ej: +593-999-1234)

**Ejemplo de entrada:**
```
102
María García
maria@email.com
+593-998-5678
```

**Validaciones:**
- ❌ El ID debe ser único
- ❌ Todos los campos son obligatorios (no pueden estar vacíos)

### Opción 2.2: Ver todos los clientes

Muestra una lista formateada de todos los clientes registrados:

```
======================================================================
CLIENTES REGISTRADOS - Mi Restaurante
======================================================================
• Cliente: Juan Pérez | Email: juan@email.com | Teléfono: +593-999-1234 | Monto gastado: $0.00
• Cliente: María García | Email: maria@email.com | Teléfono: +593-998-5678 | Monto gastado: $0.00
======================================================================
```

### Opción 2.3: Volver al menú principal

Regresa al menú principal.

---

## 3️⃣ Realizar Pedido

Esta opción permite que un cliente realice un pedido.

```
REALIZAR PEDIDO
----------------------------------------------------------------------
Ingrese el ID del cliente: 101
```

Luego, el sistema muestra los productos disponibles:

```
✓ Cliente: Juan Pérez

Productos disponibles:
  ID: 1 | Hamburguesa Clásica - $8.99 (Disponibles: 50)
  ID: 2 | Pizza Margherita - $12.50 (Disponibles: 30)
  ID: 3 | Refresco Cola - $2.50 (Disponibles: 100)
```

Después, se te pedirá que selecciones productos:

```
Ingrese el ID del producto (o 'fin' para terminar): 1
¿Cuántas unidades desea de este producto? 2
✓ Producto agregado al pedido.

Ingrese el ID del producto (o 'fin' para terminar): 3
¿Cuántas unidades desea de este producto? 1
✓ Producto agregado al pedido.

Ingrese el ID del producto (o 'fin' para terminar): fin
✓ Pedido realizado exitosamente.
```

**Proceso:**
1. Ingresa el ID del cliente que realiza el pedido
2. El sistema muestra los productos disponibles
3. Ingresa el ID del producto que deseas agregar
4. Ingresa la cantidad de unidades
5. Repite los pasos 3-4 para agregar más productos
6. Escribe "fin" para terminar y procesar el pedido

**Validaciones:**
- ❌ El cliente debe existir
- ❌ El producto debe existir
- ❌ Debe haber suficiente cantidad disponible
- ❌ La cantidad debe ser > 0

---

## 4️⃣ Ver Catálogo de Productos

Muestra el catálogo completo con la siguiente información:

```
======================================================================
CATÁLOGO DE PRODUCTOS - Mi Restaurante
======================================================================
• Producto: Hamburguesa Clásica | Descripción: Hamburguesa jugosa con queso | Precio: $8.99 | Disponibles: 50
• Producto: Pizza Margherita | Descripción: Pizza tradicional con tomate | Precio: $12.50 | Disponibles: 30
======================================================================
```

---

## 5️⃣ Ver Clientes Registrados

Muestra la lista de todos los clientes con la siguiente información:

```
======================================================================
CLIENTES REGISTRADOS - Mi Restaurante
======================================================================
• Cliente: Juan Pérez | Email: juan@email.com | Teléfono: +593-999-1234 | Monto gastado: $20.50
• Cliente: María García | Email: maria@email.com | Teléfono: +593-998-5678 | Monto gastado: $15.99
======================================================================
```

---

## 6️⃣ Ver Estadísticas

Muestra un resumen estadístico del restaurante:

```
======================================================================
ESTADÍSTICAS - Mi Restaurante
======================================================================
Total de Productos: 3
Total de Clientes: 2
Ingresos Totales: $36.49
======================================================================
```

---

## 7️⃣ Ver Inventario

Muestra el estado detallado del inventario:

```
----------------------------------------------------------------------
INVENTARIO ACTUAL
----------------------------------------------------------------------

✓ Hamburguesa Clásica
  • Descripción: Hamburguesa jugosa con queso y lechuga
  • Precio: $8.99
  • Disponibles: 48 unidades

✓ Pizza Margherita
  • Descripción: Pizza tradicional con tomate y queso
  • Precio: $12.50
  • Disponibles: 30 unidades

✓ Refresco Cola
  • Descripción: Bebida refrescante de cola 350ml
  • Precio: $2.50
  • Disponibles: 99 unidades
```

---

## 8️⃣ Salir

Cierra el programa mostrando un mensaje de despedida:

```
======================================================================
¡Gracias por usar el Sistema de Gestión de Restaurante!
======================================================================
```

---

## 📝 Ejemplo Completo de Uso

### Paso 1: Iniciar el programa
```bash
python main_interactivo.py
```

### Paso 2: Crear el restaurante
```
¿Cuál es el nombre de su restaurante? La Mesa Feliz
✓ Restaurante 'La Mesa Feliz' creado exitosamente.
```

### Paso 3: Agregar productos (Opción 1.1)
```
1 → Gestionar Productos
1 → Agregar nuevo producto

ID: 1
Nombre: Hamburguesa
Descripción: Hamburguesa con queso
Precio: 8.99
Cantidad: 50
✓ Producto agregado exitosamente.
```

### Paso 4: Agregar cliente (Opción 2.1)
```
2 → Gestionar Clientes
1 → Agregar nuevo cliente

ID: 101
Nombre: Juan Pérez
Email: juan@email.com
Teléfono: +593-999-1234
✓ Cliente registrado exitosamente.
```

### Paso 5: Realizar pedido (Opción 3)
```
3 → Realizar Pedido

ID Cliente: 101
ID Producto: 1
Cantidad: 2
Fin: fin

✓ Pedido realizado exitosamente.
```

### Paso 6: Ver información (Opciones 4, 5, 6)
```
4 → Ver catálogo
5 → Ver clientes
6 → Ver estadísticas
```

### Paso 7: Salir (Opción 8)
```
8 → Salir
```

---

## 🛡️ Manejo de Errores

El programa incluye validaciones para los siguientes errores:

| Error | Mensaje | Solución |
|-------|---------|----------|
| ID duplicado | "El producto/cliente con ID X ya existe" | Usa un ID diferente |
| Datos vacíos | "Los campos son obligatorios" | Completa todos los campos |
| Valor inválido | "Ingrese valores válidos" | Ingresa números donde se requiera |
| Cliente no existe | "Cliente no encontrado" | Verifica el ID del cliente |
| Producto no existe | "Producto no encontrado" | Verifica el ID del producto |
| Inventario agotado | "No hay suficiente cantidad" | Solicita menos unidades |

---

## 💡 Consejos

1. **IDs únicos**: Siempre usa IDs diferentes para productos y clientes
2. **Información precisa**: Ingresa información correcta para facilitar búsquedas
3. **Seguimiento de inventario**: Consulta el inventario frecuentemente
4. **Revisión de estadísticas**: Las estadísticas se actualizan automáticamente con cada pedido

---

## 🎯 Casos de Uso

### Caso 1: Abrir un restaurante nuevo
1. Ejecutar el programa
2. Ingresar nombre del restaurante
3. Agregar productos principales
4. Registrar clientes iniciales
5. Consultar catálogo

### Caso 2: Procesar un pedido
1. Opción 3: Realizar Pedido
2. Ingresar ID del cliente
3. Seleccionar productos y cantidades
4. Finalizar con "fin"

### Caso 3: Revisar estado del negocio
1. Opción 6: Ver Estadísticas
2. Opción 7: Ver Inventario
3. Opción 5: Ver Clientes

---

**¡Ahora ya estás listo para usar el sistema interactivo!** 🎉

