"""
Servicio principal del restaurante.
"""

from typing import Optional

from modelos import Cliente, Producto


class Restaurante:
    """Administra productos y clientes registrados."""

    def __init__(self, nombre: str, ubicacion: str) -> None:
        self.nombre: str = nombre
        self.ubicacion: str = ubicacion
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []
        self.contador_pedidos: int = 0

    def __str__(self) -> str:
        return (
            f"Restaurante: {self.nombre}\n"
            f"Ubicacion: {self.ubicacion}\n"
            f"Productos registrados: {len(self.productos)}\n"
            f"Clientes registrados: {len(self.clientes)}"
        )

    def registrar_producto(self, producto: Producto) -> bool:
        if any(item.nombre.lower() == producto.nombre.lower() for item in self.productos):
            return False
        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        if any(item.email.lower() == cliente.email.lower() for item in self.clientes):
            return False
        self.clientes.append(cliente)
        return True

    def obtener_producto_por_nombre(self, nombre: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def obtener_cliente_por_email(self, email: str) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.email.lower() == email.lower():
                return cliente
        return None

    def listar_productos(self) -> str:
        if not self.productos:
            return "No hay productos registrados."

        lineas = []
        categorias: dict[str, list[Producto]] = {}
        for producto in self.productos:
            if producto.disponible:
                categorias.setdefault(producto.categoria, []).append(producto)

        for categoria in sorted(categorias):
            lineas.append(f"\n{categoria.upper()}")
            lineas.append("-" * 40)
            for producto in categorias[categoria]:
                lineas.append(f"{producto.nombre}: ${producto.precio:.2f}")
                lineas.append(f"  -> {producto.descripcion}")
        return "\n".join(lineas)

    def listar_clientes(self) -> str:
        if not self.clientes:
            return "No hay clientes registrados."
        lineas = []
        for cliente in self.clientes:
            lineas.append(str(cliente))
            lineas.append("-" * 60)
        return "\n".join(lineas)

