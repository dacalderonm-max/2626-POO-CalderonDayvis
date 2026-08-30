"""Módulo principal del sistema de restaurante."""

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario


def mostrar_menu_principal() -> None:
    print("\n" + "=" * 60)
    print("  SISTEMA DE RESTAURANTE - SEMANA 11")
    print("=" * 60)
    print("--- REGISTROS ---")
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("--- OPERACIONES ---")
    print("3. Vender producto")
    print("4. Consultar ventas por usuario")
    print("--- CONSULTAS ---")
    print("5. Listar productos")
    print("6. Listar usuarios")
    print("7. Buscar producto")
    print("8. Buscar usuario")
    print("--- ELIMINACIÓN ---")
    print("9. Eliminar producto")
    print("10. Eliminar usuario")
    print("--- PERSISTENCIA ---")
    print("11. Guardar datos en JSON")
    print("12. Cargar datos desde JSON")
    print("13. Limpiar datos en memoria")
    print("14. Salir")
    print("=" * 60)


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría del producto: ").strip()
    try:
        precio = float(input("Precio del producto ($): ").strip())
        stock = int(input("Stock inicial: ").strip())
    except ValueError:
        print("Error: Precio y stock deben ser valores válidos.")
        return

    try:
        producto = Producto(codigo, nombre, categoria, precio, stock)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    exito, mensaje = restaurante.registrar_producto(producto)
    print(mensaje)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = input("Identificación del usuario: ").strip()
    nombre = input("Nombre del usuario: ").strip()
    correo = input("Correo del usuario: ").strip()

    try:
        usuario = Usuario(identificacion, nombre, correo)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    exito, mensaje = restaurante.registrar_usuario(usuario)
    print(mensaje)


def vender_producto(restaurante: Restaurante) -> None:
    print("\n--- Vender Producto ---")
    codigo_producto = input("Código del producto: ").strip()
    identificacion_usuario = input("Identificación del usuario: ").strip()
    try:
        cantidad = int(input("Cantidad a vender: ").strip())
    except ValueError:
        print("Error: La cantidad debe ser un número entero válido.")
        return

    exito, mensaje = restaurante.vender_producto(codigo_producto, identificacion_usuario, cantidad)
    print(mensaje)


def consultar_ventas_usuario(restaurante: Restaurante) -> None:
    print("\n--- Consultar ventas por usuario ---")
    identificacion = input("Identificación del usuario: ").strip()
    for venta in restaurante.listar_ventas_por_usuario(identificacion):
        print(venta)


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Productos registrados ---")
    for producto in restaurante.listar_productos():
        print(producto)
    print(f"\nTotal de productos: {restaurante.obtener_cantidad_productos()}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Usuarios registrados ---")
    for usuario in restaurante.listar_usuarios():
        print(usuario)
    print(f"\nTotal de usuarios: {restaurante.obtener_cantidad_usuarios()}")


def buscar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto a buscar: ").strip()
    exito, producto, mensaje = restaurante.buscar_producto(codigo)
    print(mensaje)


def buscar_usuario(restaurante: Restaurante) -> None:
    identificacion = input("Identificación del usuario a buscar: ").strip()
    exito, usuario, mensaje = restaurante.buscar_usuario(identificacion)
    print(mensaje)


def eliminar_producto(restaurante: Restaurante) -> None:
    codigo = input("Código del producto a eliminar: ").strip()
    exito, mensaje = restaurante.eliminar_producto(codigo)
    print(mensaje)


def eliminar_usuario(restaurante: Restaurante) -> None:
    identificacion = input("Identificación del usuario a eliminar: ").strip()
    exito, mensaje = restaurante.eliminar_usuario(identificacion)
    print(mensaje)


def guardar_datos(restaurante: Restaurante, servicio: ArchivoServicio) -> None:
    print("\n--- Guardar datos en JSON ---")
    ok_productos, mensaje_productos = servicio.guardar_productos(restaurante.obtener_productos())
    ok_usuarios, mensaje_usuarios = servicio.guardar_usuarios(restaurante.obtener_usuarios())
    ok_ventas, mensaje_ventas = servicio.guardar_ventas(restaurante.obtener_ventas())

    print(mensaje_productos)
    print(mensaje_usuarios)
    print(mensaje_ventas)

    if ok_productos and ok_usuarios and ok_ventas:
        print("\n✓ Todos los datos se han guardado exitosamente.")
    else:
        print("\n✗ Ocurrió un error al guardar los datos.")


def cargar_datos(restaurante: Restaurante, servicio: ArchivoServicio) -> None:
    print("\n--- Cargar datos desde JSON ---")
    ok_productos, productos, mensaje_productos = servicio.cargar_productos()
    ok_usuarios, usuarios, mensaje_usuarios = servicio.cargar_usuarios()
    ok_ventas, ventas, mensaje_ventas = servicio.cargar_ventas()

    print(mensaje_productos)
    print(mensaje_usuarios)
    print(mensaje_ventas)

    if ok_productos:
        restaurante.establecer_productos(productos)
    if ok_usuarios:
        restaurante.establecer_usuarios(usuarios)
    if ok_ventas:
        restaurante.ventas = ventas

    if ok_productos and ok_usuarios and ok_ventas:
        print("\n✓ Datos cargados correctamente desde JSON.")
    else:
        print("\n✗ Ocurrió un error al cargar algunos datos.")


def limpiar_datos(restaurante: Restaurante) -> None:
    restaurante.productos.clear()
    restaurante.usuarios.clear()
    restaurante.clientes = restaurante.usuarios
    restaurante.ventas.clear()
    print("\n✓ Datos en memoria eliminados.")


def ejecutar_programa() -> None:
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio()

    print("\n¡Bienvenido al Sistema de Restaurante!")
    cargar_datos(restaurante, archivo_servicio)

    while True:
        mostrar_menu_principal()
        opcion = input("Ingrese su opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_usuario(restaurante)
        elif opcion == "3":
            vender_producto(restaurante)
        elif opcion == "4":
            consultar_ventas_usuario(restaurante)
        elif opcion == "5":
            listar_productos(restaurante)
        elif opcion == "6":
            listar_usuarios(restaurante)
        elif opcion == "7":
            buscar_producto(restaurante)
        elif opcion == "8":
            buscar_usuario(restaurante)
        elif opcion == "9":
            eliminar_producto(restaurante)
        elif opcion == "10":
            eliminar_usuario(restaurante)
        elif opcion == "11":
            guardar_datos(restaurante, archivo_servicio)
        elif opcion == "12":
            cargar_datos(restaurante, archivo_servicio)
        elif opcion == "13":
            limpiar_datos(restaurante)
        elif opcion == "14":
            guardar_datos(restaurante, archivo_servicio)
            print("\n✓ Datos guardados automáticamente. Gracias por usar el sistema de restaurante!")
            break
        else:
            print("Error: Opción no válida. Ingrese un número del 1 al 14.")


if __name__ == "__main__":
    ejecutar_programa()
