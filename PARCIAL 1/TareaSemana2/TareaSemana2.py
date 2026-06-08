class Automovil:
	def __init__(self, marca, modelo, anio, color, velocidad=0):
		self.marca = marca
		self.modelo = modelo
		self.anio = anio
		self.color = color
		self.velocidad = velocidad

	def acelerar(self, incremento=10):
		"""Aumenta la velocidad en `incremento` km/h."""
		self.velocidad += incremento
		print(f"{self.marca} {self.modelo} acelera +{incremento} km/h -> {self.velocidad} km/h")

	def frenar(self, decremento=10):
		"""Reduce la velocidad en `decremento` km/h (no baja de 0)."""
		self.velocidad = max(0, self.velocidad - decremento)
		print(f"{self.marca} {self.modelo} frena -{decremento} km/h -> {self.velocidad} km/h")

	def info(self):
		"""Devuelve una cadena con la información del automóvil."""
		return f"{self.marca} {self.modelo} ({self.anio}) - {self.color} - Velocidad: {self.velocidad} km/h"


def main():
	# Crear al menos dos objetos diferentes
	car1 = Automovil("Toyota", "Corolla", 2020, "Blanco")
	car2 = Automovil("Ford", "Mustang", 1967, "Rojo", velocidad=20)

	print("Información inicial:")
	print(car1.info())
	print(car2.info())

	print("\nAcciones:")
	car1.acelerar(30)
	car1.frenar(15)

	car2.acelerar()
	car2.frenar(50)

	print("\nInformación final:")
	print(car1.info())
	print(car2.info())


if __name__ == "__main__":
	main()

