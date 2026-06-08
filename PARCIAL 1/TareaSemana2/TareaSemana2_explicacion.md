# Explicación detallada de `TareaSemana2.py`

Este documento explica paso a paso el código en `TareaSemana2.py`. Está pensado para alguien que está empezando con la Programación Orientada a Objetos (POO).

## Resumen general

El programa define una clase `Automovil` que modela un automóvil con atributos (marca, modelo, año, color, velocidad) y métodos (acelerar, frenar, info). Luego crea dos instancias (objetos) de esa clase y demuestra su uso en la función `main()`.

---

## Explicación línea por línea y conceptos de POO

- `class Automovil:`
  - Define una nueva clase llamada `Automovil`.
  - En POO, una clase es una plantilla o molde que describe cómo son y qué hacen los objetos (instancias) de ese tipo.

- `def __init__(self, marca, modelo, anio, color, velocidad=0):`
  - `__init__` es el método constructor: se ejecuta cuando creas (instancias) un objeto de la clase.
  - `self` es una referencia al propio objeto; con `self` accedes a los atributos y métodos del objeto.
  - Los otros parámetros (`marca`, `modelo`, `anio`, `color`, `velocidad`) se usan para inicializar el estado del objeto.
  - `velocidad=0` indica un valor por defecto: si no das velocidad al crear el objeto, será 0.

- Dentro de `__init__`:
  - `self.marca = marca`, `self.modelo = modelo`, `self.anio = anio`, `self.color = color`, `self.velocidad = velocidad`
  - Aquí se crean los atributos del objeto y se les asigna el valor recibido. Los atributos representan el estado del objeto.

- `def acelerar(self, incremento=10):`
  - Método que representa un comportamiento del objeto: aumentar su velocidad.
  - `incremento=10` es un valor por defecto: si no pasas cuánto acelerar, aumentará 10 km/h.
  - Dentro del método `self.velocidad += incremento` modifica el estado del objeto (atributo `velocidad`).
  - `print(f"{self.marca} {self.modelo} acelera +{incremento} km/h -> {self.velocidad} km/h")` muestra un mensaje formateado usando f-strings.

- `def frenar(self, decremento=10):`
  - Método para disminuir la velocidad.
  - `self.velocidad = max(0, self.velocidad - decremento)` evita que la velocidad sea negativa: `max` devuelve el mayor de los dos valores.
  - De nuevo imprime el resultado con un f-string.

- `def info(self):`
  - Método que devuelve una cadena con información legible sobre el automóvil.
  - No recibe más parámetros además de `self` y no modifica el estado; solo lo lee y devuelve texto.

---

## La función `main()` y la ejecución del programa

- `def main():` define una función que agrupa el flujo principal del programa.

- `car1 = Automovil("Toyota", "Corolla", 2020, "Blanco")`
  - Esto crea (instancia) un objeto `car1` usando la clase `Automovil` y llama a `__init__` con los parámetros indicados.

- `car2 = Automovil("Ford", "Mustang", 1967, "Rojo", velocidad=20)` crea otro objeto y le asigna una velocidad inicial de 20.

- `print(car1.info())` y `print(car2.info())` muestran la información inicial de ambos objetos usando el método `info()`.

- Llamadas a métodos que cambian el estado:
  - `car1.acelerar(30)` aumenta la velocidad de `car1` en 30.
  - `car1.frenar(15)` reduce la velocidad de `car1` en 15.
  - `car2.acelerar()` usa el valor por defecto (10).
  - `car2.frenar(50)` intenta frenar 50; gracias a `max(0, ...)` la velocidad no quedará negativa.

- Finalmente se imprimen las `info()` para mostrar el estado final.

- `if __name__ == "__main__":`
  - Esta línea comprueba si el archivo se está ejecutando directamente (no importado desde otro módulo). Si es así, llama a `main()`.

---

## Conceptos de POO ilustrados en el código

- Encapsulación: Los atributos (`marca`, `modelo`, `anio`, `color`, `velocidad`) y métodos (`acelerar`, `frenar`, `info`) están agrupados dentro de la clase `Automovil`.
- Estado vs comportamiento: Los atributos representan el estado del objeto; los métodos representan comportamientos que leen o modifican ese estado.
- Instancias: `car1` y `car2` son instancias independientes; cambiar `car1` no afecta a `car2`.
- Reutilización: La clase define la lógica una sola vez; puedes crear muchos automóviles reutilizando esa definición.

---

## Detalles de Python usados aquí (para principiantes)

- `f"{self.marca} {self.modelo} ..."` (f-strings): forma moderna y legible de incluir variables dentro de cadenas.
- Valores por defecto en funciones: `incremento=10` permite llamar `acelerar()` sin argumentos.
- `max(0, ...)` es una forma simple de evitar valores negativos.
- La convención `if __name__ == "__main__":` permite que el archivo pueda importarse sin ejecutar `main()` automáticamente.

---

## Pequeños ejercicios sugeridos para practicar

1. Crea un tercer automóvil con otros valores y prueba métodos distintos.
2. Añade un método `pintar(nuevo_color)` que cambie el color del coche.
3. Añade validación en `__init__` para asegurar que `anio` sea un número razonable.
4. Implementa un método `reproducir_musica(cancion)` que imprima que la canción se está reproduciendo.

---

Si quieres, puedo:
- Abrir el archivo y comentar el código línea por línea dentro del propio `TareaSemana2.py`.
- Añadir los ejercicios anteriores como funciones o pruebas automáticas.
- Explicar con diagramas UML cómo se relacionan clases y objetos.

Dime cuál de estas opciones prefieres y lo hago a continuación.
