"""
Modelo de producto del restaurante.
"""

from __future__ import annotations


class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre: str, descripcion: str, precio: float, categoria: str, disponible: bool = True) -> None:
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.categoria: str = categoria
        self.disponible: bool = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"[{self.categoria.upper()}] {self.nombre} - ${self.precio:.2f}\n"
            f"    Descripcion: {self.descripcion}\n"
            f"    Estado: {estado}"
        )

    def cambiar_disponibilidad(self) -> None:
        self.disponible = not self.disponible

    def aplicar_descuento(self, porcentaje: float) -> float:
        self.precio = self.precio * (1 - porcentaje / 100)
        return self.precio

