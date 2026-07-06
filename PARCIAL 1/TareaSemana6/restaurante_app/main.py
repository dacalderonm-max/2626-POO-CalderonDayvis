# =============================================================
# main.py — Punto de arranque del programa
# Sistema de restaurante con herencia, encapsulación y
# polimorfismo aplicados en Python modular.
# Semana 6 - Programación Orientada a Objetos
# Autor: Calderón Dayvis
# =============================================================

import sys
import os

# Permite que Python encuentre los módulos desde la carpeta restaurante_app
sys.path.insert(0, os.path.dirname(__file__))

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    print("\n" + "=" * 55)
    print("   SISTEMA DE RESTAURANTE — POO SEMANA 6")
    print("=" * 55)

    # ---- Crear el servicio principal del restaurante ----
    restaurante = Restaurante("El Buen Sabor")

    # ---- Crear objetos de tipo Platillo ----
    # Platillo 1: Seco de pollo
    seco_pollo = Platillo(
        nombre="Seco de Pollo",
        precio=6.50,
        calorias=520,
        tipo_platillo="Plato fuerte",
        tiempo_prep=20
    )

    # Platillo 2: Ensalada César
    ensalada_cesar = Platillo(
        nombre="Ensalada César",
        precio=4.25,
        calorias=310,
        tipo_platillo="Entrada",
        tiempo_prep=10
    )

    # ---- Crear objetos de tipo Bebida ----
    # Bebida 1: Jugo de naranja
    jugo_naranja = Bebida(
        nombre="Jugo de Naranja",
        precio=2.00,
        volumen_ml=350,
        tipo_bebida="Jugo natural",
        es_alcoholica=False
    )

    # Bebida 2: Agua mineral
    agua_mineral = Bebida(
        nombre="Agua Mineral",
        precio=1.25,
        volumen_ml=500,
        tipo_bebida="Agua",
        es_alcoholica=False
    )

    # ---- Agregar los productos al restaurante ----
    print("\n  Registrando productos en el sistema...")
    restaurante.agregar_producto(seco_pollo)
    restaurante.agregar_producto(ensalada_cesar)
    restaurante.agregar_producto(jugo_naranja)
    restaurante.agregar_producto(agua_mineral)
    print(f"\n  Total de productos registrados: {restaurante.total_productos()}")

    # ---- Demostrar encapsulación y validación de precio ----
    print("\n" + "=" * 55)
    print("   DEMOSTRACIÓN DE ENCAPSULACIÓN")
    print("=" * 55)
    print(f"\n  Precio actual de '{seco_pollo.nombre}': ${seco_pollo.obtener_precio():.2f}")
    print("\n  Intentando cambiar el precio a $0.00 (inválido):")
    seco_pollo.cambiar_precio(0.00)
    print("\n  Intentando cambiar el precio a -3.00 (inválido):")
    seco_pollo.cambiar_precio(-3.00)
    print("\n  Actualizando el precio a $7.00 (válido):")
    seco_pollo.cambiar_precio(7.00)

    # ---- Mostrar el menú completo (demuestra polimorfismo) ----
    print()
    restaurante.mostrar_menu()

    print(f"\n  Programa finalizado correctamente.\n")


if __name__ == "__main__":
    main()

