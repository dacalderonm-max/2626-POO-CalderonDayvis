"""Servicio principal del restaurante para la capa de negocio."""

from __future__ import annotations

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina la carga de datos y las operaciones del restaurante."""

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self) -> None:
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()
        self.ventas = self.archivo_servicio.cargar_ventas()

    def _guardar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(self.productos)

    def _guardar_usuarios(self) -> None:
        self.archivo_servicio.guardar_usuarios(self.usuarios)

    def _guardar_ventas(self) -> None:
        self.archivo_servicio.guardar_ventas(self.ventas)

    def validar_acceso(self, usuario: str, password: str) -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        password_limpia = (password or "").strip()

        if not usuario_limpio or not password_limpia:
            return False, "Debe ingresar usuario y contraseña."

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario_limpio.lower() and usuario_registrado.password == password_limpia:
                return True, f"Bienvenido, {usuario_registrado.nombre}."

        return False, "Usuario o contraseña incorrectos."

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.usuarios)

    def listar_ventas(self) -> list[Venta]:
        return list(self.ventas)

    def consultar_usuario(self, usuario: str) -> Usuario | None:
        usuario_limpio = (usuario or "").strip()
        if not usuario_limpio:
            return None

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario_limpio.lower():
                return usuario_registrado
        return None

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        identificacion_limpia = (identificacion_usuario or "").strip()
        if not identificacion_limpia:
            return []
        return [venta for venta in self.ventas if venta.usuario_id.lower() == identificacion_limpia.lower()]

    def registrar_usuario(self, usuario: str, password: str, nombre: str, rol: str = "usuario") -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        password_limpia = (password or "").strip()
        nombre_limpio = (nombre or "").strip()
        rol_limpio = (rol or "").strip() or "usuario"

        if not usuario_limpio or not password_limpia or not nombre_limpio:
            return False, "Usuario, contraseña y nombre son obligatorios."
        if self.consultar_usuario(usuario_limpio) is not None:
            return False, f"El usuario '{usuario_limpio}' ya existe."

        usuario_obj = Usuario(usuario_limpio, password_limpia, nombre_limpio, rol_limpio)
        self.usuarios.append(usuario_obj)
        self._guardar_usuarios()
        return True, f"Usuario '{usuario_obj.usuario}' registrado correctamente."

    def actualizar_usuario(
        self,
        usuario: str,
        password: str | None = None,
        nombre: str | None = None,
        rol: str | None = None,
    ) -> tuple[bool, str]:
        usuario_actual = self.consultar_usuario(usuario)
        if usuario_actual is None:
            return False, f"El usuario '{usuario}' no existe."

        password_nueva = (password if password is not None else usuario_actual.password).strip()
        nombre_nuevo = (nombre if nombre is not None else usuario_actual.nombre).strip()
        rol_nuevo = (rol if rol is not None else usuario_actual.rol).strip() or "usuario"

        if not password_nueva or not nombre_nuevo:
            return False, "Contraseña y nombre son obligatorios."

        usuario_actual.password = password_nueva
        usuario_actual.nombre = nombre_nuevo
        usuario_actual.rol = rol_nuevo
        self._guardar_usuarios()
        return True, f"Usuario '{usuario_actual.usuario}' actualizado correctamente."

    def eliminar_usuario(self, usuario: str) -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        usuario_actual = self.consultar_usuario(usuario_limpio)
        if usuario_actual is None:
            return False, f"El usuario '{usuario_limpio}' no existe."

        self.usuarios = [item for item in self.usuarios if item.usuario.lower() != usuario_limpio.lower()]
        self._guardar_usuarios()
        return True, f"Usuario '{usuario_actual.usuario}' eliminado correctamente."

    def consultar_stock(self, codigo: str) -> int | None:
        producto = self.consultar_producto(codigo)
        if producto is None:
            return None
        return producto.stock

    def consultar_producto(self, codigo: str) -> Producto | None:
        codigo_limpio = (codigo or "").strip()
        if not codigo_limpio:
            return None

        for producto in self.productos:
            if producto.codigo.lower() == codigo_limpio.lower():
                return producto
        return None

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float | str,
        stock: int | str,
    ) -> tuple[bool, str]:
        codigo_limpio = (codigo or "").strip()
        nombre_limpio = (nombre or "").strip()
        categoria_limpia = (categoria or "").strip()

        if not codigo_limpio or not nombre_limpio or not categoria_limpia:
            return False, "Código, nombre y categoría son obligatorios."

        try:
            precio_valido = float(precio)
        except (TypeError, ValueError):
            return False, "El precio debe ser un número válido."

        try:
            stock_valido = int(stock)
        except (TypeError, ValueError):
            return False, "El stock debe ser un número entero válido."

        if precio_valido < 0:
            return False, "El precio no puede ser negativo."
        if stock_valido < 0:
            return False, "El stock no puede ser negativo."
        if self.consultar_producto(codigo_limpio) is not None:
            return False, f"El código '{codigo_limpio}' ya existe."

        producto = Producto(codigo_limpio, nombre_limpio, categoria_limpia, precio_valido, stock_valido)
        self.productos.append(producto)
        self._guardar_productos()
        return True, f"Producto '{producto.nombre}' registrado correctamente."

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | str | None = None,
        stock: int | str | None = None,
    ) -> tuple[bool, str]:
        producto = self.consultar_producto(codigo)
        if producto is None:
            return False, f"El código '{codigo}' no existe."

        nombre_nuevo = (nombre or producto.nombre).strip()
        categoria_nueva = (categoria or producto.categoria).strip()

        try:
            precio_nuevo = float(precio) if precio is not None else producto.precio
        except (TypeError, ValueError):
            return False, "El precio debe ser un número válido."

        try:
            stock_nuevo = int(stock) if stock is not None else producto.stock
        except (TypeError, ValueError):
            return False, "El stock debe ser un número entero válido."

        if not nombre_nuevo or not categoria_nueva:
            return False, "Nombre y categoría son obligatorios."
        if precio_nuevo < 0:
            return False, "El precio no puede ser negativo."
        if stock_nuevo < 0:
            return False, "El stock no puede ser negativo."

        producto.nombre = nombre_nuevo
        producto.categoria = categoria_nueva
        producto.precio = float(precio_nuevo)
        producto.stock = int(stock_nuevo)
        self._guardar_productos()
        return True, f"Producto '{producto.codigo}' actualizado correctamente."

    def eliminar_producto(self, codigo: str) -> tuple[bool, str]:
        codigo_limpio = (codigo or "").strip()
        producto = self.consultar_producto(codigo_limpio)
        if producto is None:
            return False, f"El código '{codigo_limpio}' no existe."

        nombre = producto.nombre
        self.productos = [item for item in self.productos if item.codigo.lower() != codigo_limpio.lower()]
        self._guardar_productos()
        return True, f"Producto '{nombre}' eliminado correctamente."

    def vender_producto(self, usuario: str, producto: str, cantidad: int | str) -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        producto_limpio = (producto or "").strip()

        usuario_obj = self.consultar_usuario(usuario_limpio)
        if usuario_obj is None:
            return False, f"El usuario '{usuario_limpio}' no existe."

        producto_obj = self.consultar_producto(producto_limpio)
        if producto_obj is None:
            return False, f"El producto '{producto_limpio}' no existe."

        try:
            cantidad_entera = int(cantidad)
        except (TypeError, ValueError):
            return False, "La cantidad debe ser un número entero válido."

        if cantidad_entera <= 0:
            return False, "La cantidad vendida debe ser mayor que cero."
        if producto_obj.stock < cantidad_entera:
            return False, "Stock insuficiente para completar la venta."

        venta = Venta(usuario_obj.usuario, producto_obj.codigo, cantidad_entera)
        self.ventas.append(venta)
        producto_obj.vender(cantidad_entera)
        self._guardar_productos()
        self._guardar_ventas()
        return True, (
            f"Venta registrada correctamente: {producto_obj.nombre} (x{cantidad_entera}) "
            f"para {usuario_obj.nombre}. Stock actual: {producto_obj.stock}"
        )

    def registrar_venta(self, usuario: str, producto: str, cantidad: int | str) -> tuple[bool, str]:
        return self.vender_producto(usuario, producto, cantidad)

    def obtener_ventas_formateadas(self) -> list[str]:
        if not self.ventas:
            return ["No hay ventas registradas."]
        return [venta.mostrar_informacion() for venta in self.ventas]

    def listar_ventas_por_usuario(self, identificacion_usuario: str) -> list[str]:
        ventas = self.consultar_ventas_por_usuario(identificacion_usuario)
        if not ventas:
            return [f"No hay ventas registradas para el usuario '{identificacion_usuario}'."]
        return [venta.mostrar_informacion() for venta in ventas]

    def obtener_productos_formateados(self) -> list[str]:
        if not self.productos:
            return ["No hay productos registrados."]
        return [producto.mostrar_informacion() for producto in self.productos]

    def obtener_usuarios_formateados(self) -> list[str]:
        if not self.usuarios:
            return ["No hay usuarios registrados."]
        return [usuario.mostrar_informacion() for usuario in self.usuarios]

    def obtener_cantidad_ventas(self) -> int:
        return len(self.ventas)
