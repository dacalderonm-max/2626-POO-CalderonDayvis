"""
GUÍA DE USO - Sistema de Restaurante
Semana 8 - Aplicación de Principios SOLID

Este archivo demuestra cómo usar el sistema de forma interactiva.
Sigue el flujo paso a paso para entender el funcionamiento del programa.
"""

# ============================================================================
# PASO 1: INICIAR EL PROGRAMA
# ============================================================================

# Desde la terminal, navega a la carpeta restaurante_app:
# cd restaurante_app
#
# Luego ejecuta:
# python main.py
#
# Verás el menú principal:
# ========================================
#         SISTEMA DE RESTAURANTE
# ========================================
# 1. Registrar producto
# 2. Registrar bebida
# 3. Registrar cliente
# ----------------------------------------
# 4. Listar productos
# 5. Listar clientes
# ----------------------------------------
# 6. Salir
# ========================================
# Ingrese su opción: _

# ============================================================================
# PASO 2: REGISTRAR UN PRODUCTO (Opción 1)
# ============================================================================

# Ingresa: 1
# El sistema solicita:
#
# --- Registrar Producto ---
# Código del producto: P001
# Nombre del producto: Hamburguesa
# Categoría del producto: Comida Rápida
# Precio del producto ($): 8.50
#
# Resultado esperado:
# Producto registrado exitosamente: Hamburguesa

# ============================================================================
# PASO 3: REGISTRAR UNA BEBIDA (Opción 2)
# ============================================================================

# Ingresa: 2
# El sistema solicita:
#
# --- Registrar Bebida ---
# Código de la bebida: B001
# Nombre de la bebida: Refresco de Cola
# Categoría de la bebida: Bebidas
# Precio de la bebida ($): 2.00
# Tamaño (pequeño/mediano/grande): mediano
# Tipo de envase (vaso/botella/lata): vaso
#
# Resultado esperado:
# Bebida registrada exitosamente: Refresco de Cola

# NOTA IMPORTANTE (Principio LSP):
# Internamente, Bebida se almacena en la MISMA lista que Producto.
# No se requieren listas separadas.

# ============================================================================
# PASO 4: REGISTRAR OTRO PRODUCTO (Opción 1)
# ============================================================================

# Ingresa: 1
#
# --- Registrar Producto ---
# Código del producto: P002
# Nombre del producto: Pizza Margherita
# Categoría del producto: Comida Italiana
# Precio del producto ($): 12.00
#
# Resultado esperado:
# Producto registrado exitosamente: Pizza Margherita

# ============================================================================
# PASO 5: REGISTRAR OTRA BEBIDA (Opción 2)
# ============================================================================

# Ingresa: 2
#
# --- Registrar Bebida ---
# Código de la bebida: B002
# Nombre de la bebida: Agua Mineral
# Categoría de la bebida: Bebidas
# Precio de la bebida ($): 1.50
# Tamaño (pequeño/mediano/grande): grande
# Tipo de envase (vaso/botella/lata): botella
#
# Resultado esperado:
# Bebida registrada exitosamente: Agua Mineral

# ============================================================================
# PASO 6: REGISTRAR UN CLIENTE (Opción 3)
# ============================================================================

# Ingresa: 3
#
# --- Registrar Cliente ---
# Identificación del cliente: 1234567890
# Nombre del cliente: Juan Pérez
# Correo del cliente: juan.perez@email.com
#
# Resultado esperado:
# Cliente registrado exitosamente: Juan Pérez

# ============================================================================
# PASO 7: REGISTRAR OTRO CLIENTE (Opción 3)
# ============================================================================

# Ingresa: 3
#
# --- Registrar Cliente ---
# Identificación del cliente: 9876543210
# Nombre del cliente: María García
# Correo del cliente: maria.garcia@email.com
#
# Resultado esperado:
# Cliente registrado exitosamente: María García

# ============================================================================
# PASO 8: LISTAR PRODUCTOS (Opción 4)
# ============================================================================

# Ingresa: 4
#
# --- Productos Registrados ---
# Código: P001 | Nombre: Hamburguesa | Categoría: Comida Rápida | Precio: $8.50
# Código: B001 | Nombre: Refresco de Cola | Categoría: Bebidas | Precio: $2.00 | Tamaño: mediano | Envase: vaso
# Código: P002 | Nombre: Pizza Margherita | Categoría: Comida Italiana | Precio: $12.00
# Código: B002 | Nombre: Agua Mineral | Categoría: Bebidas | Precio: $1.50 | Tamaño: grande | Envase: botella
#
# Total de productos: 4
#
# NOTA IMPORTANTE (Polimorfismo):
# Observa que:
# - P001 y P002 (Productos) muestran formato básico
# - B001 y B002 (Bebidas) muestran formato extendido con Tamaño y Envase
# - NO hay condicionales en el código para diferenciar tipos
# - Cada objeto ejecuta su propia versión de mostrar_informacion()

# ============================================================================
# PASO 9: LISTAR CLIENTES (Opción 5)
# ============================================================================

# Ingresa: 5
#
# --- Clientes Registrados ---
# ID: 1234567890 | Nombre: Juan Pérez | Correo: juan.perez@email.com
# ID: 9876543210 | Nombre: María García | Correo: maria.garcia@email.com
#
# Total de clientes: 2

# ============================================================================
# PASO 10: INTENTAR DUPLICAR UN CÓDIGO (Validación)
# ============================================================================

# Ingresa: 1
#
# --- Registrar Producto ---
# Código del producto: P001  # Este código ya existe
# Nombre del producto: Otro Producto
# Categoría del producto: Otra Categoría
# Precio del producto ($): 5.00
#
# Resultado esperado (VALIDACIÓN):
# Error: El código 'P001' ya existe.
#
# El sistema PREVIENE códigos duplicados

# ============================================================================
# PASO 11: INTENTAR DUPLICAR UNA IDENTIFICACIÓN (Validación)
# ============================================================================

# Ingresa: 3
#
# --- Registrar Cliente ---
# Identificación del cliente: 1234567890  # Este ID ya existe
# Nombre del cliente: Otro Cliente
# Correo del cliente: otro@email.com
#
# Resultado esperado (VALIDACIÓN):
# Error: La identificación '1234567890' ya existe.
#
# El sistema PREVIENE identificaciones duplicadas

# ============================================================================
# PASO 12: VALIDACIÓN DE ENTRADA - PRECIO NEGATIVO
# ============================================================================

# Ingresa: 1
#
# --- Registrar Producto ---
# Código del producto: P003
# Nombre del producto: Producto Inválido
# Categoría del producto: Test
# Precio del producto ($): -5.00  # Precio negativo
#
# Resultado esperado (VALIDACIÓN):
# Error: El precio no puede ser negativo.
#
# El sistema VALIDA que los precios sean positivos

# ============================================================================
# PASO 13: VALIDACIÓN DE ENTRADA - CAMPO VACÍO
# ============================================================================

# Ingresa: 1
#
# --- Registrar Producto ---
# Código del producto: P003
# Nombre del producto:  # Deja vacío
#
# Resultado esperado (VALIDACIÓN):
# Error: El nombre no puede estar vacío.
#
# El sistema VALIDA que no haya campos vacíos

# ============================================================================
# PASO 14: VALIDACIÓN DE ENTRADA - TIPO DE DATO INVÁLIDO
# ============================================================================

# Ingresa: 2
#
# --- Registrar Bebida ---
# Código de la bebida: B003
# Nombre de la bebida: Jugo Natural
# Categoría de la bebida: Bebidas
# Precio de la bebida ($): abc  # Ingresa texto en lugar de número
#
# Resultado esperado (VALIDACIÓN):
# Error: El precio debe ser un número válido.
#
# El sistema VALIDA tipos de dato

# ============================================================================
# PASO 15: SALIR DEL PROGRAMA (Opción 6)
# ============================================================================

# Ingresa: 6
#
# Resultado esperado:
# ¡Gracias por usar el sistema de restaurante!
#
# El programa se cierra

# ============================================================================
# CONCEPTOS CLAVE DEMOSTRADOS
# ============================================================================

"""
1. RESPONSABILIDAD ÚNICA (SRP):
   - Producto: Representa datos de producto
   - Bebida: Extiende Producto con datos específicos
   - Cliente: Representa datos de cliente
   - Restaurante: Administra colecciones
   - main.py: Interacción con usuario

2. ABIERTO/CERRADO (OCP):
   - Bebida se agregó sin modificar Producto
   - Se podría agregar Platillo, Postre, etc.
   - Las nuevas clases heredarían de Producto

3. SUSTITUCIÓN DE LISKOV (LSP):
   - Bebida se usa donde se espera Producto
   - No hay condicionales if isinstance()
   - Polimorfismo en acción en listar_productos()

4. VALIDACIONES:
   - Códigos únicos
   - Identificaciones únicas
   - Precios válidos (no negativos)
   - Campos no vacíos

5. POLIMORFISMO:
   - Cada objeto ejecuta su propia mostrar_informacion()
   - Productos y Bebidas en la misma lista
   - Sin necesidad de condicionales

6. ANOTACIONES DE TIPOS:
   - Todos los métodos incluyen anotaciones
   - Mejor legibilidad y mantenibilidad
"""

# ============================================================================
# EJEMPLOS DE ENTRADA VÁLIDA
# ============================================================================

# PRODUCTO VÁLIDO:
# Código: P001
# Nombre: Hamburguesa
# Categoría: Comida Rápida
# Precio: 8.50

# BEBIDA VÁLIDA:
# Código: B001
# Nombre: Refresco de Cola
# Categoría: Bebidas
# Precio: 2.00
# Tamaño: mediano
# Tipo de envase: vaso

# CLIENTE VÁLIDO:
# Identificación: 1234567890
# Nombre: Juan Pérez
# Correo: juan@email.com

# ============================================================================
# EJEMPLOS DE ENTRADA INVÁLIDA (Serán rechazadas)
# ============================================================================

# PRODUCTO INVÁLIDO - Código duplicado:
# Código: P001  # Ya existe
# Resultado: Error rechazado

# BEBIDA INVÁLIDA - Precio negativo:
# Precio: -5.00
# Resultado: Error rechazado

# CLIENTE INVÁLIDO - ID duplicada:
# Identificación: 1234567890  # Ya existe
# Resultado: Error rechazado

# PRODUCTO INVÁLIDO - Campo vacío:
# Nombre:  # Vacío
# Resultado: Error rechazado

# BEBIDA INVÁLIDA - Tipo de dato:
# Precio: abc  # No es número
# Resultado: Error rechazado

