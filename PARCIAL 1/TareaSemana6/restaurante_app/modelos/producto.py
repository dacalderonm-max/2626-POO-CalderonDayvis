# =============================================================
# Clase padre: Producto
# Representa un producto general disponible en el restaurante.
# Aplica encapsulación en el atributo __precio.
# =============================================================

class Producto:
    """
    Clase base que define los atributos y comportamientos
    comunes de cualquier producto del restaurante.
    """

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        # Atributo público: nombre del producto
        self.nombre = nombre
        # Atributo encapsulado: el precio no debe ser modificado directamente
        self.__precio = precio
        # Atributo público: indica si el producto está disponible
        self.disponible = disponible

    # ---- Método de acceso (getter) ----
    def obtener_precio(self) -> float:
        """Retorna el precio actual del producto."""
        return self.__precio

    # ---- Método de modificación (setter) con validación ----
    def cambiar_precio(self, nuevo_precio: float) -> None:
        """
        Actualiza el precio del producto.
        Valida que el nuevo precio sea mayor que cero.
        """
        if nuevo_precio <= 0:
            print(f"  [Error] El precio debe ser mayor que cero. Precio no actualizado para '{self.nombre}'.")
        else:
            self.__precio = nuevo_precio
            print(f"  [OK] Precio de '{self.nombre}' actualizado a ${self.__precio:.2f}")

    # ---- Método base para mostrar información ----
    def mostrar_informacion(self) -> None:
        """
        Muestra la información básica del producto.
        Será sobrescrito por las clases hijas (polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"  Producto : {self.nombre}")
        print(f"  Precio   : ${self.__precio:.2f}")
        print(f"  Estado   : {estado}")

