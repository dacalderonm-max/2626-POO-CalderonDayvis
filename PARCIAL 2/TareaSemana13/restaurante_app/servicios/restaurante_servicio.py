"""Servicio principal del restaurante para la capa de negocio."""

from __future__ import annotations

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina la carga de datos y las operaciones del restaurante."""

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self) -> None:
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario: str, password: str) -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        password_limpio = (password or "").strip()

        if not usuario_limpio or not password_limpio:
            return False, "Debe ingresar usuario y contraseña."

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario_limpio.lower() and usuario_registrado.password == password_limpio:
                return True, f"Bienvenido, {usuario_registrado.nombre}."

        return False, "Usuario o contraseña incorrectos."

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.usuarios)

    def consultar_stock(self, codigo: str) -> int | None:
        for producto in self.productos:
            if producto.codigo.lower() == codigo.strip().lower():
                return producto.stock
        return None

    def obtener_productos_formateados(self) -> list[str]:
        if not self.productos:
            return ["No hay productos registrados."]
        return [producto.mostrar_informacion() for producto in self.productos]

    def obtener_usuarios_formateados(self) -> list[str]:
        if not self.usuarios:
            return ["No hay usuarios registrados."]
        return [usuario.mostrar_informacion() for usuario in self.usuarios]
