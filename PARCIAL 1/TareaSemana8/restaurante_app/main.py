"""
Módulo principal del sistema de restaurante.
Proporciona la interfaz interactiva de consola para el usuario.

Principio de Responsabilidad Única:
Este módulo únicamente se encarga de:
- Mostrar el menú
- Solicitar datos del usuario
- Crear objetos basados en los datos
- Llamar a métodos del servicio Restaurante
- Mostrar resultados

No administra directamente las listas ni contiene lógica de validación compleja.
"""

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema en consola."""
    print("\n" + "=" * 40)
    print("    SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")
    print("=" * 40)


def registrar_producto(restaurante: Restaurante) -> None:
    """
    Solicita información para registrar un producto y lo agrega al restaurante.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Registrar Producto ---")

    codigo: str = input("Código del producto: ").strip()
    if not codigo:
        print("Error: El código no puede estar vacío.")
        return

    nombre: str = input("Nombre del producto: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    categoria: str = input("Categoría del producto: ").strip()
    if not categoria:
        print("Error: La categoría no puede estar vacía.")
        return

    try:
        precio: float = float(input("Precio del producto ($): "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
            return
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return

    # Crear el objeto Producto
    producto: Producto = Producto(codigo, nombre, categoria, precio)

    # Registrar en el restaurante
    exito: bool
    mensaje: str
    exito, mensaje = restaurante.registrar_producto(producto)

    print(mensaje)


def registrar_bebida(restaurante: Restaurante) -> None:
    """
    Solicita información para registrar una bebida y la agrega al restaurante.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Registrar Bebida ---")

    codigo: str = input("Código de la bebida: ").strip()
    if not codigo:
        print("Error: El código no puede estar vacío.")
        return

    nombre: str = input("Nombre de la bebida: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    categoria: str = input("Categoría de la bebida: ").strip()
    if not categoria:
        print("Error: La categoría no puede estar vacía.")
        return

    try:
        precio: float = float(input("Precio de la bebida ($): "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
            return
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return

    tamaño: str = input("Tamaño (pequeño/mediano/grande): ").strip()
    if not tamaño:
        print("Error: El tamaño no puede estar vacío.")
        return

    tipo_envase: str = input("Tipo de envase (vaso/botella/lata): ").strip()
    if not tipo_envase:
        print("Error: El tipo de envase no puede estar vacío.")
        return

    # Crear el objeto Bebida
    bebida: Bebida = Bebida(codigo, nombre, categoria, precio, tamaño, tipo_envase)

    # Registrar en el restaurante
    exito: bool
    mensaje: str
    exito, mensaje = restaurante.registrar_producto(bebida)

    print(mensaje)


def registrar_cliente(restaurante: Restaurante) -> None:
    """
    Solicita información para registrar un cliente y lo agrega al restaurante.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Registrar Cliente ---")

    identificacion: str = input("Identificación del cliente: ").strip()
    if not identificacion:
        print("Error: La identificación no puede estar vacía.")
        return

    nombre: str = input("Nombre del cliente: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    correo: str = input("Correo del cliente: ").strip()
    if not correo:
        print("Error: El correo no puede estar vacío.")
        return

    # Crear el objeto Cliente
    cliente: Cliente = Cliente(identificacion, nombre, correo)

    # Registrar en el restaurante
    exito: bool
    mensaje: str
    exito, mensaje = restaurante.registrar_cliente(cliente)

    print(mensaje)


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos registrados en el restaurante.

    Demuestra el polimorfismo: Producto y Bebida usan el mismo método mostrar_informacion().

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Productos Registrados ---")

    productos: list = restaurante.listar_productos()

    for producto_info in productos:
        print(producto_info)

    print(f"\nTotal de productos: {restaurante.obtener_cantidad_productos()}")


def listar_clientes(restaurante: Restaurante) -> None:
    """
    Lista todos los clientes registrados en el restaurante.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Clientes Registrados ---")

    clientes: list = restaurante.listar_clientes()

    for cliente_info in clientes:
        print(cliente_info)

    print(f"\nTotal de clientes: {restaurante.obtener_cantidad_clientes()}")


def ejecutar_programa() -> None:
    """
    Ejecuta el programa principal con el menú interactivo.
    Mantiene el programa en ejecución hasta que el usuario elige salir.
    """
    restaurante: Restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion: str = input("Ingrese su opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema de restaurante!")
            break
        else:
            print("Error: Opción no válida. Ingrese un número del 1 al 6.")


if __name__ == "__main__":
    ejecutar_programa()

