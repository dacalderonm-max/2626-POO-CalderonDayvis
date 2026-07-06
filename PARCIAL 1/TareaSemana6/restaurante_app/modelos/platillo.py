# =============================================================
# Clase hija: Platillo
# Hereda de Producto y añade atributos propios de un plato.
# =============================================================

from modelos.producto import Producto


class Platillo(Producto):
    """
    Representa un plato de comida del restaurante.
    Hereda los atributos comunes de Producto y agrega:
      - calorias      : valor calórico del platillo
      - tipo_platillo : categoría (Entrada, Plato fuerte, Postre, etc.)
      - tiempo_prep   : tiempo estimado de preparación en minutos
    """

    def __init__(self, nombre: str, precio: float,
                 calorias: int, tipo_platillo: str,
                 tiempo_prep: int, disponible: bool = True):
        # Reutiliza el constructor de la clase padre mediante super()
        super().__init__(nombre, precio, disponible)
        # Atributos específicos del platillo
        self.calorias = calorias
        self.tipo_platillo = tipo_platillo
        self.tiempo_prep = tiempo_prep

    # ---- Sobrescritura de mostrar_informacion() (polimorfismo) ----
    def mostrar_informacion(self) -> None:
        """
        Muestra la información completa del platillo,
        incluyendo los datos propios de esta clase.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"  [PLATILLO] {self.nombre}")
        print(f"  Tipo          : {self.tipo_platillo}")
        print(f"  Precio        : ${self.obtener_precio():.2f}")
        print(f"  Calorías      : {self.calorias} kcal")
        print(f"  Tiempo prep.  : {self.tiempo_prep} min")
        print(f"  Estado        : {estado}")

