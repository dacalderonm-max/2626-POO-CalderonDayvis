"""
Módulo de la clase GestorDatos.
Administra la persistencia de datos en archivos JSON.

Principio de Responsabilidad Única:
Esta clase únicamente se encarga de guardar y cargar datos desde archivos JSON.
"""

import json
import os
from typing import List, Dict, Any
from modelos.producto import Producto
from modelos.cliente import Cliente


class GestorDatos:
    """
    Clase que administra la persistencia de datos en archivos JSON.
    Convierte objetos de negocio a diccionarios y viceversa.

    Atributos:
        ruta_productos (str): Ruta del archivo JSON para productos
        ruta_clientes (str): Ruta del archivo JSON para clientes
    """

    def __init__(self, ruta_productos: str = "datos/productos.json",
                 ruta_clientes: str = "datos/clientes.json") -> None:
        """
        Inicializa el gestor de datos.

        Args:
            ruta_productos: Ruta del archivo JSON para productos
            ruta_clientes: Ruta del archivo JSON para clientes
        """
        self.ruta_productos: str = ruta_productos
        self.ruta_clientes: str = ruta_clientes

        # Crear directorio de datos si no existe
        self._crear_directorio_datos()

    def _crear_directorio_datos(self) -> None:
        """Crea el directorio para guardar archivos JSON si no existe."""
        directorio = os.path.dirname(self.ruta_productos)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    # ==================== MÉTODOS PARA PRODUCTOS ====================

    def guardar_productos(self, productos: List[Producto]) -> tuple[bool, str]:
        """
        Guarda la lista de productos en un archivo JSON.

        Args:
            productos: Lista de productos a guardar

        Returns:
            Tupla con (éxito: bool, mensaje: str)
        """
        try:
            # Convertir productos a diccionarios
            productos_dict = [producto.a_diccionario() for producto in productos]

            # Guardar en JSON
            with open(self.ruta_productos, 'w', encoding='utf-8') as archivo:
                json.dump(productos_dict, archivo, indent=4, ensure_ascii=False)

            return True, f"Productos guardados exitosamente en {self.ruta_productos}"
        except Exception as e:
            return False, f"Error al guardar productos: {str(e)}"

    def cargar_productos(self) -> tuple[bool, List[Producto], str]:
        """
        Carga la lista de productos desde un archivo JSON.

        Returns:
            Tupla con (éxito: bool, lista_productos: List[Producto], mensaje: str)
        """
        try:
            if not os.path.exists(self.ruta_productos):
                return True, [], f"Archivo de productos no encontrado. Se iniciará con lista vacía."

            with open(self.ruta_productos, 'r', encoding='utf-8') as archivo:
                productos_dict = json.load(archivo)

            # Convertir diccionarios a objetos Producto
            productos = [Producto.desde_diccionario(p) for p in productos_dict]

            return True, productos, f"Productos cargados exitosamente. Total: {len(productos)}"
        except Exception as e:
            return False, [], f"Error al cargar productos: {str(e)}"

    # ==================== MÉTODOS PARA CLIENTES ====================

    def guardar_clientes(self, clientes: List[Cliente]) -> tuple[bool, str]:
        """
        Guarda la lista de clientes en un archivo JSON.

        Args:
            clientes: Lista de clientes a guardar

        Returns:
            Tupla con (éxito: bool, mensaje: str)
        """
        try:
            # Convertir clientes a diccionarios
            clientes_dict = [cliente.a_diccionario() for cliente in clientes]

            # Guardar en JSON
            with open(self.ruta_clientes, 'w', encoding='utf-8') as archivo:
                json.dump(clientes_dict, archivo, indent=4, ensure_ascii=False)

            return True, f"Clientes guardados exitosamente en {self.ruta_clientes}"
        except Exception as e:
            return False, f"Error al guardar clientes: {str(e)}"

    def cargar_clientes(self) -> tuple[bool, List[Cliente], str]:
        """
        Carga la lista de clientes desde un archivo JSON.

        Returns:
            Tupla con (éxito: bool, lista_clientes: List[Cliente], mensaje: str)
        """
        try:
            if not os.path.exists(self.ruta_clientes):
                return True, [], f"Archivo de clientes no encontrado. Se iniciará con lista vacía."

            with open(self.ruta_clientes, 'r', encoding='utf-8') as archivo:
                clientes_dict = json.load(archivo)

            # Convertir diccionarios a objetos Cliente
            clientes = [Cliente.desde_diccionario(c) for c in clientes_dict]

            return True, clientes, f"Clientes cargados exitosamente. Total: {len(clientes)}"
        except Exception as e:
            return False, [], f"Error al cargar clientes: {str(e)}"

    # ==================== MÉTODOS GENERALES ====================

    def eliminar_archivos(self) -> tuple[bool, str]:
        """
        Elimina los archivos de datos.

        Returns:
            Tupla con (éxito: bool, mensaje: str)
        """
        try:
            if os.path.exists(self.ruta_productos):
                os.remove(self.ruta_productos)
            if os.path.exists(self.ruta_clientes):
                os.remove(self.ruta_clientes)
            return True, "Archivos de datos eliminados exitosamente."
        except Exception as e:
            return False, f"Error al eliminar archivos: {str(e)}"



