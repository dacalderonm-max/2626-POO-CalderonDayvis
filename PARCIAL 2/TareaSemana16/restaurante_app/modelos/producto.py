"""Modelo del producto del restaurante."""


class Producto:
    """Representa un producto disponible en el menú."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> None:
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

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.stock = int(stock)

    def mostrar_informacion(self) -> str:
        return (
            f"{self.codigo} | {self.nombre} | {self.categoria} | "
            f"${self.precio:.2f} | Stock: {self.stock}"
        )

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        return cls(
            codigo=str(datos["codigo"]),
            nombre=str(datos["nombre"]),
            categoria=str(datos["categoria"]),
            precio=float(datos["precio"]),
            stock=int(datos.get("stock", 0)),
        )
