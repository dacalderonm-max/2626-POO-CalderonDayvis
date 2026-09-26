"""Servicio principal del restaurante para la capa de negocio."""

from __future__ import annotations

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina la carga de datos y las operaciones del restaurante.

    Contiene las validaciones y reglas de negocio para las ventas,
    evitando que la interfaz manipule directamente los archivos JSON.
    """

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

    # ── Acceso / Login ────────────────────────────────────────

    def validar_acceso(self, usuario: str, password: str) -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        password_limpio = (password or "").strip()

        if not usuario_limpio or not password_limpio:
            return False, "Debe ingresar usuario y contraseña."

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario.lower() == usuario_limpio.lower() and usuario_registrado.password == password_limpio:
                return True, f"Bienvenido, {usuario_registrado.nombre}."

        return False, "Usuario o contraseña incorrectos."

    # ── Productos ─────────────────────────────────────────────

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def obtener_productos_formateados(self) -> list[str]:
        if not self.productos:
            return ["No hay productos registrados."]
        return [producto.mostrar_informacion() for producto in self.productos]

    def buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        """Busca un producto por su código. Retorna None si no existe."""
        for producto in self.productos:
            if producto.codigo.lower() == codigo.strip().lower():
                return producto
        return None

    def consultar_stock(self, codigo: str) -> int | None:
        producto = self.buscar_producto_por_codigo(codigo)
        return producto.stock if producto else None

    # ── Usuarios ──────────────────────────────────────────────

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.usuarios)

    def obtener_usuarios_formateados(self) -> list[str]:
        if not self.usuarios:
            return ["No hay usuarios registrados."]
        return [usuario.mostrar_informacion() for usuario in self.usuarios]

    def buscar_usuario_por_id(self, usuario_id: str) -> Usuario | None:
        """Busca un usuario por su identificador. Retorna None si no existe."""
        for usuario in self.usuarios:
            if usuario.usuario.lower() == usuario_id.strip().lower():
                return usuario
        return None

    # ── Ventas ────────────────────────────────────────────────

    def registrar_venta(self, usuario_id: str, producto_codigo: str, cantidad: int) -> tuple[bool, str]:
        """Valida y registra una venta, persistiéndola en ventas.json.

        Flujo: validación → creación del objeto Venta → persistencia → respuesta.
        """
        # Validar que el usuario exista
        usuario = self.buscar_usuario_por_id(usuario_id)
        if usuario is None:
            return False, f"Error: El usuario '{usuario_id}' no se encuentra registrado."

        # Validar que el producto exista
        producto = self.buscar_producto_por_codigo(producto_codigo)
        if producto is None:
            return False, f"Error: El producto con código '{producto_codigo}' no existe."

        # Validar cantidad
        try:
            cantidad_int = int(cantidad)
        except (TypeError, ValueError):
            return False, "Error: La cantidad debe ser un número entero válido."

        if cantidad_int <= 0:
            return False, "Error: La cantidad debe ser mayor que cero."

        # Validar stock disponible
        if producto.stock < cantidad_int:
            return False, (
                f"Error: Stock insuficiente para '{producto.nombre}'. "
                f"Disponible: {producto.stock}, solicitado: {cantidad_int}."
            )

        # Crear la venta
        venta = Venta(usuario.usuario, producto.codigo, cantidad_int)

        # Descontar stock
        producto.stock -= cantidad_int

        # Agregar a la lista en memoria
        self.ventas.append(venta)

        # Persistir ventas y productos actualizados en archivos JSON
        self.archivo_servicio.guardar_ventas(self.ventas)
        self.archivo_servicio.guardar_productos(self.productos)

        return True, (
            f"Venta registrada: {producto.nombre} (x{cantidad_int}) "
            f"para {usuario.nombre}. Stock actual: {producto.stock}"
        )

    def listar_ventas(self) -> list[Venta]:
        """Retorna una copia de todas las ventas registradas."""
        return list(self.ventas)

    def obtener_ventas_formateadas(self) -> list[str]:
        """Retorna las ventas como cadenas legibles para la interfaz."""
        if not self.ventas:
            return ["No hay ventas registradas."]
        resultado: list[str] = []
        for venta in self.ventas:
            producto = self.buscar_producto_por_codigo(venta.producto_codigo)
            nombre_producto = producto.nombre if producto else "Producto no encontrado"
            usuario = self.buscar_usuario_por_id(venta.usuario_id)
            nombre_usuario = usuario.nombre if usuario else venta.usuario_id
            resultado.append(
                f"{venta.fecha} | {nombre_usuario} | "
                f"{nombre_producto} (x{venta.cantidad})"
            )
        return resultado
