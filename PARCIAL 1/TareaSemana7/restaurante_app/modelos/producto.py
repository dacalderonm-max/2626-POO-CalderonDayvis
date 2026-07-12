"""
Módulo que define la clase Producto con constructor, propiedades y setters.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    Utiliza constructor tradicional __init__, @property y @setter para
    controlar el acceso a los atributos.
    """

    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor tradicional de la clase Producto.

        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            precio (float): Precio del producto
            disponible (bool): Disponibilidad del producto (default: True)

        Raises:
            ValueError: Si los datos no cumplen con las validaciones
        """
        # Validaciones durante la inicialización
        # Validar nombre
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío")

        # Validar categoría
        if not categoria or not categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía")

        # Validar precio
        try:
            precio_float = float(precio)
            if precio_float <= 0:
                raise ValueError("El precio debe ser mayor que cero")
        except (ValueError, TypeError) as e:
            if "mayor que cero" in str(e):
                raise
            raise ValueError(f"Precio inválido: {e}")

        # Asignar valores validados
        self._nombre = nombre.strip()
        self._categoria = categoria.strip()
        self._precio = precio_float
        self._disponible = bool(disponible)

    @property
    def nombre(self):
        """
        Propiedad para acceder al nombre del producto.

        Returns:
            str: Nombre del producto
        """
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Setter para modificar el nombre del producto con validación.

        Args:
            valor (str): Nuevo nombre del producto

        Raises:
            ValueError: Si el nombre está vacío
        """
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def categoria(self):
        """
        Propiedad para acceder a la categoría del producto.

        Returns:
            str: Categoría del producto
        """
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        """
        Setter para modificar la categoría del producto con validación.

        Args:
            valor (str): Nueva categoría del producto

        Raises:
            ValueError: Si la categoría está vacía
        """
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía")
        self._categoria = valor.strip()

    @property
    def precio(self):
        """
        Propiedad para acceder al precio del producto.

        Returns:
            float: Precio del producto
        """
        return self._precio

    @precio.setter
    def precio(self, valor):
        """
        Setter para modificar el precio del producto con validación.

        Args:
            valor (float): Nuevo precio del producto

        Raises:
            ValueError: Si el precio es menor o igual a cero
        """
        try:
            precio_float = float(valor)
            if precio_float <= 0:
                raise ValueError("El precio debe ser mayor que cero")
            self._precio = precio_float
        except ValueError as e:
            raise ValueError(f"Precio inválido: {e}")

    @property
    def disponible(self):
        """
        Propiedad para acceder a la disponibilidad del producto.

        Returns:
            bool: True si el producto está disponible, False en caso contrario
        """
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        """
        Setter para modificar la disponibilidad del producto.

        Args:
            valor (bool): Nueva disponibilidad del producto
        """
        self._disponible = bool(valor)

    def mostrar_informacion(self):
        """
        Método que muestra la información del producto de forma legible.

        Returns:
            str: Información formateada del producto
        """
        estado = "Disponible" if self._disponible else "No disponible"
        return (
            f"Nombre: {self._nombre}\n"
            f"Categoría: {self._categoria}\n"
            f"Precio: ${self._precio:.2f}\n"
            f"Estado: {estado}"
        )

    def __str__(self):
        """Representación en string del producto."""
        return f"{self._nombre} - ${self._precio:.2f} ({self._categoria})"

    def __repr__(self):
        """Representación técnica del producto."""
        return (
            f"Producto(nombre='{self._nombre}', "
            f"categoria='{self._categoria}', "
            f"precio={self._precio}, "
            f"disponible={self._disponible})"
        )

