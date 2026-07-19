"""
Módulo de la clase Cliente.
Define la clase que representa un cliente del restaurante.

Principio de Responsabilidad Única:
La clase Cliente únicamente se encarga de representar la información de un cliente.
No mantiene relación de herencia con Producto ya que son entidades conceptualmente diferentes.
"""


class Cliente:
    """
    Clase que representa un cliente registrado en el restaurante.

    Atributos:
        identificacion (str): Número único de identificación del cliente
        nombre (str): Nombre completo del cliente
        correo (str): Correo electrónico del cliente
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        """
        Inicializa una instancia de Cliente.

        Args:
            identificacion: Número único de identificación del cliente
            nombre: Nombre completo del cliente
            correo: Correo electrónico del cliente
        """
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        """
        Genera una representación en texto de la información del cliente.

        Returns:
            str: Información formateada del cliente
        """
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def obtener_identificacion(self) -> str:
        """
        Retorna la identificación del cliente.

        Returns:
            str: La identificación única del cliente
        """
        return self.identificacion

