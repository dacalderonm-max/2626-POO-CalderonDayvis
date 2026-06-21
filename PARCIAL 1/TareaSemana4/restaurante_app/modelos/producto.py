"""
Módulo de Producto
Representa los platos, bebidas y productos disponibles en el restaurante.
"""

class Producto:
    """
    Clase que modela un producto del restaurante.
    
    Atributos:
        nombre (str): nombre del producto
        descripcion (str): descripción detallada del producto
        precio (float): precio del producto en dólares
        categoria (str): categoría del producto (plato principal, bebida, postre, etc)
        disponible (bool): indica si el producto está disponible para venta
    """
    
    def __init__(self, nombre, descripcion, precio, categoria, disponible=True):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre: nombre del producto
            descripcion: descripción del producto
            precio: precio en dólares
            categoria: categoría del producto
            disponible: estado de disponibilidad (por defecto True)
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible
    
    def __str__(self):
        """
        Representación en string del producto.
        Retorna una descripción legible del producto.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return (f"[{self.categoria.upper()}] {self.nombre} - ${self.precio:.2f}\n"
                f"    Descripción: {self.descripcion}\n"
                f"    Estado: {estado}")
    
    def cambiar_disponibilidad(self):
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = not self.disponible
    
    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al precio del producto.
        
        Args:
            porcentaje: porcentaje de descuento (ej: 10 para 10%)
        
        Returns:
            float: nuevo precio después del descuento
        """
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        return self.precio

