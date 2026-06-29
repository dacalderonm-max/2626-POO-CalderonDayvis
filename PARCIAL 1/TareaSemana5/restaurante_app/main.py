"""
Punto de entrada principal del sistema de gestión de restaurante "El Sabor Zapotillano".
Autor: Dayvis Calderón
Sistema: Restaurante Lojano-Zapotillano
"""

from modelos import Producto, Cliente
from servicios import Restaurante


def main() -> None:
    """
    Función principal que demuestra el uso del sistema de gestión de restaurante.
    Crea instancias de productos y clientes, los registra en el restaurante,
    y muestra la información de forma organizada.
    """

    # ========== CREAR INSTANCIA DEL RESTAURANTE ==========
    # Se crea un restaurante con información descriptiva
    restaurante: Restaurante = Restaurante(
        nombre="El Sabor Zapotillano",
        ubicacion="Loja - Zapotillo, Ecuador",
    )

    print("=" * 70)
    print(f"BIENVENIDO A {restaurante.nombre.upper()}")
    print("=" * 70)
    print()

    # ========== CREAR PRODUCTOS ==========
    # Creación de platos y bebidas típicas del restaurante lojano

    # Producto 1: Ceviche
    ceviche: Producto = Producto(
        nombre="Ceviche de Camarón",
        descripcion="Ceviche fresco preparado con camarones del puerto ecuatoriano",
        precio=12.50,
        categoria="Platos Principales",
        disponible=True,
    )

    # Producto 2: Encocado
    encocado: Producto = Producto(
        nombre="Encocado de Atún",
        descripcion="Atún cocinado en salsa de coco, especialidad de la casa",
        precio=14.00,
        categoria="Platos Principales",
        disponible=True,
    )

    # Producto 3: Bebida típica
    bebida_tradicional: Producto = Producto(
        nombre="Chicha Morada",
        descripcion="Bebida tradicional lojana elaborada con maíz morado",
        precio=3.50,
        categoria="Bebidas",
        disponible=True,
    )

    # Producto 4: Postre
    postre: Producto = Producto(
        nombre="Flan de Zapotillo",
        descripcion="Postre especial hecho con frutas locales de Zapotillo",
        precio=4.75,
        categoria="Postres",
        disponible=True,
    )

    # ========== REGISTRAR PRODUCTOS ==========
    # Se agregan los productos a la lista del restaurante
    productos_a_registrar: list[Producto] = [ceviche, encocado, bebida_tradicional, postre]

    print("REGISTRANDO PRODUCTOS...")
    print("-" * 70)
    for producto in productos_a_registrar:
        if restaurante.registrar_producto(producto):
            print(f"✓ Producto registrado: {producto.nombre}")
        else:
            print(f"✗ No se pudo registrar: {producto.nombre}")
    print()

    # ========== CREAR CLIENTES ==========
    # Creación de clientes del restaurante

    # Cliente 1: Cliente frecuente
    cliente_frecuente: Cliente = Cliente(
        nombre_completo="Dayvis Calderón García",
        email="dayvis.calderon@email.com",
        numero_telefono="+593 98765432",
        es_miembro_frecuente=True,
    )

    # Cliente 2: Cliente nuevo
    cliente_nuevo: Cliente = Cliente(
        nombre_completo="María Rodríguez López",
        email="maria.rodriguez@email.com",
        numero_telefono="+593 99876543",
        es_miembro_frecuente=False,
    )

    # ========== REGISTRAR CLIENTES ==========
    # Se agregan los clientes a la lista del restaurante
    clientes_a_registrar: list[Cliente] = [cliente_frecuente, cliente_nuevo]

    print("REGISTRANDO CLIENTES...")
    print("-" * 70)
    for cliente in clientes_a_registrar:
        if restaurante.registrar_cliente(cliente):
            print(f"[OK] Cliente registrado: {cliente.nombre_completo}")
        else:
            print(f"[ERROR] No se pudo registrar: {cliente.nombre_completo}")
    print()

    # ========== SIMULAR ÓRDENES ==========
    # Se simula que los clientes han realizado órdenes
    cliente_frecuente.registrar_orden()
    cliente_frecuente.registrar_orden()
    cliente_nuevo.registrar_orden()

    # ========== MOSTRAR INFORMACIÓN REGISTRADA ==========
    print("=" * 70)
    print("INFORMACIÓN DEL RESTAURANTE")
    print("=" * 70)
    print(restaurante)
    print()

    # Mostrar productos disponibles
    print("=" * 70)
    print("CATÁLOGO DE PRODUCTOS")
    print("=" * 70)
    print(restaurante.listar_productos())
    print()

    # Mostrar clientes registrados
    print("=" * 70)
    print("CLIENTES REGISTRADOS")
    print("=" * 70)
    print(restaurante.listar_clientes())
    print()

    # ========== INFORMACIÓN ADICIONAL ==========
    print("=" * 70)
    print("INFORMACIÓN ADICIONAL DE CLIENTES")
    print("=" * 70)
    for cliente in clientes_a_registrar:
        print(f"\n{cliente.nombre_completo}:")
        print(f"  - Descuento aplicable: {cliente.obtener_descuento() * 100:.0f}%")
        print(
            f"  - Precio con IVA (Ceviche): "
            f"${restaurante.obtener_producto_por_nombre('Ceviche de Camarón').obtener_precio_con_iva():.2f}"
        )

    print("\n" + "=" * 70)
    print("FIN DEL PROGRAMA")
    print("=" * 70)


if __name__ == "__main__":
    main()


