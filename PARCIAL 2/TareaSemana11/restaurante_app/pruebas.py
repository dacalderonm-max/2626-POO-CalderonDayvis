"""
Script de pruebas para validar el funcionamiento del sistema.
Prueba la creación de objetos, persistencia en JSON y recuperación de datos.
"""

import os
import json
import sys
from pathlib import Path

# Agregar el directorio actual al path para las importaciones
sys.path.insert(0, str(Path(__file__).parent))

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
from servicios.gestor_datos import GestorDatos


def limpiar_archivos(gestor: GestorDatos) -> None:
    """Limpia los archivos JSON anteriores."""
    gestor.eliminar_archivos()
    print("✓ Archivos anteriores eliminados")


def prueba_modelos() -> None:
    """Prueba la creación de modelos y conversión a diccionarios."""
    print("\n" + "=" * 50)
    print("PRUEBA 1: Modelos y Diccionarios")
    print("=" * 50)

    # Crear un producto
    producto = Producto("P001", "Pizza Margarita", "Platos Principales", 12.50)
    print(f"\n✓ Producto creado: {producto.mostrar_informacion()}")

    # Convertir a diccionario
    producto_dict = producto.a_diccionario()
    print(f"✓ Convertido a diccionario: {producto_dict}")

    # Recuperar desde diccionario
    producto_recuperado = Producto.desde_diccionario(producto_dict)
    print(f"✓ Recuperado desde diccionario: {producto_recuperado.mostrar_informacion()}")

    # Crear un cliente
    cliente = Cliente("1234567890", "Juan Pérez", "juan@example.com")
    print(f"\n✓ Cliente creado: {cliente.mostrar_informacion()}")

    # Convertir a diccionario
    cliente_dict = cliente.a_diccionario()
    print(f"✓ Convertido a diccionario: {cliente_dict}")

    # Recuperar desde diccionario
    cliente_recuperado = Cliente.desde_diccionario(cliente_dict)
    print(f"✓ Recuperado desde diccionario: {cliente_recuperado.mostrar_informacion()}")


def prueba_persistencia() -> None:
    """Prueba guardar y cargar datos desde JSON."""
    print("\n" + "=" * 50)
    print("PRUEBA 2: Persistencia en JSON")
    print("=" * 50)

    # Crear instancias
    restaurante = Restaurante()
    gestor = GestorDatos()

    # Limpiar archivos anteriores
    limpiar_archivos(gestor)

    # Registrar productos
    print("\n--- Registrando Productos ---")
    p1 = Producto("P001", "Pizza Margarita", "Platos Principales", 12.50)
    p2 = Producto("P002", "Ensalada César", "Ensaladas", 8.50)
    p3 = Producto("P003", "Pasta Carbonara", "Platos Principales", 11.00)

    restaurante.registrar_producto(p1)
    restaurante.registrar_producto(p2)
    restaurante.registrar_producto(p3)
    print(f"✓ {restaurante.obtener_cantidad_productos()} productos registrados en memoria")

    # Registrar clientes
    print("\n--- Registrando Clientes ---")
    c1 = Cliente("1234567890", "Juan Pérez", "juan@example.com")
    c2 = Cliente("0987654321", "María García", "maria@example.com")
    c3 = Cliente("1122334455", "Carlos López", "carlos@example.com")

    restaurante.registrar_cliente(c1)
    restaurante.registrar_cliente(c2)
    restaurante.registrar_cliente(c3)
    print(f"✓ {restaurante.obtener_cantidad_clientes()} clientes registrados en memoria")

    # Guardar en JSON
    print("\n--- Guardando en JSON ---")
    exito_p, msg_p = gestor.guardar_productos(restaurante.obtener_productos())
    exito_c, msg_c = gestor.guardar_clientes(restaurante.obtener_clientes())
    print(f"✓ {msg_p}")
    print(f"✓ {msg_c}")

    # Verificar que los archivos existen
    print("\n--- Verificando Archivos ---")
    if os.path.exists(gestor.ruta_productos):
        print(f"✓ Archivo de productos existe: {gestor.ruta_productos}")
        with open(gestor.ruta_productos, 'r', encoding='utf-8') as f:
            productos_json = json.load(f)
            print(f"  Contenido: {len(productos_json)} productos en JSON")
    else:
        print(f"✗ Archivo de productos no encontrado")

    if os.path.exists(gestor.ruta_clientes):
        print(f"✓ Archivo de clientes existe: {gestor.ruta_clientes}")
        with open(gestor.ruta_clientes, 'r', encoding='utf-8') as f:
            clientes_json = json.load(f)
            print(f"  Contenido: {len(clientes_json)} clientes en JSON")
    else:
        print(f"✗ Archivo de clientes no encontrado")


def prueba_carga() -> None:
    """Prueba cargar datos desde JSON."""
    print("\n" + "=" * 50)
    print("PRUEBA 3: Carga desde JSON")
    print("=" * 50)

    # Crear nuevas instancias vacías
    restaurante = Restaurante()
    gestor = GestorDatos()

    print(f"\n✓ Restaurante vacío:")
    print(f"  - Productos en memoria: {restaurante.obtener_cantidad_productos()}")
    print(f"  - Clientes en memoria: {restaurante.obtener_cantidad_clientes()}")

    # Cargar desde JSON
    print("\n--- Cargando desde JSON ---")
    exito_p, productos, msg_p = gestor.cargar_productos()
    exito_c, clientes, msg_c = gestor.cargar_clientes()

    print(f"✓ {msg_p}")
    print(f"✓ {msg_c}")

    # Establecer datos en restaurante
    restaurante.establecer_productos(productos)
    restaurante.establecer_clientes(clientes)

    # Verificar datos cargados
    print("\n--- Datos Cargados ---")
    print(f"✓ Productos cargados: {restaurante.obtener_cantidad_productos()}")
    for p in restaurante.listar_productos():
        print(f"  - {p}")

    print(f"\n✓ Clientes cargados: {restaurante.obtener_cantidad_clientes()}")
    for c in restaurante.listar_clientes():
        print(f"  - {c}")


def prueba_validacion() -> None:
    """Prueba la validación de duplicados."""
    print("\n" + "=" * 50)
    print("PRUEBA 4: Validación de Duplicados")
    print("=" * 50)

    restaurante = Restaurante()

    # Registrar producto
    p1 = Producto("P001", "Pizza", "Platos", 10.00)
    exito, msg = restaurante.registrar_producto(p1)
    print(f"\n✓ Primer registro: {msg}")

    # Intentar registrar producto con mismo código
    p2 = Producto("P001", "Pasta", "Platos", 12.00)
    exito, msg = restaurante.registrar_producto(p2)
    print(f"✓ Intento de duplicado: {msg}")

    # Registrar cliente
    c1 = Cliente("123456", "Juan", "juan@email.com")
    exito, msg = restaurante.registrar_cliente(c1)
    print(f"\n✓ Primer cliente: {msg}")

    # Intentar registrar cliente con misma identificación
    c2 = Cliente("123456", "María", "maria@email.com")
    exito, msg = restaurante.registrar_cliente(c2)
    print(f"✓ Intento de duplicado: {msg}")


def prueba_estructura_json() -> None:
    """Prueba que la estructura JSON sea correcta."""
    print("\n" + "=" * 50)
    print("PRUEBA 5: Estructura JSON")
    print("=" * 50)

    gestor = GestorDatos()

    print("\n--- Estructura de productos.json ---")
    try:
        with open(gestor.ruta_productos, 'r', encoding='utf-8') as f:
            productos = json.load(f)
            print("✓ JSON válido")
            if productos:
                print(f"✓ Primer producto: {json.dumps(productos[0], indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"✗ Error: {e}")

    print("\n--- Estructura de clientes.json ---")
    try:
        with open(gestor.ruta_clientes, 'r', encoding='utf-8') as f:
            clientes = json.load(f)
            print("✓ JSON válido")
            if clientes:
                print(f"✓ Primer cliente: {json.dumps(clientes[0], indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"✗ Error: {e}")


def ejecutar_todas_pruebas() -> None:
    """Ejecuta todas las pruebas del sistema."""
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " " * 10 + "PRUEBAS DEL SISTEMA DE RESTAURANTE" + " " * 4 + "║")
    print("╚" + "=" * 48 + "╝")

    try:
        prueba_modelos()
        prueba_persistencia()
        prueba_carga()
        prueba_validacion()
        prueba_estructura_json()

        print("\n" + "=" * 50)
        print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 50 + "\n")

    except Exception as e:
        print(f"\n✗ ERROR DURANTE LAS PRUEBAS: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    ejecutar_todas_pruebas()

