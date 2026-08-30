"""Módulo de la clase Venta."""


class Venta:
    """Representa la relación entre un usuario y un producto vendido."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        if not usuario_id or not usuario_id.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        if not producto_codigo or not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")

        self.usuario_id: str = usuario_id.strip()
        self.producto_codigo: str = producto_codigo.strip()
        self.cantidad: int = int(cantidad)

    def mostrar_informacion(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Venta":
        if "usuario_id" not in datos:
            raise KeyError("Falta la clave 'usuario_id' en la venta.")
        if "producto_codigo" not in datos:
            raise KeyError("Falta la clave 'producto_codigo' en la venta.")
        if "cantidad" not in datos:
            raise KeyError("Falta la clave 'cantidad' en la venta.")

        return cls(
            datos["usuario_id"],
            datos["producto_codigo"],
            datos["cantidad"],
        )
