"""Modelo del usuario para el acceso a la aplicación."""


class Usuario:
    """Representa un usuario que puede ingresar al sistema."""

    def __init__(self, usuario: str, password: str, nombre: str, rol: str = "usuario") -> None:
        if not usuario or not usuario.strip():
            raise ValueError("El usuario no puede estar vacío.")
        if not password or not password.strip():
            raise ValueError("La contraseña no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")

        self.usuario = usuario.strip()
        self.password = password.strip()
        self.nombre = nombre.strip()
        self.rol = rol.strip() or "usuario"

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario} | Nombre: {self.nombre} | Rol: {self.rol}"

    def a_diccionario(self) -> dict:
        return {
            "usuario": self.usuario,
            "password": self.password,
            "nombre": self.nombre,
            "rol": self.rol,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        return cls(
            usuario=str(datos["usuario"]),
            password=str(datos["password"]),
            nombre=str(datos["nombre"]),
            rol=str(datos.get("rol", "usuario")),
        )
