"""Módulo de la clase Producto."""


class Producto:
    """Representa un producto del restaurante con stock disponible."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        if not codigo or not codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not categoria or not categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        if precio < 0:
            raise ValueError("El precio del producto no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock del producto no puede ser negativo.")

        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = float(precio)
        self.stock: int = int(stock)

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def obtener_codigo(self) -> str:
        return self.codigo

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        if self.stock < cantidad:
            raise ValueError("No hay stock suficiente para completar la venta.")
        self.stock -= int(cantidad)

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
            "tipo": "Producto",
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        if "codigo" not in datos:
            raise KeyError("Falta la clave 'codigo' en el producto.")
        if "nombre" not in datos:
            raise KeyError("Falta la clave 'nombre' en el producto.")
        if "categoria" not in datos:
            raise KeyError("Falta la clave 'categoria' en el producto.")
        if "precio" not in datos:
            raise KeyError("Falta la clave 'precio' en el producto.")

        stock = datos.get("stock", 0)
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            stock,
        )
