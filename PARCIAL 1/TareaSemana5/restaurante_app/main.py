"""
Punto de entrada del sistema de restaurante.
"""

from modelos import Cliente, Producto
from servicios import Restaurante


def mostrar_titulo(titulo: str) -> None:
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def main() -> None:
    restaurante = Restaurante("Sabor Amazonico", "Puyo, Ecuador")

    producto_1 = Producto(
        "Ceviche de Tilapia",
        "Plato fresco preparado con tilapia, limon y especias locales",
        8.50,
        "plato principal",
    )
    producto_2 = Producto(
        "Jugo de Guayusa",
        "Bebida natural servida fria con un toque de miel",
        2.75,
        "bebida",
    )

    cliente_1 = Cliente(
        "Dayvis Aly Calderon Mendoza",
        "dayvis.calderon@correo.com",
        "0991234567",
        "Puyo, Pastaza",
    )
    cliente_2 = Cliente(
        "Maria Fernanda Torres",
        "maria.torres@correo.com",
        "0987654321",
        "Shell, Pastaza",
    )

    restaurante.registrar_producto(producto_1)
    restaurante.registrar_producto(producto_2)
    restaurante.registrar_cliente(cliente_1)
    restaurante.registrar_cliente(cliente_2)

    mostrar_titulo("RESUMEN DEL RESTAURANTE")
    print(restaurante)

    mostrar_titulo("PRODUCTOS REGISTRADOS")
    print(restaurante.listar_productos())

    mostrar_titulo("CLIENTES REGISTRADOS")
    print(restaurante.listar_clientes())


if __name__ == "__main__":
    main()

