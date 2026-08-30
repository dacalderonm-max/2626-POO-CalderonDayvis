"""Servicio principal del restaurante."""

from __future__ import annotations

from typing import List

from modelos.cliente import Cliente
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Administra productos, usuarios y ventas del sistema."""

    def __init__(self) -> None:
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []
        self.clientes: List[Cliente] = self.usuarios
        self.ventas: List[Venta] = []

    def registrar_producto(self, producto: Producto) -> tuple[bool, str]:
        if self._codigo_existe(producto.obtener_codigo()):
            return False, f"Error: El código '{producto.obtener_codigo()}' ya existe."
        self.productos.append(producto)
        return True, f"Producto registrado exitosamente: {producto.nombre}"

    def _codigo_existe(self, codigo: str) -> bool:
        return any(producto.obtener_codigo() == codigo for producto in self.productos)

    def listar_productos(self) -> List[str]:
        if not self.productos:
            return ["No hay productos registrados."]
        return [producto.mostrar_informacion() for producto in self.productos]

    def obtener_cantidad_productos(self) -> int:
        return len(self.productos)

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def establecer_productos(self, productos: List[Producto]) -> None:
        self.productos = productos

    def buscar_producto(self, codigo: str) -> tuple[bool, Producto | None, str]:
        for producto in self.productos:
            if producto.obtener_codigo() == codigo:
                return True, producto, f"Producto encontrado: {producto.mostrar_informacion()}"
        return False, None, f"Error: Producto con código '{codigo}' no encontrado."

    def eliminar_producto(self, codigo: str) -> tuple[bool, str]:
        for i, producto in enumerate(self.productos):
            if producto.obtener_codigo() == codigo:
                nombre = producto.nombre
                self.productos.pop(i)
                return True, f"Producto '{nombre}' eliminado exitosamente."
        return False, f"Error: Producto con código '{codigo}' no encontrado."

    def registrar_usuario(self, usuario: Usuario) -> tuple[bool, str]:
        if self._identificacion_existe(usuario.obtener_identificacion()):
            return False, f"Error: La identificación '{usuario.obtener_identificacion()}' ya existe."
        self.usuarios.append(usuario)
        self.clientes = self.usuarios
        return True, f"Usuario registrado exitosamente: {usuario.nombre}"

    def registrar_cliente(self, cliente: Cliente) -> tuple[bool, str]:
        return self.registrar_usuario(cliente)

    def _identificacion_existe(self, identificacion: str) -> bool:
        return any(usuario.obtener_identificacion() == identificacion for usuario in self.usuarios)

    def listar_usuarios(self) -> List[str]:
        if not self.usuarios:
            return ["No hay usuarios registrados."]
        return [usuario.mostrar_informacion() for usuario in self.usuarios]

    def listar_clientes(self) -> List[str]:
        return self.listar_usuarios()

    def obtener_cantidad_usuarios(self) -> int:
        return len(self.usuarios)

    def obtener_cantidad_clientes(self) -> int:
        return self.obtener_cantidad_usuarios()

    def obtener_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def obtener_clientes(self) -> List[Cliente]:
        return self.clientes

    def establecer_usuarios(self, usuarios: List[Usuario]) -> None:
        self.usuarios = usuarios
        self.clientes = self.usuarios

    def establecer_clientes(self, clientes: List[Cliente]) -> None:
        self.clientes = clientes
        self.usuarios = self.clientes

    def buscar_usuario(self, identificacion: str) -> tuple[bool, Usuario | None, str]:
        for usuario in self.usuarios:
            if usuario.obtener_identificacion() == identificacion:
                return True, usuario, f"Usuario encontrado: {usuario.mostrar_informacion()}"
        return False, None, f"Error: Usuario con identificación '{identificacion}' no encontrado."

    def buscar_cliente(self, identificacion: str) -> tuple[bool, Cliente | None, str]:
        encontrado, usuario, mensaje = self.buscar_usuario(identificacion)
        if not encontrado or usuario is None:
            return False, None, mensaje
        return True, usuario, mensaje

    def eliminar_usuario(self, identificacion: str) -> tuple[bool, str]:
        for i, usuario in enumerate(self.usuarios):
            if usuario.obtener_identificacion() == identificacion:
                nombre = usuario.nombre
                self.usuarios.pop(i)
                self.clientes = self.usuarios
                return True, f"Usuario '{nombre}' eliminado exitosamente."
        return False, f"Error: Usuario con identificación '{identificacion}' no encontrado."

    def eliminar_cliente(self, identificacion: str) -> tuple[bool, str]:
        return self.eliminar_usuario(identificacion)

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> tuple[bool, str]:
        usuario = next((u for u in self.usuarios if u.obtener_identificacion() == identificacion_usuario), None)
        producto = next((p for p in self.productos if p.obtener_codigo() == codigo_producto), None)

        if usuario is None:
            return False, f"Error: Usuario con identificación '{identificacion_usuario}' no encontrado."
        if producto is None:
            return False, f"Error: Producto con código '{codigo_producto}' no encontrado."

        try:
            cantidad_entera = int(cantidad)
        except (TypeError, ValueError):
            return False, "Error: La cantidad debe ser un número entero válido."

        if cantidad_entera <= 0:
            return False, "Error: La cantidad vendida debe ser mayor que cero."
        if producto.stock < cantidad_entera:
            return False, "Error: Stock insuficiente para completar la venta."

        venta = Venta(usuario.identificacion, producto.codigo, cantidad_entera)
        self.ventas.append(venta)
        producto.vender(cantidad_entera)
        return True, (
            f"Venta registrada correctamente: {producto.nombre} (x{cantidad_entera}) "
            f"para {usuario.nombre}. Stock actual: {producto.stock}"
        )

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        return [venta for venta in self.ventas if venta.usuario_id == identificacion_usuario]

    def listar_ventas_por_usuario(self, identificacion_usuario: str) -> List[str]:
        ventas = self.consultar_ventas_por_usuario(identificacion_usuario)
        if not ventas:
            return [f"No hay ventas registradas para el usuario '{identificacion_usuario}'."]
        resultado: List[str] = []
        for venta in ventas:
            producto = next((p for p in self.productos if p.obtener_codigo() == venta.producto_codigo), None)
            nombre_producto = producto.nombre if producto is not None else "Producto no encontrado"
            resultado.append(
                f"Usuario: {venta.usuario_id} | Producto: {venta.producto_codigo} | "
                f"Nombre: {nombre_producto} | Cantidad: {venta.cantidad}"
            )
        return resultado

    def obtener_ventas(self) -> List[Venta]:
        return self.ventas

    def obtener_cantidad_ventas(self) -> int:
        return len(self.ventas)
