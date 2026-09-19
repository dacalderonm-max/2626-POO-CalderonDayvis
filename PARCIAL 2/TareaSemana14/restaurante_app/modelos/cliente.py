"""Compatibilidad con nombres anteriores de cliente."""

from modelos.usuario import Usuario


class Cliente(Usuario):
    """Alias funcional para mantener compatibilidad con la versión anterior."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        super().__init__(usuario=identificacion, password=correo, nombre=nombre, rol="cliente")
        self.identificacion = identificacion
        self.correo = correo

    def mostrar_informacion(self) -> str:
        return f"Cliente: {self.usuario} | Nombre: {self.nombre} | Correo: {self.correo}"

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.usuario,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Cliente":
        return cls(
            identificacion=str(datos.get("identificacion", datos.get("usuario", ""))),
            nombre=str(datos.get("nombre", "")),
            correo=str(datos.get("correo", datos.get("password", ""))),
        )
