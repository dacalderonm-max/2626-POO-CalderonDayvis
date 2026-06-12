"""
Archivo: mascota.py
Definición de la clase Mascota.
"""

class Mascota:
    """Clase que representa una mascota con nombre, especie, edad, peso y color."""

    def __init__(self, nombre: str, especie: str, edad: int, peso: float, color: str):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.color = color

    def mostrar_informacion(self):
        """Muestra la información de la mascota de forma organizada."""
        print('\n----- Información de la mascota -----')
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")
        print(f"Peso   : {self.peso} kg")
        print(f"Color  : {self.color}")
        print('------------------------------------\n')

    def hacer_sonido(self):
        """Devuelve (y muestra) un sonido representativo según la especie.

        Se simplifica a algunos casos comunes y un sonido por defecto.
        """
        especie_lower = self.especie.strip().lower()
        if 'perro' in especie_lower:
            sonido = '¡Guau!'  # español
        elif 'gato' in especie_lower:
            sonido = '¡Miau!'
        elif 'paj' in especie_lower or 'ave' in especie_lower or 'pájaro' in especie_lower:
            sonido = '¡Pío!'
        else:
            sonido = '¡...'  # sonido genérico

        # También imprimimos el sonido para que se vea al ejecutar
        print(f"{self.nombre} hace: {sonido}")
        return sonido

