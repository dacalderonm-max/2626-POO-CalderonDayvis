"""Servicio para persistir productos, usuarios y ventas en JSON."""

import json
import os
from typing import Any

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Centraliza la lectura y escritura de archivos JSON del sistema."""

    def __init__(
        self,
        ruta_productos: str | None = None,
        ruta_usuarios: str | None = None,
        ruta_ventas: str | None = None,
    ) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.ruta_productos = ruta_productos or os.path.join(base_dir, "datos", "productos.json")
        self.ruta_usuarios = ruta_usuarios or os.path.join(base_dir, "datos", "usuarios.json")
        self.ruta_ventas = ruta_ventas or os.path.join(base_dir, "datos", "ventas.json")
        self._crear_directorio_datos()

    def _crear_directorio_datos(self) -> None:
        directorio = os.path.dirname(self.ruta_productos)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

    def guardar_productos(self, productos: list[Producto]) -> tuple[bool, str]:
        try:
            with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump([p.a_diccionario() for p in productos], archivo, indent=4, ensure_ascii=False)
            return True, f"Productos guardados exitosamente en {self.ruta_productos}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de productos: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir productos: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar productos: {exc}"

    def cargar_productos(self) -> tuple[bool, list[Producto], str]:
        try:
            if not os.path.exists(self.ruta_productos):
                return True, [], f"Archivo de productos no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            productos = [Producto.desde_diccionario(item) for item in datos]
            return True, productos, f"Productos cargados exitosamente. Total: {len(productos)}"
        except FileNotFoundError as exc:
            return False, [], f"Archivo no encontrado al cargar productos: {exc}"
        except json.JSONDecodeError as exc:
            return False, [], f"Contenido JSON inválido en productos: {exc}"
        except PermissionError as exc:
            return False, [], f"Sin permisos para leer productos: {exc}"
        except (KeyError, TypeError, ValueError) as exc:
            return False, [], f"Error al reconstruir productos: {exc}"

    def guardar_usuarios(self, usuarios: list[Usuario]) -> tuple[bool, str]:
        try:
            with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
                json.dump([u.a_diccionario() for u in usuarios], archivo, indent=4, ensure_ascii=False)
            return True, f"Usuarios guardados exitosamente en {self.ruta_usuarios}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de usuarios: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir usuarios: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar usuarios: {exc}"

    def cargar_usuarios(self) -> tuple[bool, list[Usuario], str]:
        try:
            if not os.path.exists(self.ruta_usuarios):
                return True, [], f"Archivo de usuarios no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            usuarios = [Usuario.desde_diccionario(item) for item in datos]
            return True, usuarios, f"Usuarios cargados exitosamente. Total: {len(usuarios)}"
        except FileNotFoundError as exc:
            return False, [], f"Archivo no encontrado al cargar usuarios: {exc}"
        except json.JSONDecodeError as exc:
            return False, [], f"Contenido JSON inválido en usuarios: {exc}"
        except PermissionError as exc:
            return False, [], f"Sin permisos para leer usuarios: {exc}"
        except (KeyError, TypeError, ValueError) as exc:
            return False, [], f"Error al reconstruir usuarios: {exc}"

    def guardar_ventas(self, ventas: list[Venta]) -> tuple[bool, str]:
        try:
            with open(self.ruta_ventas, "w", encoding="utf-8") as archivo:
                json.dump([v.a_diccionario() for v in ventas], archivo, indent=4, ensure_ascii=False)
            return True, f"Ventas guardadas exitosamente en {self.ruta_ventas}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de ventas: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir ventas: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar ventas: {exc}"

    def cargar_ventas(self) -> tuple[bool, list[Venta], str]:
        try:
            if not os.path.exists(self.ruta_ventas):
                return True, [], f"Archivo de ventas no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_ventas, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            ventas = [Venta.desde_diccionario(item) for item in datos]
            return True, ventas, f"Ventas cargadas exitosamente. Total: {len(ventas)}"
        except FileNotFoundError as exc:
            return False, [], f"Archivo no encontrado al cargar ventas: {exc}"
        except json.JSONDecodeError as exc:
            return False, [], f"Contenido JSON inválido en ventas: {exc}"
        except PermissionError as exc:
            return False, [], f"Sin permisos para leer ventas: {exc}"
        except (KeyError, TypeError, ValueError) as exc:
            return False, [], f"Error al reconstruir ventas: {exc}"

    def eliminar_archivos(self) -> tuple[bool, str]:
        try:
            for ruta in (self.ruta_productos, self.ruta_usuarios, self.ruta_ventas):
                if os.path.exists(ruta):
                    os.remove(ruta)
            return True, "Archivos de datos eliminados exitosamente."
        except FileNotFoundError as exc:
            return False, f"Falta un archivo al eliminar datos: {exc}"
        except PermissionError as exc:
            return False, f"Sin permisos para eliminar archivos: {exc}"
        except OSError as exc:
            return False, f"Error al eliminar archivos: {exc}"

    def guardar_todo(self, productos: list[Producto], usuarios: list[Usuario], ventas: list[Venta]) -> tuple[bool, str]:
        ok_productos, msg_productos = self.guardar_productos(productos)
        ok_usuarios, msg_usuarios = self.guardar_usuarios(usuarios)
        ok_ventas, msg_ventas = self.guardar_ventas(ventas)
        if ok_productos and ok_usuarios and ok_ventas:
            return True, "Datos guardados correctamente."
        errores = " | ".join(part for part in (msg_productos, msg_usuarios, msg_ventas) if part)
        return False, errores
