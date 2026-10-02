"""Modelo del usuario para el acceso al sistema Restaurante App.

Semana 16: se consolidan los roles Administrador, Empleado y Cliente,
utilizados en la gestión de usuarios con eventos Tkinter.
"""


ROLES_VALIDOS = ("Administrador", "Empleado", "Cliente")


class Usuario:
    """Representa un usuario que puede ingresar al sistema del restaurante.

    Atributos:
        usuario  : identificador único de acceso.
        password : contraseña de acceso (no se expone en la interfaz).
        nombre   : nombre completo del usuario.
        rol      : diferencia entre Administrador, Empleado y Cliente.
    """

    def __init__(self, usuario: str, password: str, nombre: str, rol: str = "Empleado") -> None:
        if not usuario or not usuario.strip():
            raise ValueError("El nombre de usuario no puede estar vacío.")
        if not password or not password.strip():
            raise ValueError("La contraseña no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre completo no puede estar vacío.")

        self.usuario: str = usuario.strip()
        self.password: str = password.strip()
        self.nombre: str = nombre.strip()
        # Normalizar rol: si viene de datos viejos ("usuario","mesero") lo conservamos
        rol_norm = rol.strip() if rol else "Empleado"
        self.rol: str = rol_norm

    # ── Propiedades de conveniencia ───────────────────────────────────────────

    @property
    def es_administrador(self) -> bool:
        """True si el usuario tiene rol Administrador (insensible a mayúsculas)."""
        return self.rol.lower() == "administrador"

    # ── Representación ────────────────────────────────────────────────────────

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario} | Nombre: {self.nombre} | Rol: {self.rol}"

    # ── Serialización ─────────────────────────────────────────────────────────

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
            rol=str(datos.get("rol", "Empleado")),
        )
