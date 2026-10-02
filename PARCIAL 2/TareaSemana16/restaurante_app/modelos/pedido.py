"""Modelo del pedido realizado por un Cliente.

Semana 16 (extensión): un Cliente crea un pedido con estado 'pendiente'.
El Administrador o Empleado lo aprueba (convirtiéndolo en Venta)
o lo rechaza. El stock solo se descuenta al aprobar.

Estados posibles:
    pendiente  → recién creado, esperando resolución.
    aprobado   → convertido en Venta; stock ya descontado.
    rechazado  → cancelado por Admin/Empleado.
"""

from __future__ import annotations

from datetime import datetime


ESTADOS_PEDIDO = ("pendiente", "aprobado", "rechazado")


class Pedido:
    """Representa una solicitud de compra de un Cliente, pendiente de aprobación."""

    def __init__(
        self,
        pedido_id: str,
        cliente_id: str,
        producto_codigo: str,
        cantidad: int,
        estado: str = "pendiente",
        fecha: str = "",
        fecha_resolucion: str = "",
    ) -> None:
        if not pedido_id or not pedido_id.strip():
            raise ValueError("El identificador del pedido no puede estar vacío.")
        if not cliente_id or not cliente_id.strip():
            raise ValueError("El identificador del cliente no puede estar vacío.")
        if not producto_codigo or not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        if int(cantidad) <= 0:
            raise ValueError("La cantidad del pedido debe ser mayor que cero.")

        self.pedido_id: str = pedido_id.strip()
        self.cliente_id: str = cliente_id.strip()
        self.producto_codigo: str = producto_codigo.strip()
        self.cantidad: int = int(cantidad)
        self.estado: str = estado.strip() if estado else "pendiente"
        self.fecha: str = fecha.strip() if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_resolucion: str = fecha_resolucion.strip() if fecha_resolucion else ""

    @property
    def es_pendiente(self) -> bool:
        return self.estado == "pendiente"

    def mostrar_informacion(self) -> str:
        return (
            f"Pedido {self.pedido_id} | Cliente: {self.cliente_id} | "
            f"Producto: {self.producto_codigo} | Cantidad: {self.cantidad} | "
            f"Estado: {self.estado} | Fecha: {self.fecha}"
        )

    def a_diccionario(self) -> dict:
        return {
            "pedido_id": self.pedido_id,
            "cliente_id": self.cliente_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "estado": self.estado,
            "fecha": self.fecha,
            "fecha_resolucion": self.fecha_resolucion,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Pedido":
        return cls(
            pedido_id=str(datos["pedido_id"]),
            cliente_id=str(datos["cliente_id"]),
            producto_codigo=str(datos["producto_codigo"]),
            cantidad=int(datos["cantidad"]),
            estado=str(datos.get("estado", "pendiente")),
            fecha=str(datos.get("fecha", "")),
            fecha_resolucion=str(datos.get("fecha_resolucion", "")),
        )
