"""
Archivo Principal - main.py
Punto de entrada de la aplicación de gestión de restaurante.
Demuestra el funcionamiento del sistema creando objetos e interactuando con ellos.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """
    Función principal que ejecuta la aplicación.
    Demuestra la creación de objetos y las operaciones del restaurante.
    """

    print("\n" + "="*70)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE - POO")
    print("="*70 + "\n")

    # Crear una instancia del restaurante
    restaurante = Restaurante("La Mesa Feliz")
    print(f"✓ Restaurante creado: {restaurante}")

    # ========== CREAR PRODUCTOS ==========
    print("\n" + "-"*70)
    print("CREANDO PRODUCTOS")
    print("-"*70)

    # Crear objetos de tipo Producto
    producto1 = Producto(1, "Hamburguesa Clásica", "Hamburguesa jugosa con queso y lechuga", 8.99, 50)
    producto2 = Producto(2, "Pizza Margherita", "Pizza tradicional con tomate, queso y albahaca", 12.50, 30)
    producto3 = Producto(3, "Refresco Cola", "Bebida refrescante de cola 350ml", 2.50, 100)
    producto4 = Producto(4, "Esteak a la Parrilla", "Filete premium a la parrilla con verduras", 18.99, 20)
    producto5 = Producto(5, "Ensalada César", "Ensalada fresca con aderezo César y crutones", 7.99, 40)

    # Agregar productos al restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)
    restaurante.agregar_producto(producto5)

    # ========== CREAR CLIENTES ==========
    print("\n" + "-"*70)
    print("REGISTRANDO CLIENTES")
    print("-"*70)

    # Crear objetos de tipo Cliente
    cliente1 = Cliente(101, "Juan Pérez", "juan.perez@email.com", "+593-999-1234")
    cliente2 = Cliente(102, "María García", "maria.garcia@email.com", "+593-998-5678")
    cliente3 = Cliente(103, "Carlos López", "carlos.lopez@email.com", "+593-997-9012")

    # Agregar clientes al restaurante
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    restaurante.agregar_cliente(cliente3)

    # ========== MOSTRAR CATÁLOGO ==========
    print(restaurante.listar_productos())

    # ========== REALIZAR PEDIDOS ==========
    print("-"*70)
    print("REALIZANDO PEDIDOS")
    print("-"*70)

    # Cliente 1 realiza un pedido
    print(f"\n→ {cliente1.nombre} realiza un pedido:")
    restaurante.realizar_pedido(101, [(1, 2), (3, 3)])  # 2 hamburguesas y 3 refrescos

    # Cliente 2 realiza un pedido
    print(f"\n→ {cliente2.nombre} realiza un pedido:")
    restaurante.realizar_pedido(102, [(2, 1), (5, 2)])  # 1 pizza y 2 ensaladas

    # Cliente 3 realiza un pedido
    print(f"\n→ {cliente3.nombre} realiza un pedido:")
    restaurante.realizar_pedido(103, [(4, 1), (1, 1), (3, 2)])  # 1 steak, 1 hamburguesa y 2 refrescos

    # ========== MOSTRAR CLIENTES REGISTRADOS ==========
    print(restaurante.listar_clientes())

    # ========== INFORMACIÓN DETALLADA DE CLIENTE ==========
    print("-"*70)
    print("INFORMACIÓN DETALLADA DE UN CLIENTE")
    print("-"*70)

    cliente_seleccionado = restaurante.obtener_cliente(101)
    if cliente_seleccionado:
        print(f"\n✓ Cliente: {cliente_seleccionado.nombre}")
        info = cliente_seleccionado.obtener_informacion()
        for clave, valor in info.items():
            print(f"  • {clave}: {valor}")

        print(f"\n  Pedidos realizados:")
        for idx, pedido in enumerate(cliente_seleccionado.obtener_pedidos(), 1):
            print(f"    Pedido #{idx}:")
            for producto in pedido["productos"]:
                print(f"      - {producto}")
            print(f"    Monto: {pedido['monto']:.2f}")

    # ========== VERIFICAR DISPONIBILIDAD DE PRODUCTOS ==========
    print("\n" + "-"*70)
    print("INVENTARIO ACTUAL DE PRODUCTOS")
    print("-"*70)

    for producto in [producto1, producto2, producto3, producto4, producto5]:
        info = producto.obtener_informacion()
        print(f"\n✓ {info['Nombre']}")
        print(f"  • Descripción: {info['Descripción']}")
        print(f"  • Precio: {info['Precio']}")
        print(f"  • Disponibles: {info['Disponibles']} unidades")

    # ========== MOSTRAR ESTADÍSTICAS ==========
    print(restaurante.obtener_resumen_estadisticas())

    # ========== DEMOSTRACIÓN DE __str__() ==========
    print("-"*70)
    print("REPRESENTACIÓN EN TEXTO USANDO __str__()")
    print("-"*70)

    print(f"\n✓ Restaurante: {str(restaurante)}")
    print(f"✓ Primer Producto: {str(producto1)}")
    print(f"✓ Primer Cliente: {str(cliente1)}")

    print("\n" + "="*70)
    print("FIN DE LA DEMOSTRACIÓN DEL SISTEMA")
    print("="*70 + "\n")


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Se ejecuta solo si el archivo se corre directamente.
    """
    main()

