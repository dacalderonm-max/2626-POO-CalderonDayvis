"""
Módulo de Cliente
Representa a los clientes del restaurante.
"""

class Cliente:
    """
    Clase que modela un cliente del restaurante.

    Atributos:
        nombre (str): nombre completo del cliente
        email (str): correo electrónico del cliente
        telefono (str): número de teléfono del cliente
        direccion (str): dirección de domicilio del cliente
        activo (bool): indica si el cliente está activo en el sistema
    """

    def __init__(self, nombre, email, telefono, direccion, activo=True):
        """
        Constructor de la clase Cliente.

        Args:
            nombre: nombre completo del cliente
            email: correo electrónico del cliente
            telefono: número de teléfono del cliente
            direccion: dirección de domicilio del cliente
            activo: estado del cliente (por defecto True)
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.activo = activo
        self.historial_pedidos = []  # lista para almacenar historial de pedidos

    def __str__(self):
        """
        Representación en string del cliente.
        Retorna una descripción legible del cliente.
        """
        estado = "Activo" if self.activo else "Inactivo"
        return (f"Cliente: {self.nombre}\n"
                f"    Email: {self.email}\n"
                f"    Teléfono: {self.telefono}\n"
                f"    Dirección: {self.direccion}\n"
                f"    Estado: {estado}\n"
                f"    Pedidos realizados: {len(self.historial_pedidos)}")

    def cambiar_estado(self):
        """Cambia el estado del cliente entre activo e inactivo."""
        self.activo = not self.activo

    def registrar_pedido(self, id_pedido, monto_total):
        """
        Registra un nuevo pedido en el historial del cliente.

        Args:
            id_pedido: identificador del pedido
            monto_total: monto total del pedido
        """
        self.historial_pedidos.append({
            'id_pedido': id_pedido,
            'monto_total': monto_total
        })

    def obtener_total_gastado(self):
        """
        Calcula el total gastado por el cliente.

        Returns:
            float: monto total gastado en todos los pedidos
        """
        return sum(pedido['monto_total'] for pedido in self.historial_pedidos)

