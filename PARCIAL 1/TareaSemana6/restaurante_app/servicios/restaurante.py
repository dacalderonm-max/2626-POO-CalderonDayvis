# =============================================================
# Clase de servicio: Restaurante
# Administra la lista de productos registrados en el sistema.
# =============================================================

from modelos.producto import Producto


class Restaurante:
    """
    Clase de servicio que almacena y gestiona los productos
    del restaurante (platillos y bebidas).
    """

    def __init__(self, nombre_restaurante: str):
        # Nombre del restaurante
        self.nombre_restaurante = nombre_restaurante
        # Lista interna que almacena todos los productos registrados
        self.__productos = []

    # ---- Agregar un producto a la lista ----
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto (Platillo o Bebida) a la lista del restaurante."""
        self.__productos.append(producto)
        print(f"  [+] '{producto.nombre}' agregado correctamente.")

    # ---- Mostrar todos los productos registrados ----
    def mostrar_menu(self) -> None:
        """
        Recorre la lista de productos y ejecuta mostrar_informacion()
        en cada objeto. Aquí se evidencia el polimorfismo, ya que
        el método se comporta distinto según el tipo de producto.
        """
        print("=" * 55)
        print(f"   MENÚ DEL RESTAURANTE: {self.nombre_restaurante.upper()}")
        print("=" * 55)

        if not self.__productos:
            print("  No hay productos registrados aún.")
            return

        for indice, producto in enumerate(self.__productos, start=1):
            print(f"\n  #{indice}")
            # Polimorfismo: se llama al método de la clase hija correspondiente
            producto.mostrar_informacion()
            print("  " + "-" * 50)

    # ---- Obtener la cantidad de productos registrados ----
    def total_productos(self) -> int:
        """Retorna el número total de productos en la lista."""
        return len(self.__productos)

