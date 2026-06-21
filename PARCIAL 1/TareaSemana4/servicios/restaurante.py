"""
Módulo de Servicios - Restaurante
Define la clase Restaurante que gestiona los productos y clientes del sistema.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que gestiona el restaurante, administrando productos y clientes.

    Atributos:
        nombre_restaurante (str): nombre del restaurante
        productos (list): lista de productos disponibles
        clientes (list): lista de clientes registrados
    """

    def __init__(self, nombre_restaurante):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre_restaurante (str): nombre del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.productos = []
        self.clientes = []

    def __str__(self):
        """
        Representación en texto del restaurante.

        Returns:
            str: información del restaurante
        """
        return f"Restaurante: {self.nombre_restaurante} | Productos: {len(self.productos)} | Clientes: {len(self.clientes)}"

    def agregar_producto(self, producto):
        """
        Agrega un producto al catálogo del restaurante.

        Args:
            producto (Producto): objeto de la clase Producto

        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        # Verificar si producto ya existe
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print(f"Error: El producto con ID {producto.id_producto} ya existe.")
                return False

        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado exitosamente.")
        return True

    def obtener_producto(self, id_producto):
        """
        Obtiene un producto por su ID.

        Args:
            id_producto (int): identificador del producto

        Returns:
            Producto: objeto del producto si existe, None si no
        """
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def agregar_cliente(self, cliente):
        """
        Agrega un cliente al sistema del restaurante.

        Args:
            cliente (Cliente): objeto de la clase Cliente

        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        # Verificar si cliente ya existe
        for c in self.clientes:
            if c.id_cliente == cliente.id_cliente:
                print(f"Error: El cliente con ID {cliente.id_cliente} ya existe.")
                return False

        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado exitosamente.")
        return True

    def obtener_cliente(self, id_cliente):
        """
        Obtiene un cliente por su ID.

        Args:
            id_cliente (int): identificador del cliente

        Returns:
            Cliente: objeto del cliente si existe, None si no
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def realizar_pedido(self, id_cliente, productos_pedido):
        """
        Realiza un pedido para un cliente.

        Args:
            id_cliente (int): identificador del cliente
            productos_pedido (list): lista de tuplas (id_producto, cantidad)

        Returns:
            bool: True si el pedido se realizó exitosamente
        """
        cliente = self.obtener_cliente(id_cliente)
        if not cliente:
            print(f"Error: Cliente con ID {id_cliente} no encontrado.")
            return False

        monto_total = 0
        productos_nombres = []

        for id_prod, cantidad in productos_pedido:
            producto = self.obtener_producto(id_prod)
            if not producto:
                print(f"Error: Producto con ID {id_prod} no encontrado.")
                return False

            if producto.cantidad_disponible < cantidad:
                print(f"Error: No hay suficiente cantidad de '{producto.nombre}'")
                return False

            monto_total += producto.precio * cantidad
            productos_nombres.append(f"{cantidad}x {producto.nombre}")
            producto.actualizar_disponibilidad(cantidad)

        pedido = {
            "productos": productos_nombres,
            "monto": monto_total
        }

        cliente.registrar_pedido(pedido)
        print(f"Pedido realizado para {cliente.nombre}: ${monto_total:.2f}")
        return True

    def listar_productos(self):
        """
        Muestra el catálogo de productos disponibles.

        Returns:
            str: información de todos los productos
        """
        if not self.productos:
            return "No hay productos disponibles."

        resultado = f"\n{'='*70}\n"
        resultado += f"CATÁLOGO DE PRODUCTOS - {self.nombre_restaurante}\n"
        resultado += f"{'='*70}\n"

        for producto in self.productos:
            resultado += f"• {producto}\n"

        resultado += f"{'='*70}\n"
        return resultado

    def listar_clientes(self):
        """
        Muestra la información de los clientes registrados.

        Returns:
            str: información de todos los clientes
        """
        if not self.clientes:
            return "No hay clientes registrados."

        resultado = f"\n{'='*70}\n"
        resultado += f"CLIENTES REGISTRADOS - {self.nombre_restaurante}\n"
        resultado += f"{'='*70}\n"

        for cliente in self.clientes:
            resultado += f"• {cliente}\n"

        resultado += f"{'='*70}\n"
        return resultado

    def obtener_resumen_estadisticas(self):
        """
        Obtiene un resumen estadístico del restaurante.

        Returns:
            str: resumen de estadísticas
        """
        total_ingresos = sum(c.obtener_monto_total_gastado() for c in self.clientes)
        total_productos = len(self.productos)
        total_clientes = len(self.clientes)

        resultado = f"\n{'='*70}\n"
        resultado += f"ESTADÍSTICAS - {self.nombre_restaurante}\n"
        resultado += f"{'='*70}\n"
        resultado += f"Total de Productos: {total_productos}\n"
        resultado += f"Total de Clientes: {total_clientes}\n"
        resultado += f"Ingresos Totales: ${total_ingresos:.2f}\n"
        resultado += f"{'='*70}\n"
        return resultado

