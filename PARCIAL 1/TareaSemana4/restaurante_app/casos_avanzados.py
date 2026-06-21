"""
Casos de Uso Avanzados del Sistema de Restaurante
Este archivo demuestra funcionalidades adicionales del sistema.
"""

from modelos import Producto, Cliente
from servicios import Restaurante


def demostrar_casos_avanzados():
    """
    Función que demuestra casos de uso más complejos del sistema de restaurante.
    """

    print("\n" + "=" * 70)
    print("CASOS DE USO AVANZADOS - SISTEMA DE RESTAURANTE")
    print("=" * 70 + "\n")

    # Crear restaurante
    restaurante = Restaurante("La Cocina Amazónica", "Tena, Ecuador")

    # =====================================================================
    # CASO 1: Manejo de productos duplicados
    # =====================================================================
    print("-" * 70)
    print("CASO 1: Prevención de Productos Duplicados")
    print("-" * 70 + "\n")

    producto1 = Producto("Arroz con Pollo", "Arroz sabroso con pollo", 12.00, "platos_principales")
    producto2 = Producto("Arroz con Pollo", "Otra versión del arroz con pollo", 13.00, "platos_principales")

    resultado1 = restaurante.registrar_producto(producto1)
    print(f"Primer registro de 'Arroz con Pollo': {'✓ Exitoso' if resultado1 else '✗ Duplicado'}")

    resultado2 = restaurante.registrar_producto(producto2)
    print(f"Segundo registro de 'Arroz con Pollo': {'✓ Exitoso' if resultado2 else '✗ Duplicado'}")

    # =====================================================================
    # CASO 2: Búsqueda case-insensitive
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 2: Búsqueda Case-Insensitive")
    print("-" * 70 + "\n")

    buscador = restaurante.obtener_producto_por_nombre("arroz CON POLLO")
    if buscador:
        print(f"Búsqueda encontrada independientemente de mayúsculas/minúsculas:")
        print(f"  Producto: {buscador.nombre}")
        print(f"  Precio: ${buscador.precio:.2f}")
    else:
        print("Producto no encontrado")

    # =====================================================================
    # CASO 3: Cambio de disponibilidad de productos
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 3: Cambio de Disponibilidad de Productos")
    print("-" * 70 + "\n")

    bebida = Producto("Chicha Morada", "Bebida tradicional ecuatoriana", 3.50, "bebidas")
    restaurante.registrar_producto(bebida)

    print(f"Estado inicial: {'Disponible' if bebida.disponible else 'No disponible'}")
    bebida.cambiar_disponibilidad()
    print(f"Después de cambio: {'Disponible' if bebida.disponible else 'No disponible'}")
    bebida.cambiar_disponibilidad()
    print(f"Después de otro cambio: {'Disponible' if bebida.disponible else 'No disponible'}")

    # =====================================================================
    # CASO 4: Validación de clientes duplicados
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 4: Prevención de Clientes Duplicados")
    print("-" * 70 + "\n")

    cliente1 = Cliente("Paula Rivadeneira", "paula@email.com", "0987654324", "Calle Héroes, Tena")
    cliente2 = Cliente("Paula Rivadeneira Silva", "paula@email.com", "0999999999", "Otra dirección")

    resultado1 = restaurante.registrar_cliente(cliente1)
    print(f"Primer registro de Paula (paula@email.com): {'✓ Exitoso' if resultado1 else '✗ Duplicado'}")

    resultado2 = restaurante.registrar_cliente(cliente2)
    print(f"Segundo registro con mismo email: {'✓ Exitoso' if resultado2 else '✗ Duplicado'}")

    # =====================================================================
    # CASO 5: Aplicación de descuentos en cascada
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 5: Aplicación de Descuentos")
    print("-" * 70 + "\n")

    plato = Producto("Sopa Amazónica", "Sopa de mariscos y vegetales",  18.00, "sopas")
    restaurante.registrar_producto(plato)

    print(f"Precio original: ${plato.precio:.2f}")
    plato.aplicar_descuento(10)
    print(f"Después de 10% descuento: ${plato.precio:.2f}")
    plato.aplicar_descuento(5)
    print(f"Después de 5% descuento adicional: ${plato.precio:.2f}")

    # =====================================================================
    # CASO 6: Múltiples pedidos por cliente
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 6: Múltiples Pedidos por Cliente")
    print("-" * 70 + "\n")

    cliente = Cliente("Ricardo Soto", "ricardo@email.com", "0987654325", "Av. Colón, Tena")
    restaurante.registrar_cliente(cliente)

    # Agregar más productos
    restaurante.registrar_producto(Producto("Lomo Saltado", "Lomo de res salteado con especias", 22.00, "platos_principales"))
    restaurante.registrar_producto(Producto("Papas a la Huancaína", "Papa con salsa amarilla", 8.00, "entradas"))

    # Crear primer pedido
    pedido1 = restaurante.crear_pedido(cliente, [("Arroz con Pollo", 1), ("Agua Mineral con Gas", 1)])
    if pedido1:
        print(f"Pedido 1: {pedido1['id']} - Total: ${pedido1['monto_total']:.2f}")

    # Crear segundo pedido
    pedido2 = restaurante.crear_pedido(cliente, [("Lomo Saltado", 1), ("Papas a la Huancaína", 2)])
    if pedido2:
        print(f"Pedido 2: {pedido2['id']} - Total: ${pedido2['monto_total']:.2f}")

    # Mostrar total gastado
    print(f"\nTotal gastado por {cliente.nombre}: ${cliente.obtener_total_gastado():.2f}")
    print(f"Número de pedidos realizados: {len(cliente.historial_pedidos)}")

    # =====================================================================
    # CASO 7: Cambio de estado de cliente
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 7: Cambio de Estado de Cliente")
    print("-" * 70 + "\n")

    print(f"Estado inicial de {cliente.nombre}: {'Activo' if cliente.activo else 'Inactivo'}")
    cliente.cambiar_estado()
    print(f"Después de cambio: {'Activo' if cliente.activo else 'Inactivo'}")

    # Intentar crear pedido con cliente inactivo
    pedido3 = restaurante.crear_pedido(cliente, [("Arroz con Pollo", 1)])
    if pedido3:
        print("Pedido creado exitosamente")
    else:
        print("No se pudo crear pedido: Cliente inactivo")

    # =====================================================================
    # CASO 8: Método __str__() en detalle
    # =====================================================================
    print("\n" + "-" * 70)
    print("CASO 8: Representación de Objetos (__str__())")
    print("-" * 70 + "\n")

    cliente.cambiar_estado()  # Volver a activar
    print("Información completa del cliente:\n")
    print(cliente)

    print("\n" + "=" * 70)
    print("FIN DE CASOS AVANZADOS")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    demostrar_casos_avanzados()

