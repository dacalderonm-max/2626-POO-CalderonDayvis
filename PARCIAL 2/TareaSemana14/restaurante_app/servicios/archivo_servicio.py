"""Servicio de lectura y escritura de datos JSON del restaurante."""

from __future__ import annotations

import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Centraliza la carga y persistencia de productos, usuarios y ventas desde JSON."""

    def __init__(self, ruta_productos: str | None = None, ruta_usuarios: str | None = None, ruta_ventas: str | None = None) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.ruta_productos = os.path.abspath(ruta_productos or os.path.join(base_dir, "datos", "productos.json"))
        self.ruta_usuarios = os.path.abspath(ruta_usuarios or os.path.join(base_dir, "datos", "usuarios.json"))
        self.ruta_ventas = os.path.abspath(ruta_ventas or os.path.join(base_dir, "datos", "ventas.json"))

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

    def cargar_ventas(self) -> list[Venta]:
        if not os.path.exists(self.ruta_ventas):
            return []

        with open(self.ruta_ventas, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Venta.desde_diccionario(item) for item in datos]

    def guardar_productos(self, productos: list[Producto]) -> None:
        os.makedirs(os.path.dirname(self.ruta_productos), exist_ok=True)

        with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
            json.dump(
                [producto.a_diccionario() for producto in productos],
                archivo,
                ensure_ascii=False,
                indent=4,
            )
            archivo.write("\n")

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        os.makedirs(os.path.dirname(self.ruta_usuarios), exist_ok=True)

        with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
            json.dump(
                [usuario.a_diccionario() for usuario in usuarios],
                archivo,
                ensure_ascii=False,
                indent=4,
            )
            archivo.write("\n")

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        os.makedirs(os.path.dirname(self.ruta_ventas), exist_ok=True)

        with open(self.ruta_ventas, "w", encoding="utf-8") as archivo:
            json.dump(
                [venta.a_diccionario() for venta in ventas],
                archivo,
                ensure_ascii=False,
                indent=4,
            )
            archivo.write("\n")
