"""
Módulo de Servicios - Restaurante
Contiene la clase principal de gestión del restaurante.
"""

from modelos import Producto, Cliente


class Restaurante:
    """
    Clase que gestiona las operaciones principales del restaurante.

    Atributos:
        nombre (str): nombre del restaurante
        ubicacion (str): ubicación del restaurante
        productos (list): lista de productos registrados
        clientes (list): lista de clientes registrados
        contador_pedidos (int): contador para generar IDs de pedidos
    """

    def __init__(self, nombre, ubicacion):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre: nombre del restaurante
            ubicacion: ubicación del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []
        self.clientes = []
        self.contador_pedidos = 0

    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.

        Args:
            producto: objeto de tipo Producto a registrar

        Returns:
            bool: True si se registró exitosamente, False si ya existe
        """
        # Verificar que el producto no esté duplicado
        if any(p.nombre.lower() == producto.nombre.lower() for p in self.productos):
            return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.

        Args:
            cliente: objeto de tipo Cliente a registrar

        Returns:
            bool: True si se registró exitosamente, False si ya existe
        """
        # Verificar que el cliente no esté duplicado por email
        if any(c.email.lower() == cliente.email.lower() for c in self.clientes):
            return False

        self.clientes.append(cliente)
        return True

    def obtener_producto_por_nombre(self, nombre):
        """
        Busca un producto por nombre.

        Args:
            nombre: nombre del producto a buscar

        Returns:
            Producto: objeto del producto si existe, None en caso contrario
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def obtener_cliente_por_email(self, email):
        """
        Busca un cliente por email.

        Args:
            email: email del cliente a buscar

        Returns:
            Cliente: objeto del cliente si existe, None en caso contrario
        """
        for cliente in self.clientes:
            if cliente.email.lower() == email.lower():
                return cliente
        return None

    def listar_productos(self):
        """
        Retorna una lista de todos los productos disponibles.

        Returns:
            str: representación de los productos disponibles
        """
        if not self.productos:
            return "No hay productos registrados."

        resultado = "=" * 60 + "\n"
        resultado += f"MENÚ DEL RESTAURANTE - {self.nombre}\n"
        resultado += "=" * 60 + "\n\n"

        categorias = {}
        for producto in self.productos:
            if producto.disponible:
                if producto.categoria not in categorias:
                    categorias[producto.categoria] = []
                categorias[producto.categoria].append(producto)

        for categoria, productos_cat in sorted(categorias.items()):
            resultado += f"\n{categoria.upper()}\n"
            resultado += "-" * 40 + "\n"
            for prod in productos_cat:
                resultado += f"{prod.nombre}: ${prod.precio:.2f}\n"
                resultado += f"  → {prod.descripcion}\n\n"

        return resultado

    def listar_clientes(self):
        """
        Retorna una lista de todos los clientes registrados.

        Returns:
            str: representación de los clientes registrados
        """
        if not self.clientes:
            return "No hay clientes registrados."

        resultado = "=" * 60 + "\n"
        resultado += "CLIENTES REGISTRADOS\n"
        resultado += "=" * 60 + "\n\n"

        for cliente in self.clientes:
            resultado += str(cliente) + "\n" + "-" * 60 + "\n"

        return resultado

    def crear_pedido(self, cliente, productos_pedido):
        """
        Crea un nuevo pedido para un cliente.

        Args:
            cliente: objeto Cliente que realiza el pedido
            productos_pedido: lista de tuplas (nombre_producto, cantidad)

        Returns:
            dict: información del pedido si fue exitoso, None en caso contrario
        """
        if not cliente.activo:
            return None

        self.contador_pedidos += 1
        id_pedido = f"PED-{self.contador_pedidos:04d}"

        items_pedido = []
        monto_total = 0

        for nombre_prod, cantidad in productos_pedido:
            producto = self.obtener_producto_por_nombre(nombre_prod)
            if producto is None or not producto.disponible:
                return None

            subtotal = producto.precio * cantidad
            items_pedido.append({
                'producto': nombre_prod,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
            monto_total += subtotal

        # Registrar el pedido en el cliente
        cliente.registrar_pedido(id_pedido, monto_total)

        pedido = {
            'id': id_pedido,
            'cliente': cliente.nombre,
            'items': items_pedido,
            'monto_total': monto_total
        }

        return pedido

    def __str__(self):
        """
        Representación en string del restaurante.
        Retorna información general del restaurante.
        """
        return (f"Restaurante: {self.nombre}\n"
                f"Ubicación: {self.ubicacion}\n"
                f"Productos registrados: {len(self.productos)}\n"
                f"Clientes registrados: {len(self.clientes)}")

