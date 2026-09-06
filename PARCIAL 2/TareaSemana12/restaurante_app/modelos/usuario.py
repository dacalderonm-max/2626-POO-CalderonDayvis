"""Módulo de la clase Usuario."""


class Usuario:
    """Representa una persona registrada que puede realizar compras."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion or not identificacion.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        if not correo or not correo.strip():
            raise ValueError("El correo del usuario no puede estar vacío.")

        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()

    def mostrar_informacion(self) -> str:
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def obtener_identificacion(self) -> str:
        return self.identificacion

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        if "identificacion" not in datos:
            raise KeyError("Falta la clave 'identificacion' en el usuario.")
        if "nombre" not in datos:
            raise KeyError("Falta la clave 'nombre' en el usuario.")
        if "correo" not in datos:
            raise KeyError("Falta la clave 'correo' en el usuario.")

        return cls(
            datos["identificacion"],
            datos["nombre"],
            datos["correo"],
        )
