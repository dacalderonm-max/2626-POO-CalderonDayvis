"""
Archivo: main.py
Sistema de gestión de mascotas con creación infinita de mascotas y visualización bajo demanda.
"""

from mascota import Mascota


def solicitar_mascota_por_usuario(indice=1):
    print(f"\nCreando mascota #{indice} (ingrese los datos):")
    nombre = input("Nombre: ").strip()
    while not nombre:
        nombre = input("Nombre no puede estar vacío. Nombre: ").strip()

    especie = input("Especie: ").strip()
    while not especie:
        especie = input("Especie no puede estar vacía. Especie: ").strip()

    edad_str = input("Edad (años): ").strip()
    while True:
        try:
            edad = int(edad_str)
            if edad < 0:
                raise ValueError
            break
        except ValueError:
            edad_str = input("Edad inválida. Ingrese un número entero no negativo: ").strip()

    peso_str = input("Peso (kg): ").strip()
    while True:
        try:
            peso = float(peso_str)
            if peso < 0:
                raise ValueError
            break
        except ValueError:
            peso_str = input("Peso inválido. Ingrese un número positivo: ").strip()

    color = input("Color: ").strip()
    while not color:
        color = input("Color no puede estar vacío. Color: ").strip()

    return Mascota(nombre, especie, edad, peso, color)


def mostrar_todas_mascotas(mascotas):
    """Muestra la información de todas las mascotas registradas."""
    if not mascotas:
        print("\n¡No hay mascotas registradas aún!\n")
        return

    print(f"\n===== MASCOTAS REGISTRADAS ({len(mascotas)}) =====")
    for i, m in enumerate(mascotas, 1):
        print(f"\n--- Mascota #{i} ---")
        m.mostrar_informacion()
        m.hacer_sonido()
    print("=" * 40 + "\n")


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n----- MENÚ -----")
    print("1. Registrar nueva mascota")
    print("2. Mostrar todas las mascotas")
    print("3. Salir")
    print("----------------")


def main():
    print("Sistema de gestión de mascotas (Programación Orientada a Objetos)")
    print("Permite registrar infinitas mascotas y visualizarlas bajo demanda.\n")

    mascotas = []
    contador = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            m = solicitar_mascota_por_usuario(contador)
            mascotas.append(m)
            contador += 1
            print(f"\n✓ Mascota registrada exitosamente. Total: {len(mascotas)}\n")

        elif opcion == "2":
            mostrar_todas_mascotas(mascotas)

        elif opcion == "3":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n✗ Opción inválida. Por favor, seleccione 1, 2 o 3.\n")


if __name__ == '__main__':
    main()

