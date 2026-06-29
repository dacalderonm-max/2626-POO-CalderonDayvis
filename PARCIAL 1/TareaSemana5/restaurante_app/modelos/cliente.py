"""
Modelo de Cliente - Representa a una persona registrada en el sistema del restaurante.
"""


class Cliente:
    """
    Clase que representa un cliente registrado en el restaurante "El Sabor Zapotillano".
    
    Atributos:
        nombre_completo (str): Nombre completo del cliente.
        email (str): Correo electrónico único del cliente.
        numero_telefono (str): Número de teléfono del cliente.
        es_miembro_frecuente (bool): Indica si es cliente frecuente.
        numero_ordenes (int): Cantidad de órdenes realizadas.
    """

    def __init__(
        self,
        nombre_completo: str,
        email: str,
        numero_telefono: str,
        es_miembro_frecuente: bool = False,
    ) -> None:
        """
        Constructor de la clase Cliente.

        Args:
            nombre_completo: Nombre completo del cliente.
            email: Correo electrónico del cliente.
            numero_telefono: Número de teléfono del cliente.
            es_miembro_frecuente: Indica si es miembro frecuente (por defecto, False).
        """
        self.nombre_completo: str = nombre_completo
        self.email: str = email
        self.numero_telefono: str = numero_telefono
        self.es_miembro_frecuente: bool = es_miembro_frecuente
        self.numero_ordenes: int = 0

    def __str__(self) -> str:
        """
        Representación en texto del cliente.

        Returns:
            Cadena con la información formateada del cliente.
        """
        estado_miembro: str = "Sí" if self.es_miembro_frecuente else "No"
        return (
            f"Cliente: {self.nombre_completo}\n"
            f"  Email: {self.email}\n"
            f"  Teléfono: {self.numero_telefono}\n"
            f"  Miembro Frecuente: {estado_miembro}\n"
            f"  Órdenes Realizadas: {self.numero_ordenes}"
        )

    def registrar_orden(self) -> None:
        """
        Incrementa el contador de órdenes del cliente.
        """
        self.numero_ordenes += 1

    def promover_a_miembro_frecuente(self) -> None:
        """
        Promueve al cliente a miembro frecuente si no lo es.
        """
        if not self.es_miembro_frecuente:
            self.es_miembro_frecuente = True

    def obtener_descuento(self) -> float:
        """
        Calcula el descuento aplicable al cliente.

        Returns:
            Porcentaje de descuento (0.0 si no es miembro, 0.10 si es miembro frecuente).
        """
        if self.es_miembro_frecuente:
            return 0.10
        return 0.0

