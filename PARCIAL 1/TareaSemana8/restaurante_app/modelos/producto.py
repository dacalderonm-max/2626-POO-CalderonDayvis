"""
Módulo de la clase Producto.
Define la clase base que representa un producto del restaurante.

Principio de Responsabilidad Única:
La clase Producto únicamente se encarga de representar y mostrar la información
de un producto genérico del restaurante.
"""


class Producto:
    """
    Clase que representa un producto genérico del restaurante.

    Atributos:
        codigo (str): Identificador único del producto
        nombre (str): Nombre del producto
        categoria (str): Categoría del producto
        precio (float): Precio del producto en unidades monetarias
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        """
        Inicializa una instancia de Producto.

        Args:
            codigo: Identificador único del producto
            nombre: Nombre del producto
            categoria: Categoría a la que pertenece el producto
            precio: Precio del producto
        """
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        """
        Genera una representación en texto de la información del producto.

        Returns:
            str: Información formateada del producto
        """
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )

    def obtener_codigo(self) -> str:
        """
        Retorna el código del producto.

        Returns:
            str: El código único del producto
        """
        return self.codigo

