"""
Módulo de Modelos - Producto
Define la clase Producto que representa un artículo disponible en el restaurante.
"""


class Producto:
    """
    Clase que representa un producto (plato, bebida o artículo) del restaurante.

    Atributos:
        id_producto (int): identificador único del producto
        nombre (str): nombre del producto
        descripcion (str): descripción breve del producto
        precio (float): precio del producto
        cantidad_disponible (int): cantidad de unidades disponibles en el inventario
    """

    def __init__(self, id_producto, nombre, descripcion, precio, cantidad_disponible):
        """
        Constructor de la clase Producto.

        Args:
            id_producto (int): identificador único
            nombre (str): nombre del producto
            descripcion (str): descripción del producto
            precio (float): precio unitario
            cantidad_disponible (int): cantidad disponible en inventario
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        """
        Representación en texto del producto.

        Returns:
            str: información formateada del producto
        """
        return f"Producto: {self.nombre} | Descripción: {self.descripcion} | Precio: ${self.precio:.2f} | Disponibles: {self.cantidad_disponible}"

    def obtener_informacion(self):
        """
        Obtiene la información detallada del producto.

        Returns:
            dict: diccionario con los atributos del producto
        """
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Descripción": self.descripcion,
            "Precio": f"${self.precio:.2f}",
            "Disponibles": self.cantidad_disponible
        }

    def actualizar_disponibilidad(self, cantidad):
        """
        Actualiza la cantidad disponible del producto.

        Args:
            cantidad (int): cantidad a restar del inventario (positivo para restar, negativo para sumar)
        """
        if self.cantidad_disponible + cantidad >= 0:
            self.cantidad_disponible += cantidad
        else:
            print(f"Error: No hay suficiente inventario de {self.nombre}")

    def obtener_precio(self):
        """
        Retorna el precio del producto.

        Returns:
            float: precio del producto
        """
        return self.precio

