"""
Módulo que define la clase Cliente utilizando el decorador @dataclass.
"""

from dataclasses import dataclass, field


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    Implementada mediante el decorador @dataclass para simplificar
    la creación de objetos con datos básicos.
    """

    nombre: str
    correo: str
    id_cliente: str = field(default_factory=lambda: "")

    def __post_init__(self):
        """
        Validaciones que se ejecutan después de la inicialización.
        """
        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío")
        if not self.correo or not self.correo.strip():
            raise ValueError("El correo del cliente no puede estar vacío")

        # Limpiar espacios en blanco
        self.nombre = self.nombre.strip()
        self.correo = self.correo.strip()
        self.id_cliente = self.id_cliente.strip()

    def mostrar_informacion(self):
        """
        Método que muestra la información del cliente de forma legible.

        Returns:
            str: Información formateada del cliente
        """
        return (
            f"ID: {self.id_cliente}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )

    def __str__(self):
        """Representación en string del cliente."""
        return f"{self.nombre} ({self.correo})"

