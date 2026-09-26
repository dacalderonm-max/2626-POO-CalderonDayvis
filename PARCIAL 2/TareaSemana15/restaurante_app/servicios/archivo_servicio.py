"""Servicio de lectura y escritura de datos JSON del restaurante."""

from __future__ import annotations

import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Centraliza la carga y persistencia de productos, usuarios y ventas desde archivos JSON."""

    def __init__(
        self,
        ruta_productos: str | None = None,
        ruta_usuarios: str | None = None,
        ruta_ventas: str | None = None,
    ) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.ruta_productos = os.path.abspath(ruta_productos or os.path.join(base_dir, "datos", "productos.json"))
        self.ruta_usuarios = os.path.abspath(ruta_usuarios or os.path.join(base_dir, "datos", "usuarios.json"))
        self.ruta_ventas = os.path.abspath(ruta_ventas or os.path.join(base_dir, "datos", "ventas.json"))

    # ── Productos ─────────────────────────────────────────────

    def cargar_productos(self) -> list[Producto]:
        if not os.path.exists(self.ruta_productos):
            return []

        with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Producto.desde_diccionario(item) for item in datos]

    def guardar_productos(self, productos: list[Producto]) -> None:
        """Persiste la lista completa de productos en el archivo JSON."""
        self._guardar_json(self.ruta_productos, [p.a_diccionario() for p in productos])

    # ── Usuarios ──────────────────────────────────────────────

    def cargar_usuarios(self) -> list[Usuario]:
        if not os.path.exists(self.ruta_usuarios):
            return []

        with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Usuario.desde_diccionario(item) for item in datos]

    # ── Ventas ────────────────────────────────────────────────

    def cargar_ventas(self) -> list[Venta]:
        """Lee las ventas almacenadas en ventas.json."""
        if not os.path.exists(self.ruta_ventas):
            return []

        with open(self.ruta_ventas, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Venta.desde_diccionario(item) for item in datos]

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        """Persiste la lista completa de ventas en el archivo JSON."""
        self._guardar_json(self.ruta_ventas, [v.a_diccionario() for v in ventas])

    # ── Utilidades internas ───────────────────────────────────

    @staticmethod
    def _guardar_json(ruta: str, datos: list[dict]) -> None:
        """Escribe una lista de diccionarios en un archivo JSON."""
        directorio = os.path.dirname(ruta)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
