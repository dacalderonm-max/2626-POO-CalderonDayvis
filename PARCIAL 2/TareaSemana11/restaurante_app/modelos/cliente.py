"""Compatibilidad con nombres anteriores de cliente."""

from modelos.usuario import Usuario


class Cliente(Usuario):
    """Alias funcional para mantener compatibilidad con la versión anterior."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        super().__init__(identificacion, nombre, correo)
