"""
Script de pruebas ampliado para validar búsqueda y eliminación.
Verifica la funcionalidad del menú expandido con 12 opciones.
"""

import os
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
from servicios.gestor_datos import GestorDatos


def prueba_busqueda_productos() -> None:
    """Prueba la búsqueda de productos."""
    print("\n" + "=" * 50)
    print("PRUEBA: Búsqueda de Productos")
    print("=" * 50)

    restaurante = Restaurante()

    # Registrar productos
    p1 = Producto("P001", "Pizza Margarita", "Platos Principales", 12.50)
    p2 = Producto("P002", "Ensalada César", "Ensaladas", 8.50)

    restaurante.registrar_producto(p1)
    restaurante.registrar_producto(p2)
    print(f"✓ {restaurante.obtener_cantidad_productos()} productos registrados")

    # Buscar producto existente
    exito, producto, msg = restaurante.buscar_producto("P001")
    print(f"✓ Búsqueda exitosa: {msg}")
    assert exito, "Error: No se encontró el producto"

    # Buscar producto inexistente
    exito, producto, msg = restaurante.buscar_producto("P999")
    print(f"✓ Búsqueda fallida (esperada): {msg}")
    assert not exito, "Error: Se encontró un producto inexistente"


def prueba_busqueda_clientes() -> None:
    """Prueba la búsqueda de clientes."""
    print("\n" + "=" * 50)
    print("PRUEBA: Búsqueda de Clientes")
    print("=" * 50)

    restaurante = Restaurante()

    # Registrar clientes
    c1 = Cliente("123456", "Juan Pérez", "juan@example.com")
    c2 = Cliente("789012", "María García", "maria@example.com")

    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)
    print(f"✓ {restaurante.obtener_cantidad_clientes()} clientes registrados")

    # Buscar cliente existente
    exito, cliente, msg = restaurante.buscar_cliente("123456")
    print(f"✓ Búsqueda exitosa: {msg}")
    assert exito, "Error: No se encontró el cliente"

    # Buscar cliente inexistente
    exito, cliente, msg = restaurante.buscar_cliente("999999")
    print(f"✓ Búsqueda fallida (esperada): {msg}")
    assert not exito, "Error: Se encontró un cliente inexistente"


def prueba_eliminacion_productos() -> None:
    """Prueba la eliminación de productos."""
    print("\n" + "=" * 50)
    print("PRUEBA: Eliminación de Productos")
    print("=" * 50)

    restaurante = Restaurante()

    # Registrar productos
    p1 = Producto("P001", "Pizza", "Platos", 12.50)
    p2 = Producto("P002", "Pasta", "Platos", 10.00)

    restaurante.registrar_producto(p1)
    restaurante.registrar_producto(p2)
    print(f"✓ {restaurante.obtener_cantidad_productos()} productos registrados")

    # Eliminar producto existente
    exito, msg = restaurante.eliminar_producto("P001")
    print(f"✓ Eliminación exitosa: {msg}")
    assert exito, "Error: No se eliminó el producto"
    assert restaurante.obtener_cantidad_productos() == 1, "Error: Cantidad incorrecta"

    # Eliminar producto inexistente
    exito, msg = restaurante.eliminar_producto("P999")
    print(f"✓ Eliminación fallida (esperada): {msg}")
    assert not exito, "Error: Se eliminó un producto inexistente"


def prueba_eliminacion_clientes() -> None:
    """Prueba la eliminación de clientes."""
    print("\n" + "=" * 50)
    print("PRUEBA: Eliminación de Clientes")
    print("=" * 50)

    restaurante = Restaurante()

    # Registrar clientes
    c1 = Cliente("123456", "Juan", "juan@example.com")
    c2 = Cliente("789012", "María", "maria@example.com")

    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)
    print(f"✓ {restaurante.obtener_cantidad_clientes()} clientes registrados")

    # Eliminar cliente existente
    exito, msg = restaurante.eliminar_cliente("123456")
    print(f"✓ Eliminación exitosa: {msg}")
    assert exito, "Error: No se eliminó el cliente"
    assert restaurante.obtener_cantidad_clientes() == 1, "Error: Cantidad incorrecta"

    # Eliminar cliente inexistente
    exito, msg = restaurante.eliminar_cliente("999999")
    print(f"✓ Eliminación fallida (esperada): {msg}")
    assert not exito, "Error: Se eliminó un cliente inexistente"


def ejecutar_todas_pruebas() -> None:
    """Ejecuta todas las pruebas ampliadas."""
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " " * 8 + "PRUEBAS DEL MENÚ EXPANDIDO (12 OPCIONES)" + " " * 4 + "║")
    print("╚" + "=" * 48 + "╝")

    try:
        prueba_busqueda_productos()
        prueba_busqueda_clientes()
        prueba_eliminacion_productos()
        prueba_eliminacion_clientes()

        print("\n" + "=" * 50)
        print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 50 + "\n")

    except Exception as e:
        print(f"\n✗ ERROR DURANTE LAS PRUEBAS: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    ejecutar_todas_pruebas()

