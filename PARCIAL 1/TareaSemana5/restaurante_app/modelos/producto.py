"""
Modelo de Producto - Representa un plato, bebida o producto disponible en el restaurante.
"""


class Producto:
    """
    Clase que representa un producto disponible en el restaurante "El Sabor Zapotillano".
    
    Atributos:
        nombre (str): Nombre descriptivo del producto.
        descripcion (str): Descripción detallada del producto.
        precio (float): Precio en dólares del producto.
        categoria (str): Categoría a la que pertenece (e.g., "Platos", "Bebidas").
        disponible (bool): Estado de disponibilidad del producto.
    """

    def __init__(
        self,
        nombre: str,
        descripcion: str,
        precio: float,
        categoria: str,
        disponible: bool = True,
    ) -> None:
        """
        Constructor de la clase Producto.

        Args:
            nombre: Nombre del producto.
            descripcion: Descripción del producto.
            precio: Precio en dólares.
            categoria: Categoría del producto.
            disponible: Estado del producto (por defecto, True).
        """
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.categoria: str = categoria
        self.disponible: bool = disponible

    def __str__(self) -> str:
        """
        Representación en texto del producto.

        Returns:
            Cadena con la información formateada del producto.
        """
        estado: str = "Disponible" if self.disponible else "No disponible"
        return (
            f"Producto: {self.nombre}\n"
            f"  Descripción: {self.descripcion}\n"
            f"  Categoría: {self.categoria}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Estado: {estado}"
        )

    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """
        Cambia el estado de disponibilidad del producto.

        Args:
            disponible: Nuevo estado de disponibilidad.
        """
        self.disponible = disponible

    def obtener_precio_con_iva(self, porcentaje_iva: float = 0.12) -> float:
        """
        Calcula el precio del producto con IVA incluido.

        Args:
            porcentaje_iva: Porcentaje de IVA a aplicar (por defecto 12%).

        Returns:
            Precio total con IVA incluido.
        """
        return self.precio * (1 + porcentaje_iva)

