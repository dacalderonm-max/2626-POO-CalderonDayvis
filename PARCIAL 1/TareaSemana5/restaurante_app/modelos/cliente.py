"""
Modelo de cliente del restaurante.
"""


class Cliente:
    """Representa a un cliente registrado en el restaurante."""

    def __init__(self, nombre: str, email: str, telefono: str, direccion: str, activo: bool = True) -> None:
        self.nombre: str = nombre
        self.email: str = email
        self.telefono: str = telefono
        self.direccion: str = direccion
        self.activo: bool = activo
        self.historial_pedidos: list[dict] = []

    def __str__(self) -> str:
        estado = "Activo" if self.activo else "Inactivo"
        return (
            f"Cliente: {self.nombre}\n"
            f"    Email: {self.email}\n"
            f"    Telefono: {self.telefono}\n"
            f"    Direccion: {self.direccion}\n"
            f"    Estado: {estado}\n"
            f"    Pedidos realizados: {len(self.historial_pedidos)}"
        )

    def cambiar_estado(self) -> None:
        self.activo = not self.activo

    def registrar_pedido(self, id_pedido: str, monto_total: float) -> None:
        self.historial_pedidos.append({"id_pedido": id_pedido, "monto_total": monto_total})

    def obtener_total_gastado(self) -> float:
        return sum(pedido["monto_total"] for pedido in self.historial_pedidos)

