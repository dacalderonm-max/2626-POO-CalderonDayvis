"""
Módulo de la clase Restaurante.
Define el servicio principal que administra productos y clientes.

Principio de Responsabilidad Única:
La clase Restaurante únicamente se encarga de administrar las colecciones de productos y clientes,
validar duplicados y ejecutar operaciones de consulta.
"""

from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que representa el servicio del restaurante.
    Administra las colecciones de productos y clientes del sistema.

    Atributos:
        productos (List[Producto]): Lista de productos registrados (incluye bebidas)
        clientes (List[Cliente]): Lista de clientes registrados
    """

    def __init__(self) -> None:
        """Inicializa una instancia de Restaurante con listas vacías."""
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    # ==================== MÉTODOS DE PRODUCTOS ====================

    def registrar_producto(self, producto: Producto) -> tuple[bool, str]:
        """
        Registra un nuevo producto en el sistema.
        Valida que el código no esté duplicado.

        Nota sobre Sustitución de Liskov:
        Este método acepta tanto Producto como Bebida sin distinción,
        demostrando que Bebida puede sustituir a Producto transparentemente.

        Args:
            producto: Objeto Producto o Bebida a registrar

        Returns:
            Tupla con (éxito: bool, mensaje: str)
        """
        # Validar código duplicado
        if self._codigo_existe(producto.obtener_codigo()):
            return False, f"Error: El código '{producto.obtener_codigo()}' ya existe."

        self.productos.append(producto)
        return True, f"Producto registrado exitosamente: {producto.nombre}"

    def _codigo_existe(self, codigo: str) -> bool:
        """
        Verifica si un código de producto ya existe en el sistema.

        Args:
            codigo: Código a verificar

        Returns:
            bool: True si el código existe, False en caso contrario
        """
        return any(producto.obtener_codigo() == codigo for producto in self.productos)

    def listar_productos(self) -> List[str]:
        """
        Lista todos los productos registrados.

        Polimorfismo en acción:
        Ejecuta mostrar_informacion() en todos los productos (Producto y Bebida)
        sin necesidad de condicionales para determinar el tipo exacto.

        Returns:
            Lista de strings con la información formateada de cada producto
        """
        if not self.productos:
            return ["No hay productos registrados."]

        resultado: List[str] = []
        for producto in self.productos:
            # Polimorfismo: cada objeto ejecuta su propia versión de mostrar_informacion()
            resultado.append(producto.mostrar_informacion())
        return resultado

    def obtener_cantidad_productos(self) -> int:
        """
        Retorna la cantidad total de productos registrados.

        Returns:
            int: Cantidad de productos
        """
        return len(self.productos)

    # ==================== MÉTODOS DE CLIENTES ====================

    def registrar_cliente(self, cliente: Cliente) -> tuple[bool, str]:
        """
        Registra un nuevo cliente en el sistema.
        Valida que la identificación no esté duplicada.

        Args:
            cliente: Objeto Cliente a registrar

        Returns:
            Tupla con (éxito: bool, mensaje: str)
        """
        # Validar identificación duplicada
        if self._identificacion_existe(cliente.obtener_identificacion()):
            return False, f"Error: La identificación '{cliente.obtener_identificacion()}' ya existe."

        self.clientes.append(cliente)
        return True, f"Cliente registrado exitosamente: {cliente.nombre}"

    def _identificacion_existe(self, identificacion: str) -> bool:
        """
        Verifica si una identificación de cliente ya existe en el sistema.

        Args:
            identificacion: Identificación a verificar

        Returns:
            bool: True si la identificación existe, False en caso contrario
        """
        return any(cliente.obtener_identificacion() == identificacion for cliente in self.clientes)

    def listar_clientes(self) -> List[str]:
        """
        Lista todos los clientes registrados.

        Returns:
            Lista de strings con la información formateada de cada cliente
        """
        if not self.clientes:
            return ["No hay clientes registrados."]

        resultado: List[str] = []
        for cliente in self.clientes:
            resultado.append(cliente.mostrar_informacion())
        return resultado

    def obtener_cantidad_clientes(self) -> int:
        """
        Retorna la cantidad total de clientes registrados.

        Returns:
            int: Cantidad de clientes
        """
        return len(self.clientes)

