# -*- coding: utf-8 -*-
"""
Archivo Principal - main_interactivo.py
Versión interactiva del sistema de gestión de restaurante con menú.
Permite al usuario agregar productos y clientes manualmente.
"""

import sys
import io

# Configurar la salida de consola para UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    print("\n" + "="*70)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE - MENÚ PRINCIPAL")
    print("="*70)
    print("1. Gestionar Productos")
    print("2. Gestionar Clientes")
    print("3. Realizar Pedido")
    print("4. Ver Catálogo de Productos")
    print("5. Ver Clientes Registrados")
    print("6. Ver Estadísticas")
    print("7. Ver Inventario")
    print("8. Salir")
    print("="*70)


def mostrar_menu_productos():
    """Muestra el menú de gestión de productos."""
    print("\n" + "-"*70)
    print("GESTIÓN DE PRODUCTOS")
    print("-"*70)
    print("1. Agregar nuevo producto")
    print("2. Ver todos los productos")
    print("3. Volver al menú principal")
    print("-"*70)


def mostrar_menu_clientes():
    """Muestra el menú de gestión de clientes."""
    print("\n" + "-"*70)
    print("GESTIÓN DE CLIENTES")
    print("-"*70)
    print("1. Agregar nuevo cliente")
    print("2. Ver todos los clientes")
    print("3. Volver al menú principal")
    print("-"*70)


def agregar_producto_manual(restaurante):
    """Permite agregar un producto de forma manual."""
    print("\n" + "-"*70)
    print("AGREGAR NUEVO PRODUCTO")
    print("-"*70)

    try:
        id_producto = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ").strip()
        descripcion = input("Ingrese la descripción del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: $"))
        cantidad = int(input("Ingrese la cantidad disponible: "))

        if nombre == "" or descripcion == "":
            print("[ERROR] El nombre y descripción no pueden estar vacíos.")
            return
        
        if precio <= 0 or cantidad < 0:
            print("[ERROR] El precio debe ser positivo y la cantidad no debe ser negativa.")
            return

        producto = Producto(id_producto, nombre, descripcion, precio, cantidad)
        if restaurante.agregar_producto(producto):
            print("[OK] Producto agregado exitosamente.")

    except ValueError:
        print("[ERROR] Ingrese valores válidos (números donde se requiera).")
    except Exception as e:
        print(f"[ERROR] {str(e)}")


def agregar_cliente_manual(restaurante):
    """Permite agregar un cliente de forma manual."""
    print("\n" + "-"*70)
    print("AGREGAR NUEVO CLIENTE")
    print("-"*70)

    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))
        nombre = input("Ingrese el nombre del cliente: ").strip()
        email = input("Ingrese el email del cliente: ").strip()
        telefono = input("Ingrese el teléfono del cliente: ").strip()

        if nombre == "" or email == "" or telefono == "":
            print("[ERROR] Todos los campos son obligatorios.")
            return

        cliente = Cliente(id_cliente, nombre, email, telefono)
        if restaurante.agregar_cliente(cliente):
            print("✓ Cliente registrado exitosamente.")

    except ValueError:
        print("[ERROR] Ingrese un ID válido (número).")
    except Exception as e:
        print(f"[ERROR] {str(e)}")


def realizar_pedido_manual(restaurante):
    """Permite realizar un pedido de forma manual."""
    print("\n" + "-"*70)
    print("REALIZAR PEDIDO")
    print("-"*70)

    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))

        # Verificar que el cliente existe
        cliente = restaurante.obtener_cliente(id_cliente)
        if not cliente:
            print("[ERROR] Cliente no encontrado.")
            return
        
        print(f"[OK] Cliente: {cliente.nombre}")
        print("\nProductos disponibles:")
        
        if not restaurante.productos:
            print("[ERROR] No hay productos disponibles.")
            return

        for producto in restaurante.productos:
            print(f"  ID: {producto.id_producto} | {producto.nombre} - ${producto.precio:.2f} (Disponibles: {producto.cantidad_disponible})")

        productos_pedido = []

        while True:
            id_prod = input("\nIngrese el ID del producto (o 'fin' para terminar): ").strip()

            if id_prod.lower() == 'fin':
                break

            try:
                id_prod = int(id_prod)
                cantidad = int(input(f"¿Cuántas unidades desea de este producto? "))

                if cantidad <= 0:
                    print("[ERROR] La cantidad debe ser mayor a 0.")
                    continue

                productos_pedido.append((id_prod, cantidad))
                print("[OK] Producto agregado al pedido.")

            except ValueError:
                print("[ERROR] Ingrese valores válidos.")

        if productos_pedido:
            if restaurante.realizar_pedido(id_cliente, productos_pedido):
                print("[OK] Pedido realizado exitosamente.")
        else:
            print("[ERROR] El pedido está vacío.")

    except ValueError:
        print("[ERROR] Ingrese un ID de cliente válido.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")


def menu_productos(restaurante):
    """Menú de gestión de productos."""
    while True:
        mostrar_menu_productos()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregar_producto_manual(restaurante)
        elif opcion == "2":
            print(restaurante.listar_productos())
        elif opcion == "3":
            break
        else:
            print("[ERROR] Opción no válida. Intente de nuevo.")


def menu_clientes(restaurante):
    """Menú de gestión de clientes."""
    while True:
        mostrar_menu_clientes()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cliente_manual(restaurante)
        elif opcion == "2":
            print(restaurante.listar_clientes())
        elif opcion == "3":
            break
        else:
            print("[ERROR] Opción no válida. Intente de nuevo.")


def ver_cliente_detallado(restaurante):
    """Permite ver la información detallada de un cliente."""
    print("\n" + "-"*70)
    print("INFORMACIÓN DETALLADA DE CLIENTE")
    print("-"*70)

    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))
        cliente = restaurante.obtener_cliente(id_cliente)

        if not cliente:
            print("❌ Cliente no encontrado.")
            return

        print(f"\n✓ Cliente: {cliente.nombre}")
        info = cliente.obtener_informacion()
        for clave, valor in info.items():
            print(f"  • {clave}: {valor}")

        if cliente.obtener_pedidos():
            print(f"\n  Pedidos realizados:")
            for idx, pedido in enumerate(cliente.obtener_pedidos(), 1):
                print(f"    Pedido #{idx}:")
                for producto in pedido["productos"]:
                    print(f"      - {producto}")
                print(f"    Monto: ${pedido['monto']:.2f}")
        else:
            print(f"\n  Este cliente aún no tiene pedidos registrados.")

    except ValueError:
        print("❌ Error: Ingrese un ID válido.")


def main():
    """Función principal del programa interactivo."""

    print("\n" + "="*70)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*70)

    # Crear instancia del restaurante
    nombre_restaurante = input("\n¿Cuál es el nombre de su restaurante? ").strip()

    if nombre_restaurante == "":
        nombre_restaurante = "La Mesa Feliz"

    restaurante = Restaurante(nombre_restaurante)
    print(f"\n[OK] Restaurante '{nombre_restaurante}' creado exitosamente.\n")

    # Menú principal
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_productos(restaurante)

        elif opcion == "2":
            menu_clientes(restaurante)

        elif opcion == "3":
            realizar_pedido_manual(restaurante)

        elif opcion == "4":
            print(restaurante.listar_productos())

        elif opcion == "5":
            print(restaurante.listar_clientes())

        elif opcion == "6":
            print(restaurante.obtener_resumen_estadisticas())

        elif opcion == "7":
            print("\n" + "-"*70)
            print("INVENTARIO ACTUAL")
            print("-"*70)
            if restaurante.productos:
                for producto in restaurante.productos:
                    info = producto.obtener_informacion()
                    print(f"\n✓ {info['Nombre']}")
                    print(f"  • Descripción: {info['Descripción']}")
                    print(f"  • Precio: {info['Precio']}")
                    print(f"  • Disponibles: {info['Disponibles']} unidades")
            else:
                print("No hay productos registrados.")

        elif opcion == "8":
            print("\n" + "="*70)
            print("¡Gracias por usar el Sistema de Gestión de Restaurante!")
            print("="*70 + "\n")
            break
        
        else:
            print("[ERROR] Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    """
    Punto de entrada del programa interactivo.
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[ABORTADO] Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n[ERROR] Error inesperado: {str(e)}")

