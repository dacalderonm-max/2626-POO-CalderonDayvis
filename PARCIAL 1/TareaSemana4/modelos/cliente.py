"""
Módulo de Modelos - Cliente
Define la clase Cliente que representa un cliente del restaurante.
"""


class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Atributos:
        id_cliente (int): identificador único del cliente
        nombre (str): nombre completo del cliente
        email (str): correo electrónico del cliente
        telefono (str): número de teléfono del cliente
        pedidos_realizados (list): lista de pedidos realizados por el cliente
        monto_total_gastado (float): monto total gastado por el cliente
    """

    def __init__(self, id_cliente, nombre, email, telefono):
        """
        Constructor de la clase Cliente.

        Args:
            id_cliente (int): identificador único
            nombre (str): nombre completo
            email (str): correo electrónico
            telefono (str): número telefónico
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.pedidos_realizados = []
        self.monto_total_gastado = 0.0

    def __str__(self):
        """
        Representación en texto del cliente.

        Returns:
            str: información formateada del cliente
        """
        return f"Cliente: {self.nombre} | Email: {self.email} | Teléfono: {self.telefono} | Monto gastado: ${self.monto_total_gastado:.2f}"

    def obtener_informacion(self):
        """
        Obtiene la información detallada del cliente.

        Returns:
            dict: diccionario con los atributos del cliente
        """
        return {
            "ID": self.id_cliente,
            "Nombre": self.nombre,
            "Email": self.email,
            "Teléfono": self.telefono,
            "Pedidos realizados": len(self.pedidos_realizados),
            "Monto total gastado": f"${self.monto_total_gastado:.2f}"
        }

    def registrar_pedido(self, pedido):
        """
        Registra un nuevo pedido para el cliente.

        Args:
            pedido (dict): información del pedido con monto y descripción
        """
        self.pedidos_realizados.append(pedido)
        self.monto_total_gastado += pedido.get("monto", 0)

    def obtener_pedidos(self):
        """
        Retorna lista de pedidos del cliente.

        Returns:
            list: lista de pedidos realizados
        """
        return self.pedidos_realizados

    def obtener_monto_total_gastado(self):
        """
        Retorna el monto total gastado.

        Returns:
            float: monto total gastado
        """
        return self.monto_total_gastado

    def obtener_nombre(self):
        """
        Retorna el nombre del cliente.

        Returns:
            str: nombre del cliente
        """
        return self.nombre

