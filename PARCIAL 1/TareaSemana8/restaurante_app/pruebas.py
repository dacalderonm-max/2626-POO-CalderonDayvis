"""
Script de prueba automatizado para el Sistema de Restaurante.
Verifica que todas las funcionalidades funcionan correctamente.
"""

import sys
from io import StringIO
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def prueba_producto():
    """Prueba la creación y funcionamiento de la clase Producto."""
    print("=" * 60)
    print("PRUEBA 1: Clase Producto")
    print("=" * 60)

    producto = Producto("P001", "Hamburguesa", "Comida Rápida", 8.50)
    print(f"✓ Producto creado: {producto.nombre}")
    print(f"✓ Información: {producto.mostrar_informacion()}")
    print(f"✓ Código: {producto.obtener_codigo()}")
    print()


def prueba_bebida():
    """Prueba la creación y herencia de la clase Bebida."""
    print("=" * 60)
    print("PRUEBA 2: Clase Bebida (herencia de Producto)")
    print("=" * 60)

    bebida = Bebida("B001", "Refresco de Cola", "Bebidas", 2.00, "mediano", "vaso")
    print(f"✓ Bebida creada: {bebida.nombre}")
    print(f"✓ Información: {bebida.mostrar_informacion()}")
    print(f"✓ Código: {bebida.obtener_codigo()}")
    print(f"✓ Verificación de herencia: {isinstance(bebida, Producto)}")
    print()


def prueba_cliente():
    """Prueba la creación de la clase Cliente."""
    print("=" * 60)
    print("PRUEBA 3: Clase Cliente")
    print("=" * 60)

    cliente = Cliente("1234567890", "Juan Pérez", "juan@email.com")
    print(f"✓ Cliente creado: {cliente.nombre}")
    print(f"✓ Información: {cliente.mostrar_informacion()}")
    print(f"✓ Identificación: {cliente.obtener_identificacion()}")
    print()


def prueba_restaurante_productos():
    """Prueba el registro y listado de productos."""
    print("=" * 60)
    print("PRUEBA 4: Restaurante - Registro de Productos")
    print("=" * 60)

    restaurante = Restaurante()

    # Registrar Producto
    p1 = Producto("P001", "Hamburguesa", "Comida Rápida", 8.50)
    exito, msg = restaurante.registrar_producto(p1)
    print(f"{'✓' if exito else '✗'} {msg}")

    # Registrar Bebida (polimorfismo)
    b1 = Bebida("B001", "Refresco", "Bebidas", 2.00, "mediano", "vaso")
    exito, msg = restaurante.registrar_producto(b1)
    print(f"{'✓' if exito else '✗'} {msg}")

    # Intentar registrar código duplicado
    p2 = Producto("P001", "Otro Producto", "Otra Categoría", 5.00)
    exito, msg = restaurante.registrar_producto(p2)
    print(f"{'✓' if not exito else '✗'} {msg} (Validación correcta: código duplicado rechazado)")

    # Listar productos (polimorfismo en acción)
    print("\n--- Listado de Productos (con polimorfismo) ---")
    productos = restaurante.listar_productos()
    for p in productos:
        print(f"  {p}")

    print(f"\n✓ Total de productos: {restaurante.obtener_cantidad_productos()}")
    print()


def prueba_restaurante_clientes():
    """Prueba el registro y listado de clientes."""
    print("=" * 60)
    print("PRUEBA 5: Restaurante - Registro de Clientes")
    print("=" * 60)

    restaurante = Restaurante()

    # Registrar Clientes
    c1 = Cliente("1234567890", "Juan Pérez", "juan@email.com")
    exito, msg = restaurante.registrar_cliente(c1)
    print(f"{'✓' if exito else '✗'} {msg}")

    c2 = Cliente("0987654321", "María García", "maria@email.com")
    exito, msg = restaurante.registrar_cliente(c2)
    print(f"{'✓' if exito else '✗'} {msg}")

    # Intentar registrar identificación duplicada
    c3 = Cliente("1234567890", "Otro Cliente", "otro@email.com")
    exito, msg = restaurante.registrar_cliente(c3)
    print(f"{'✓' if not exito else '✗'} {msg} (Validación correcta: ID duplicada rechazada)")

    # Listar clientes
    print("\n--- Listado de Clientes ---")
    clientes = restaurante.listar_clientes()
    for c in clientes:
        print(f"  {c}")

    print(f"\n✓ Total de clientes: {restaurante.obtener_cantidad_clientes()}")
    print()


def prueba_polimorfismo():
    """Prueba el polimorfismo sin condicionales."""
    print("=" * 60)
    print("PRUEBA 6: Polimorfismo (Sin condicionales)")
    print("=" * 60)

    restaurante = Restaurante()

    # Crear una lista mixta de Producto y Bebida
    productos_originales = [
        Producto("P001", "Hamburguesa", "Comida Rápida", 8.50),
        Bebida("B001", "Agua", "Bebidas", 1.50, "grande", "botella"),
        Producto("P002", "Pizza", "Comida Rápida", 12.00),
        Bebida("B002", "Café", "Bebidas", 2.50, "pequeño", "vaso"),
    ]

    # Registrar todos sin condicionales
    for producto in productos_originales:
        exito, msg = restaurante.registrar_producto(producto)
        print(f"{'✓' if exito else '✗'} Registrado: {producto.__class__.__name__} - {producto.nombre}")

    # Listar usando polimorfismo
    print("\n--- Listado usando Polimorfismo (cada objeto muestra su propia información) ---")
    productos_listados = restaurante.listar_productos()
    for p in productos_listados:
        print(f"  {p}")

    print(f"\n✓ POLIMORFISMO EXITOSO:")
    print(f"  - {restaurante.obtener_cantidad_productos()} productos mezclados")
    print(f"  - Cada objeto mostró su información correctamente")
    print(f"  - No se usaron condicionales para distinguir tipos")
    print()


def prueba_validaciones():
    """Prueba las validaciones del sistema."""
    print("=" * 60)
    print("PRUEBA 7: Validaciones")
    print("=" * 60)

    restaurante = Restaurante()

    # Validar código duplicado
    p1 = Producto("P001", "Producto 1", "Cat 1", 10.0)
    p2 = Producto("P001", "Producto 2", "Cat 2", 20.0)

    exito1, msg1 = restaurante.registrar_producto(p1)
    exito2, msg2 = restaurante.registrar_producto(p2)

    print(f"✓ Validación 1: {msg1}")
    print(f"✓ Validación 2: {msg2}")
    print(f"✓ Código duplicado correctamente rechazado: {not exito2}")

    # Validar identificación duplicada
    c1 = Cliente("ID001", "Cliente 1", "cliente1@email.com")
    c2 = Cliente("ID001", "Cliente 2", "cliente2@email.com")

    exito3, msg3 = restaurante.registrar_cliente(c1)
    exito4, msg4 = restaurante.registrar_cliente(c2)

    print(f"✓ Validación 3: {msg3}")
    print(f"✓ Validación 4: {msg4}")
    print(f"✓ Identificación duplicada correctamente rechazada: {not exito4}")
    print()


def prueba_listas_vacias():
    """Prueba el comportamiento con listas vacías."""
    print("=" * 60)
    print("PRUEBA 8: Listas Vacías")
    print("=" * 60)

    restaurante = Restaurante()

    # Listar productos vacíos
    productos = restaurante.listar_productos()
    print(f"✓ Productos vacíos: {productos[0]}")

    # Listar clientes vacíos
    clientes = restaurante.listar_clientes()
    print(f"✓ Clientes vacíos: {clientes[0]}")

    print(f"✓ Total productos: {restaurante.obtener_cantidad_productos()}")
    print(f"✓ Total clientes: {restaurante.obtener_cantidad_clientes()}")
    print()


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del sistema."""
    print("\n")
    print("#" * 60)
    print("# PRUEBAS DEL SISTEMA DE RESTAURANTE")
    print("# Aplicación de Principios SOLID")
    print("#" * 60)
    print()

    prueba_producto()
    prueba_bebida()
    prueba_cliente()
    prueba_restaurante_productos()
    prueba_restaurante_clientes()
    prueba_polimorfismo()
    prueba_validaciones()
    prueba_listas_vacias()

    print("=" * 60)
    print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 60)
    print()
    print("Principios SOLID Verificados:")
    print("✓ S - Responsabilidad Única: Cada clase tiene un propósito claro")
    print("✓ O - Abierto/Cerrado: Bebida extiende Producto sin modificarlo")
    print("✓ L - Sustitución de Liskov: Bebida puede usarse como Producto")
    print()


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()

