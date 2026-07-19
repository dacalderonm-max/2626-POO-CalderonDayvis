"""
Módulo de la clase Bebida.
Define la clase Bebida como una especialización de Producto.

Principio de Abierto/Cerrado:
La clase Bebida amplía el sistema sin modificar la clase Producto existente.

Principio de Sustitución de Liskov:
Un objeto Bebida puede utilizarse en cualquier lugar donde se espera un Producto
sin alterar el comportamiento del programa.
"""

from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida en el restaurante.
    Extiende la funcionalidad de Producto agregando atributos específicos de bebidas.

    Atributos heredados:
        codigo (str): Identificador único del producto
        nombre (str): Nombre del producto
        categoria (str): Categoría del producto
        precio (float): Precio del producto

    Atributos propios:
        tamaño (str): Tamaño de la bebida (pequeño, mediano, grande)
        tipo_envase (str): Tipo de envase (vaso, botella, lata)
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamaño: str,
        tipo_envase: str
    ) -> None:
        """
        Inicializa una instancia de Bebida.

        Args:
            codigo: Identificador único de la bebida
            nombre: Nombre de la bebida
            categoria: Categoría de la bebida
            precio: Precio de la bebida
            tamaño: Tamaño de la bebida
            tipo_envase: Tipo de envase de la bebida
        """
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño: str = tamaño
        self.tipo_envase: str = tipo_envase

    def mostrar_informacion(self) -> str:
        """
        Genera una representación en texto de la información de la bebida.
        Sobrescribe el método de la clase Producto para incluir información específica.

        Returns:
            str: Información formateada de la bebida
        """
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base} | Tamaño: {self.tamaño} | Envase: {self.tipo_envase}"

