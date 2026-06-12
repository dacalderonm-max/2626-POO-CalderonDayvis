"""
Programa 1: Programación Tradicional
Archivo: tradicional.py

Sistema de registro de mascotas que permite crear infinitas mascotas
y mostrarlas solo cuando se solicita.

No se utilizan clases ni objetos: sólo funciones y estructuras básicas.
"""

def solicitar_datos():
    """Pide al usuario los datos de una mascota y los devuelve como diccionario."""
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
            edad_str = input("Edad inválida. Ingrese un número entero no negativo para la edad: ").strip()

    peso_str = input("Peso (kg): ").strip()
    while True:
        try:
            peso = float(peso_str)
            if peso < 0:
                raise ValueError
            break
        except ValueError:
            peso_str = input("Peso inválido. Ingrese un número positivo para el peso: ").strip()

    color = input("Color: ").strip()
    while not color:
        color = input("Color no puede estar vacío. Color: ").strip()

    return {"nombre": nombre, "especie": especie, "edad": edad, "peso": peso, "color": color}


def mostrar_informacion(mascota):
    """Recibe un diccionario con la información de la mascota y la muestra formateada."""
    print('\n----- Información de la mascota -----')
    print(f"Nombre : {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad   : {mascota['edad']} años")
    print(f"Peso   : {mascota['peso']} kg")
    print(f"Color  : {mascota['color']}")
    print('------------------------------------\n')


def mostrar_todas_mascotas(mascotas):
    """Muestra la información de todas las mascotas registradas."""
    if not mascotas:
        print("\n¡No hay mascotas registradas aún!\n")
        return

    print(f"\n===== MASCOTAS REGISTRADAS ({len(mascotas)}) =====")
    for i, m in enumerate(mascotas, 1):
        print(f"\n--- Mascota #{i} ---")
        mostrar_informacion(m)
    print("=" * 40 + "\n")


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n----- MENÚ -----")
    print("1. Registrar nueva mascota")
    print("2. Mostrar todas las mascotas")
    print("3. Salir")
    print("----------------")


def main():
    print("Sistema de registro de mascotas (Programación tradicional)")
    print("Permite registrar infinitas mascotas y visualizarlas bajo demanda.\n")

    mascotas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            print(f"\nCreando mascota #{len(mascotas) + 1} (ingrese los datos):")
            m = solicitar_datos()
            mascotas.append(m)
            print(f"✓ Mascota registrada exitosamente. Total: {len(mascotas)}\n")

        elif opcion == "2":
            mostrar_todas_mascotas(mascotas)

        elif opcion == "3":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n✗ Opción inválida. Por favor, seleccione 1, 2 o 3.\n")


if __name__ == '__main__':
    main()

