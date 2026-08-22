"""
Módulo principal del sistema de restaurante con persistencia en JSON.
Proporciona la interfaz interactiva de consola para el usuario.

Principio de Responsabilidad Única:
Este módulo únicamente se encarga de:
- Mostrar el menú
- Solicitar datos del usuario
- Crear objetos basados en los datos
- Llamar a métodos del servicio Restaurante
- Mostrar resultados
- Manejar persistencia de datos en JSON

No administra directamente las listas ni contiene lógica de validación compleja.
"""

from servicios.restaurante import Restaurante
from servicios.gestor_datos import GestorDatos
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu_principal() -> None:
    """Muestra el menú principal del sistema en consola."""
    print("\n" + "=" * 50)
    print("  SISTEMA DE RESTAURANTE CON PERSISTENCIA JSON")
    print("=" * 50)
    print("--- REGISTROS ---")
    print("1. Registrar producto")
    print("2. Registrar cliente")
    print("-" * 50)
    print("--- CONSULTAS ---")
    print("3. Listar productos")
    print("4. Listar clientes")
    print("5. Buscar producto")
    print("6. Buscar cliente")
    print("-" * 50)
    print("--- ELIMINACIÓN ---")
    print("7. Eliminar producto")
    print("8. Eliminar cliente")
    print("-" * 50)
    print("--- PERSISTENCIA ---")
    print("9. Guardar datos en JSON")
    print("10. Cargar datos desde JSON")
    print("11. Limpiar datos en memoria")
    print("-" * 50)
    print("12. Salir")
    print("=" * 50)


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

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Productos Registrados en Memoria ---")

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
    print("\n--- Clientes Registrados en Memoria ---")

    clientes: list = restaurante.listar_clientes()

    for cliente_info in clientes:
        print(cliente_info)

    print(f"\nTotal de clientes: {restaurante.obtener_cantidad_clientes()}")


def guardar_datos(restaurante: Restaurante, gestor: GestorDatos) -> None:
    """
    Guarda los datos de productos y clientes en archivos JSON.

    Args:
        restaurante: Instancia del servicio Restaurante
        gestor: Instancia del gestor de datos
    """
    print("\n--- Guardar Datos en JSON ---")

    # Guardar productos
    exito_productos, mensaje_productos = gestor.guardar_productos(
        restaurante.obtener_productos()
    )
    print(mensaje_productos)

    # Guardar clientes
    exito_clientes, mensaje_clientes = gestor.guardar_clientes(
        restaurante.obtener_clientes()
    )
    print(mensaje_clientes)

    if exito_productos and exito_clientes:
        print("\n✓ Todos los datos se han guardado exitosamente en JSON")
    else:
        print("\n✗ Ocurrió un error al guardar los datos")


def cargar_datos(restaurante: Restaurante, gestor: GestorDatos) -> None:
    """
    Carga los datos de productos y clientes desde archivos JSON.

    Args:
        restaurante: Instancia del servicio Restaurante
        gestor: Instancia del gestor de datos
    """
    print("\n--- Cargar Datos desde JSON ---")

    # Cargar productos
    exito_productos, productos, mensaje_productos = gestor.cargar_productos()
    print(mensaje_productos)
    if exito_productos:
        restaurante.establecer_productos(productos)

    # Cargar clientes
    exito_clientes, clientes, mensaje_clientes = gestor.cargar_clientes()
    print(mensaje_clientes)
    if exito_clientes:
        restaurante.establecer_clientes(clientes)

    if exito_productos and exito_clientes:
        print("\n✓ Todos los datos se han cargado exitosamente desde JSON")
    else:
        print("\n✗ Ocurrió un error al cargar los datos")


def limpiar_datos(restaurante: Restaurante) -> None:
    """
    Limpia los datos en memoria (productos y clientes).
    Nota: No afecta los archivos JSON guardados.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Limpiar Datos en Memoria ---")
    confirmacion = input("¿Desea limpiar todos los datos en memoria? (s/n): ").strip().lower()

    if confirmacion == 's':
        restaurante.establecer_productos([])
        restaurante.establecer_clientes([])
        print("✓ Datos en memoria limpios exitosamente")
        print("Nota: Los datos guardados en JSON no han sido eliminados")
    else:
        print("Operación cancelada")


def buscar_producto(restaurante: Restaurante) -> None:
    """
    Busca un producto por su código.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Buscar Producto ---")
    codigo: str = input("Código del producto a buscar: ").strip()

    if not codigo:
        print("Error: El código no puede estar vacío.")
        return

    exito, producto, mensaje = restaurante.buscar_producto(codigo)
    print(mensaje)


def buscar_cliente(restaurante: Restaurante) -> None:
    """
    Busca un cliente por su identificación.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Buscar Cliente ---")
    identificacion: str = input("Identificación del cliente a buscar: ").strip()

    if not identificacion:
        print("Error: La identificación no puede estar vacía.")
        return

    exito, cliente, mensaje = restaurante.buscar_cliente(identificacion)
    print(mensaje)


def eliminar_producto(restaurante: Restaurante) -> None:
    """
    Elimina un producto por su código.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Eliminar Producto ---")
    codigo: str = input("Código del producto a eliminar: ").strip()

    if not codigo:
        print("Error: El código no puede estar vacío.")
        return

    confirmacion = input(f"¿Desea eliminar el producto con código '{codigo}'? (s/n): ").strip().lower()
    if confirmacion == 's':
        exito, mensaje = restaurante.eliminar_producto(codigo)
        print(mensaje)
    else:
        print("Operación cancelada")


def eliminar_cliente(restaurante: Restaurante) -> None:
    """
    Elimina un cliente por su identificación.

    Args:
        restaurante: Instancia del servicio Restaurante
    """
    print("\n--- Eliminar Cliente ---")
    identificacion: str = input("Identificación del cliente a eliminar: ").strip()

    if not identificacion:
        print("Error: La identificación no puede estar vacía.")
        return

    confirmacion = input(f"¿Desea eliminar el cliente con identificación '{identificacion}'? (s/n): ").strip().lower()
    if confirmacion == 's':
        exito, mensaje = restaurante.eliminar_cliente(identificacion)
        print(mensaje)
    else:
        print("Operación cancelada")


def ejecutar_programa() -> None:
    """
    Ejecuta el programa principal con el menú interactivo.
    Mantiene el programa en ejecución hasta que el usuario elige salir.
    """
    restaurante: Restaurante = Restaurante()
    gestor: GestorDatos = GestorDatos()

    print("\n¡Bienvenido al Sistema de Restaurante!")
    print("Los datos se guardarán automáticamente en archivos JSON en la carpeta 'datos/'")

    # Cargar automáticamente los datos guardados al iniciar el programa
    cargar_datos(restaurante, gestor)

    while True:
        mostrar_menu_principal()

        opcion: str = input("Ingrese su opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_cliente(restaurante)
        elif opcion == "3":
            listar_productos(restaurante)
        elif opcion == "4":
            listar_clientes(restaurante)
        elif opcion == "5":
            buscar_producto(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            eliminar_producto(restaurante)
        elif opcion == "8":
            eliminar_cliente(restaurante)
        elif opcion == "9":
            guardar_datos(restaurante, gestor)
        elif opcion == "10":
            cargar_datos(restaurante, gestor)
        elif opcion == "11":
            limpiar_datos(restaurante)
        elif opcion == "12":
            # Guardar automáticamente los datos al salir (sin preguntar)
            guardar_datos(restaurante, gestor)
            print("\n✓ Datos guardados automáticamente. Gracias por usar el sistema de restaurante!")
            break
        else:
            print("Error: Opción no válida. Ingrese un número del 1 al 12.")


if __name__ == "__main__":
    ejecutar_programa()



