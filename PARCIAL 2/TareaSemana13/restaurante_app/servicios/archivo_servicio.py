"""Servicio de lectura y escritura de datos JSON del restaurante."""

from __future__ import annotations

import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:
    """Centraliza la carga de productos y usuarios desde archivos JSON."""

    def __init__(self, ruta_productos: str | None = None, ruta_usuarios: str | None = None) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.ruta_productos = os.path.abspath(ruta_productos or os.path.join(base_dir, "datos", "productos.json"))
        self.ruta_usuarios = os.path.abspath(ruta_usuarios or os.path.join(base_dir, "datos", "usuarios.json"))

    def cargar_productos(self) -> list[Producto]:
        if not os.path.exists(self.ruta_productos):
            return []

        with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Producto.desde_diccionario(item) for item in datos]

    def cargar_usuarios(self) -> list[Usuario]:
        if not os.path.exists(self.ruta_usuarios):
            return []

        with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Usuario.desde_diccionario(item) for item in datos]
