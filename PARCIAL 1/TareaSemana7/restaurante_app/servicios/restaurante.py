"""
Módulo que define la clase Restaurante como servicio principal.
Administra las listas de productos y clientes del restaurante.
"""

from modelos import Producto, Cliente


class Restaurante:
    """
    Clase de servicio que administra productos y clientes del restaurante.
    Proporciona métodos para registrar, listar y buscar tanto productos
    como clientes.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre (str): Nombre del restaurante
        """
        self._nombre = nombre
        self._productos = []  # Lista de productos registrados
        self._clientes = []   # Lista de clientes registrados

    @property
    def nombre(self):
        """Obtiene el nombre del restaurante."""
        return self._nombre

    # ==================== MÉTODOS DE PRODUCTOS ====================

    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.

        Args:
            producto (Producto): Objeto de la clase Producto a registrar

        Returns:
            bool: True si el producto fue registrado exitosamente
        """
        if isinstance(producto, Producto):
            self._productos.append(producto)
            return True
        return False

    def listar_productos(self):
        """
        Obtiene la lista de todos los productos registrados.

        Returns:
            list: Lista de objetos Producto
        """
        return self._productos

    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre.

        Args:
            nombre (str): Nombre del producto a buscar

        Returns:
            list: Lista de productos que coinciden con el nombre
        """
        resultados = [
            p for p in self._productos
            if nombre.lower() in p.nombre.lower()
        ]
        return resultados

    def obtener_producto_por_indice(self, indice):
        """
        Obtiene un producto por su índice en la lista.

        Args:
            indice (int): Índice del producto

        Returns:
            Producto: El producto en el índice especificado o None
        """
        try:
            return self._productos[indice]
        except IndexError:
            return None

    def contar_productos(self):
        """
        Cuenta el total de productos registrados.

        Returns:
            int: Número de productos
        """
        return len(self._productos)

    # ==================== MÉTODOS DE CLIENTES ====================

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.

        Args:
            cliente (Cliente): Objeto de la clase Cliente a registrar

        Returns:
            bool: True si el cliente fue registrado exitosamente
        """
        if isinstance(cliente, Cliente):
            self._clientes.append(cliente)
            return True
        return False

    def listar_clientes(self):
        """
        Obtiene la lista de todos los clientes registrados.

        Returns:
            list: Lista de objetos Cliente
        """
        return self._clientes

    def buscar_cliente(self, nombre):
        """
        Busca un cliente por su nombre.

        Args:
            nombre (str): Nombre del cliente a buscar

        Returns:
            list: Lista de clientes que coinciden con el nombre
        """
        resultados = [
            c for c in self._clientes
            if nombre.lower() in c.nombre.lower()
        ]
        return resultados

    def obtener_cliente_por_indice(self, indice):
        """
        Obtiene un cliente por su índice en la lista.

        Args:
            indice (int): Índice del cliente

        Returns:
            Cliente: El cliente en el índice especificado o None
        """
        try:
            return self._clientes[indice]
        except IndexError:
            return None

    def contar_clientes(self):
        """
        Cuenta el total de clientes registrados.

        Returns:
            int: Número de clientes
        """
        return len(self._clientes)

    # ==================== MÉTODOS DE INFORMACIÓN ====================

    def obtener_resumen(self):
        """
        Obtiene un resumen del estado del restaurante.

        Returns:
            str: Información resumen del restaurante
        """
        return (
            f"Restaurante: {self._nombre}\n"
            f"Productos registrados: {self.contar_productos()}\n"
            f"Clientes registrados: {self.contar_clientes()}"
        )

