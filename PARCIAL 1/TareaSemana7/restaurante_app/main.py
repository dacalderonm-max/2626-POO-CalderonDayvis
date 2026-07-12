"""
Módulo principal del sistema de restaurante.
Implementa un menú interactivo que permite registrar, listar y buscar
productos y clientes del restaurante.
"""

from modelos import Producto, Cliente
from servicios import Restaurante


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_encabezado():
    """Muestra el encabezado del sistema."""
    print("\n" + "=" * 50)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 50 + "\n")


def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Ver resumen del restaurante")
    print("8. Salir")
    print("-" * 40)


def registrar_producto_interactivo(restaurante):
    """
    Solicita datos al usuario y registra un nuevo producto.
    Demuestra cómo los datos ingresados se transforman en un objeto Producto
    mediante el constructor.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío")
            return

        categoria = input("Categoría del producto: ").strip()
        if not categoria:
            print("❌ Error: La categoría no puede estar vacía")
            return

        try:
            precio = float(input("Precio del producto: "))
            if precio <= 0:
                print("❌ Error: El precio debe ser mayor que cero")
                return
        except ValueError:
            print("❌ Error: El precio debe ser un número válido")
            return

        disponible_input = input("¿Está disponible? (s/n, default: s): ").lower()
        disponible = disponible_input != 'n'

        # Crear el objeto Producto a partir de los datos ingresados
        producto = Producto(nombre, categoria, precio, disponible)

        # Registrar el producto en el restaurante
        if restaurante.registrar_producto(producto):
            print(f"\n✅ Producto '{nombre}' registrado exitosamente")
        else:
            print("❌ Error al registrar el producto")

    except Exception as e:
        print(f"❌ Error: {e}")


def listar_productos_interactivo(restaurante):
    """
    Lista todos los productos registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- LISTADO DE PRODUCTOS ---")
    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados")
        return

    print(f"\nTotal de productos: {restaurante.contar_productos()}\n")
    for indice, producto in enumerate(productos, 1):
        print(f"{indice}. {producto}")
        print(f"   Información detallada:")
        print(f"   {producto.mostrar_informacion()}\n")


def buscar_producto_interactivo(restaurante):
    """
    Busca productos por nombre.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- BUSCAR PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()

    if not nombre:
        print("❌ Error: Debe ingresar un nombre para buscar")
        return

    resultados = restaurante.buscar_producto(nombre)

    if not resultados:
        print(f"No se encontraron productos con el nombre '{nombre}'")
        return

    print(f"\nResultados encontrados: {len(resultados)}\n")
    for indice, producto in enumerate(resultados, 1):
        print(f"{indice}. {producto}")
        print(f"   {producto.mostrar_informacion()}\n")


def registrar_cliente_interactivo(restaurante):
    """
    Solicita datos al usuario y registra un nuevo cliente.
    Demuestra cómo los datos ingresados se transforman en un objeto Cliente
    mediante el constructor de @dataclass.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    try:
        nombre = input("Nombre del cliente: ").strip()
        correo = input("Correo del cliente: ").strip()
        id_cliente = input("ID del cliente (opcional): ").strip()

        # Crear el objeto Cliente a partir de los datos ingresados
        cliente = Cliente(nombre, correo, id_cliente)

        # Registrar el cliente en el restaurante
        if restaurante.registrar_cliente(cliente):
            print(f"\n✅ Cliente '{nombre}' registrado exitosamente")
        else:
            print("❌ Error al registrar el cliente")

    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")


def listar_clientes_interactivo(restaurante):
    """
    Lista todos los clientes registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- LISTADO DE CLIENTES ---")
    clientes = restaurante.listar_clientes()

    if not clientes:
        print("No hay clientes registrados")
        return

    print(f"\nTotal de clientes: {restaurante.contar_clientes()}\n")
    for indice, cliente in enumerate(clientes, 1):
        print(f"{indice}. {cliente}")
        print(f"   {cliente.mostrar_informacion()}\n")


def buscar_cliente_interactivo(restaurante):
    """
    Busca clientes por nombre.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- BUSCAR CLIENTE ---")
    nombre = input("Ingrese el nombre del cliente a buscar: ").strip()

    if not nombre:
        print("❌ Error: Debe ingresar un nombre para buscar")
        return

    resultados = restaurante.buscar_cliente(nombre)

    if not resultados:
        print(f"No se encontraron clientes con el nombre '{nombre}'")
        return

    print(f"\nResultados encontrados: {len(resultados)}\n")
    for indice, cliente in enumerate(resultados, 1):
        print(f"{indice}. {cliente}")
        print(f"   {cliente.mostrar_informacion()}\n")


def ver_resumen(restaurante):
    """
    Muestra un resumen del estado del restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n--- RESUMEN DEL RESTAURANTE ---")
    print(restaurante.obtener_resumen())


def main():
    """
    Función principal que ejecuta el menú interactivo.
    Mantiene el sistema en ejecución hasta que el usuario selecciona salir.
    """
    # Crear instancia del servicio restaurante
    restaurante = Restaurante("Mi Restaurante")

    while True:
        mostrar_encabezado()
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_producto_interactivo(restaurante)
        elif opcion == '2':
            listar_productos_interactivo(restaurante)
        elif opcion == '3':
            buscar_producto_interactivo(restaurante)
        elif opcion == '4':
            registrar_cliente_interactivo(restaurante)
        elif opcion == '5':
            listar_clientes_interactivo(restaurante)
        elif opcion == '6':
            buscar_cliente_interactivo(restaurante)
        elif opcion == '7':
            ver_resumen(restaurante)
        elif opcion == '8':
            print("\n✅ ¡Gracias por usar el sistema de restaurante!")
            print("Hasta luego...\n")
            break
        else:
            print("❌ Error: Opción no válida. Intente nuevamente.")

        # Pausa para que el usuario vea el resultado
        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()

