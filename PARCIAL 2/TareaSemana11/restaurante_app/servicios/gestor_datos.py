"""Gestor de datos JSON compatible con la versión anterior."""

import json
import os
from typing import List

from modelos.cliente import Cliente
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class GestorDatos:
    """Permite guardar y cargar productos, clientes/usuarios y ventas."""

    def __init__(
        self,
        ruta_productos: str | None = None,
        ruta_clientes: str | None = None,
        ruta_usuarios: str | None = None,
        ruta_ventas: str | None = None,
    ) -> None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.ruta_productos = ruta_productos or os.path.join(base_dir, "datos", "productos.json")
        self.ruta_clientes = ruta_clientes or os.path.join(base_dir, "datos", "clientes.json")
        self.ruta_usuarios = ruta_usuarios or os.path.join(base_dir, "datos", "usuarios.json")
        self.ruta_ventas = ruta_ventas or os.path.join(base_dir, "datos", "ventas.json")
        self._crear_directorio_datos()

    def _crear_directorio_datos(self) -> None:
        directorio = os.path.dirname(self.ruta_productos)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

    def guardar_productos(self, productos: List[Producto]) -> tuple[bool, str]:
        try:
            with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump([producto.a_diccionario() for producto in productos], archivo, indent=4, ensure_ascii=False)
            return True, f"Productos guardados exitosamente en {self.ruta_productos}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de productos: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir productos: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar productos: {exc}"

    def cargar_productos(self) -> tuple[bool, List[Producto], str]:
        try:
            if not os.path.exists(self.ruta_productos):
                return True, [], f"Archivo de productos no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
                productos_dict = json.load(archivo)
            productos = [Producto.desde_diccionario(item) for item in productos_dict]
            return True, productos, f"Productos cargados exitosamente. Total: {len(productos)}"
        except FileNotFoundError as exc:
            return False, [], f"Archivo no encontrado al cargar productos: {exc}"
        except json.JSONDecodeError as exc:
            return False, [], f"Contenido JSON inválido en productos: {exc}"
        except PermissionError as exc:
            return False, [], f"Sin permisos para leer productos: {exc}"
        except (KeyError, TypeError, ValueError) as exc:
            return False, [], f"Error al reconstruir productos: {exc}"

    def guardar_clientes(self, clientes: List[Cliente]) -> tuple[bool, str]:
        try:
            with open(self.ruta_clientes, "w", encoding="utf-8") as archivo:
                json.dump([cliente.a_diccionario() for cliente in clientes], archivo, indent=4, ensure_ascii=False)
            return True, f"Clientes guardados exitosamente en {self.ruta_clientes}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de clientes: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir clientes: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar clientes: {exc}"

    def cargar_clientes(self) -> tuple[bool, List[Cliente], str]:
        try:
            if not os.path.exists(self.ruta_clientes):
                return True, [], f"Archivo de clientes no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_clientes, "r", encoding="utf-8") as archivo:
                clientes_dict = json.load(archivo)
            clientes = [Cliente.desde_diccionario(item) for item in clientes_dict]
            return True, clientes, f"Clientes cargados exitosamente. Total: {len(clientes)}"
        except FileNotFoundError as exc:
            return False, [], f"Archivo no encontrado al cargar clientes: {exc}"
        except json.JSONDecodeError as exc:
            return False, [], f"Contenido JSON inválido en clientes: {exc}"
        except PermissionError as exc:
            return False, [], f"Sin permisos para leer clientes: {exc}"
        except (KeyError, TypeError, ValueError) as exc:
            return False, [], f"Error al reconstruir clientes: {exc}"

    def guardar_usuarios(self, usuarios: List[Usuario]) -> tuple[bool, str]:
        try:
            with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
                json.dump([usuario.a_diccionario() for usuario in usuarios], archivo, indent=4, ensure_ascii=False)
            return True, f"Usuarios guardados exitosamente en {self.ruta_usuarios}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de usuarios: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir usuarios: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar usuarios: {exc}"

    def cargar_usuarios(self) -> tuple[bool, List[Usuario], str]:
        try:
            if not os.path.exists(self.ruta_usuarios):
                return True, [], f"Archivo de usuarios no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
                usuarios_dict = json.load(archivo)
            usuarios = [Usuario.desde_diccionario(item) for item in usuarios_dict]
            return True, usuarios, f"Usuarios cargados exitosamente. Total: {len(usuarios)}"
        except FileNotFoundError as exc:
            return False, [], f"Archivo no encontrado al cargar usuarios: {exc}"
        except json.JSONDecodeError as exc:
            return False, [], f"Contenido JSON inválido en usuarios: {exc}"
        except PermissionError as exc:
            return False, [], f"Sin permisos para leer usuarios: {exc}"
        except (KeyError, TypeError, ValueError) as exc:
            return False, [], f"Error al reconstruir usuarios: {exc}"

    def guardar_ventas(self, ventas: List[Venta]) -> tuple[bool, str]:
        try:
            with open(self.ruta_ventas, "w", encoding="utf-8") as archivo:
                json.dump([venta.a_diccionario() for venta in ventas], archivo, indent=4, ensure_ascii=False)
            return True, f"Ventas guardadas exitosamente en {self.ruta_ventas}"
        except FileNotFoundError as exc:
            return False, f"No se encontró la ruta de ventas: {exc}"
        except PermissionError as exc:
            return False, f"No tiene permisos para escribir ventas: {exc}"
        except (TypeError, ValueError, OSError) as exc:
            return False, f"Error al guardar ventas: {exc}"

    def cargar_ventas(self) -> tuple[bool, List[Venta], str]:
        try:
            if not os.path.exists(self.ruta_ventas):
                return True, [], f"Archivo de ventas no encontrado. Se iniciará con lista vacía."
            with open(self.ruta_ventas, "r", encoding="utf-8") as archivo:
                ventas_dict = json.load(archivo)
            ventas = [Venta.desde_diccionario(item) for item in ventas_dict]
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
            for ruta in (self.ruta_productos, self.ruta_clientes, self.ruta_usuarios, self.ruta_ventas):
                if os.path.exists(ruta):
                   os.remove(ruta)
            return True, "Archivos de datos eliminados exitosamente."
        except FileNotFoundError as exc:
            return False, f"Falta un archivo al eliminar datos: {exc}"
        except PermissionError as exc:
            return False, f"Sin permisos para eliminar archivos: {exc}"
        except OSError as exc:
            return False, f"Error al eliminar archivos: {exc}"
