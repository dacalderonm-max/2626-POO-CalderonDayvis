# =============================================================
# Clase hija: Bebida
# Hereda de Producto y añade atributos propios de una bebida.
# =============================================================

from modelos.producto import Producto


class Bebida(Producto):
    """
    Representa una bebida disponible en el restaurante.
    Hereda los atributos comunes de Producto y agrega:
      - volumen_ml  : volumen en mililitros
      - tipo_bebida : categoría (Refresco, Jugo, Agua, Café, etc.)
      - es_alcoholica: indica si contiene alcohol
    """

    def __init__(self, nombre: str, precio: float,
                 volumen_ml: int, tipo_bebida: str,
                 es_alcoholica: bool = False, disponible: bool = True):
        # Reutiliza el constructor de la clase padre mediante super()
        super().__init__(nombre, precio, disponible)
        # Atributos específicos de la bebida
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida
        self.es_alcoholica = es_alcoholica

    # ---- Sobrescritura de mostrar_informacion() (polimorfismo) ----
    def mostrar_informacion(self) -> None:
        """
        Muestra la información completa de la bebida,
        incluyendo los datos propios de esta clase.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        alcoholica = "Sí" if self.es_alcoholica else "No"
        print(f"  [BEBIDA] {self.nombre}")
        print(f"  Tipo          : {self.tipo_bebida}")
        print(f"  Precio        : ${self.obtener_precio():.2f}")
        print(f"  Volumen       : {self.volumen_ml} ml")
        print(f"  Con alcohol   : {alcoholica}")
        print(f"  Estado        : {estado}")

