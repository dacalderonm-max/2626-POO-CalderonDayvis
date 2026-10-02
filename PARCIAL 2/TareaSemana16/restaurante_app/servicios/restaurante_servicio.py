"""Servicio principal del restaurante para la capa de negocio.

Semana 16: incorpora operaciones CRUD de usuarios y sistema de pedidos:
  - Los Clientes crean pedidos con estado 'pendiente'.
  - Administrador y Empleado aprueban o rechazan pedidos.
  - Al aprobar se valida stock, se descuenta y se convierte en Venta.
"""

from __future__ import annotations

from datetime import datetime

from modelos.pedido import Pedido
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina la carga de datos y las operaciones del restaurante.

    Contiene las validaciones y reglas de negocio para las ventas, pedidos y la
    gestión de usuarios, evitando que la interfaz manipule directamente los JSON.
    """

    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []
        self.pedidos: list[Pedido] = []
        self.usuario_activo: str = ""
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self) -> None:
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()
        self.ventas = self.archivo_servicio.cargar_ventas()
        self.pedidos = self.archivo_servicio.cargar_pedidos()

    # ── Acceso / Login ────────────────────────────────────────

    def validar_acceso(self, usuario: str, password: str) -> tuple[bool, str]:
        usuario_limpio = (usuario or "").strip()
        password_limpio = (password or "").strip()

        if not usuario_limpio or not password_limpio:
            return False, "Debe ingresar usuario y contraseña."

        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario.lower() == usuario_limpio.lower()
                and usuario_registrado.password == password_limpio
            ):
                self.usuario_activo = usuario_registrado.usuario
                return True, f"Bienvenido, {usuario_registrado.nombre}."

        return False, "Usuario o contraseña incorrectos."

    def obtener_usuario_activo(self) -> Usuario | None:
        return self.buscar_usuario_por_id(self.usuario_activo)

    def es_administrador_activo(self) -> bool:
        usuario = self.obtener_usuario_activo()
        return usuario is not None and usuario.es_administrador

    def puede_gestionar_ventas(self) -> bool:
        """True si el usuario activo puede registrar ventas (Admin o Empleado)."""
        usuario = self.obtener_usuario_activo()
        return usuario is not None and usuario.rol.lower() in ("administrador", "empleado")

    def es_cliente_activo(self) -> bool:
        """True si el usuario activo tiene rol Cliente."""
        usuario = self.obtener_usuario_activo()
        return usuario is not None and usuario.rol.lower() == "cliente"

    # ── Productos ─────────────────────────────────────────────

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def obtener_productos_formateados(self) -> list[str]:
        if not self.productos:
            return ["No hay productos registrados."]
        return [producto.mostrar_informacion() for producto in self.productos]

    def buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
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
        for usuario in self.usuarios:
            if usuario.usuario.lower() == usuario_id.strip().lower():
                return usuario
        return None

    def registrar_usuario(self, usuario_id: str, password: str, nombre: str, rol: str) -> tuple[bool, str]:
        usuario_id = (usuario_id or "").strip()
        password = (password or "").strip()
        nombre = (nombre or "").strip()
        rol = (rol or "").strip()

        if not usuario_id:
            return False, "El nombre de usuario es obligatorio."
        if not password:
            return False, "La contraseña es obligatoria."
        if not nombre:
            return False, "El nombre completo es obligatorio."
        if not rol:
            return False, "Debe seleccionar un rol."

        if self.buscar_usuario_por_id(usuario_id) is not None:
            return False, f"Ya existe un usuario con el identificador '{usuario_id}'."

        if rol.lower() == "administrador":
            return False, "No se permite registrar un segundo Administrador desde esta sección."

        try:
            nuevo = Usuario(usuario_id, password, nombre, rol)
        except ValueError as e:
            return False, str(e)

        self.usuarios.append(nuevo)
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True, f"Usuario '{usuario_id}' registrado correctamente como {rol}."

    def actualizar_usuario(self, usuario_id: str, nuevo_nombre: str, nueva_password: str, nuevo_rol: str) -> tuple[bool, str]:
        usuario = self.buscar_usuario_por_id(usuario_id)
        if usuario is None:
            return False, f"No se encontró el usuario '{usuario_id}'."

        nuevo_nombre = (nuevo_nombre or "").strip()
        nueva_password = (nueva_password or "").strip()
        nuevo_rol = (nuevo_rol or "").strip()

        if not nuevo_nombre:
            return False, "El nombre completo es obligatorio."
        if not nueva_password:
            return False, "La contraseña es obligatoria."
        if not nuevo_rol:
            return False, "Debe seleccionar un rol."

        if usuario_id.lower() == self.usuario_activo.lower():
            if nuevo_rol.lower() != "administrador":
                return False, "No puede cambiar su propio rol mientras tiene la sesión activa."

        if usuario.es_administrador and nuevo_rol.lower() != "administrador":
            admins = [u for u in self.usuarios if u.es_administrador]
            if len(admins) <= 1:
                return False, "No puede cambiar el rol del único Administrador del sistema."

        usuario.nombre = nuevo_nombre
        usuario.password = nueva_password
        usuario.rol = nuevo_rol
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True, f"Usuario '{usuario_id}' actualizado correctamente."

    def eliminar_usuario(self, usuario_id: str) -> tuple[bool, str]:
        usuario = self.buscar_usuario_por_id(usuario_id)
        if usuario is None:
            return False, f"No se encontró el usuario '{usuario_id}'."

        if usuario_id.lower() == self.usuario_activo.lower():
            return False, "No puede eliminar su propia cuenta mientras tiene la sesión activa."

        if usuario.es_administrador:
            admins = [u for u in self.usuarios if u.es_administrador]
            if len(admins) <= 1:
                return False, "No puede eliminar al único Administrador del sistema."

        self.usuarios = [u for u in self.usuarios if u.usuario.lower() != usuario_id.lower()]
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True, f"Usuario '{usuario_id}' eliminado correctamente."

    # ── Pedidos ───────────────────────────────────────────────

    def crear_pedido(self, cliente_id: str, producto_codigo: str, cantidad: int) -> tuple[bool, str]:
        """Crea un pedido pendiente de aprobación por parte del personal.

        El Cliente llama a este método. El stock NO se descuenta aún.
        """
        cliente = self.buscar_usuario_por_id(cliente_id)
        if cliente is None:
            return False, f"El cliente '{cliente_id}' no está registrado."

        if cliente.rol.lower() != "cliente":
            return False, "Solo los usuarios con rol Cliente pueden hacer pedidos."

        producto = self.buscar_producto_por_codigo(producto_codigo)
        if producto is None:
            return False, f"El producto con código '{producto_codigo}' no existe."

        try:
            cantidad_int = int(cantidad)
        except (TypeError, ValueError):
            return False, "La cantidad debe ser un número entero válido."

        if cantidad_int <= 0:
            return False, "La cantidad debe ser mayor que cero."

        if producto.stock < cantidad_int:
            return False, (
                f"Stock insuficiente para '{producto.nombre}'. "
                f"Disponible: {producto.stock}, solicitado: {cantidad_int}."
            )

        # Generar ID único basado en timestamp con microsegundos
        pedido_id = f"PED-{datetime.now().strftime('%Y%m%d%H%M%S%f')[:18]}-{cliente_id[:3].upper()}"

        nuevo_pedido = Pedido(
            pedido_id=pedido_id,
            cliente_id=cliente.usuario,
            producto_codigo=producto.codigo,
            cantidad=cantidad_int,
        )

        self.pedidos.append(nuevo_pedido)
        self.archivo_servicio.guardar_pedidos(self.pedidos)
        return True, (
            f"Pedido enviado correctamente. ID: {pedido_id}\n"
            f"'{producto.nombre}' x{cantidad_int} — En espera de aprobación."
        )

    def listar_pedidos(self) -> list[Pedido]:
        """Retorna todos los pedidos registrados."""
        return list(self.pedidos)

    def listar_pedidos_pendientes(self) -> list[Pedido]:
        """Retorna solo los pedidos con estado 'pendiente'."""
        return [p for p in self.pedidos if p.es_pendiente]

    def listar_pedidos_de_cliente(self, cliente_id: str) -> list[Pedido]:
        """Retorna todos los pedidos de un cliente específico."""
        return [p for p in self.pedidos if p.cliente_id.lower() == cliente_id.strip().lower()]

    def buscar_pedido_por_id(self, pedido_id: str) -> Pedido | None:
        for pedido in self.pedidos:
            if pedido.pedido_id == pedido_id.strip():
                return pedido
        return None

    def aprobar_pedido(self, pedido_id: str) -> tuple[bool, str]:
        """Aprueba un pedido pendiente, descuenta el stock y genera la Venta.

        Solo Administrador y Empleado pueden aprobar pedidos.
        """
        if not self.puede_gestionar_ventas():
            return False, "Solo el Administrador o Empleado pueden aprobar pedidos."

        pedido = self.buscar_pedido_por_id(pedido_id)
        if pedido is None:
            return False, f"No se encontró el pedido '{pedido_id}'."

        if not pedido.es_pendiente:
            return False, f"El pedido '{pedido_id}' ya fue {pedido.estado}. No se puede modificar."

        producto = self.buscar_producto_por_codigo(pedido.producto_codigo)
        if producto is None:
            return False, f"El producto del pedido ya no existe en el sistema."

        if producto.stock < pedido.cantidad:
            return False, (
                f"Stock insuficiente para aprobar. "
                f"Disponible: {producto.stock}, solicitado: {pedido.cantidad}."
            )

        # Descontar stock y crear la venta
        producto.stock -= pedido.cantidad
        nueva_venta = Venta(pedido.cliente_id, producto.codigo, pedido.cantidad)
        self.ventas.append(nueva_venta)

        # Actualizar estado del pedido
        pedido.estado = "aprobado"
        pedido.fecha_resolucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Persistir cambios
        self.archivo_servicio.guardar_pedidos(self.pedidos)
        self.archivo_servicio.guardar_ventas(self.ventas)
        self.archivo_servicio.guardar_productos(self.productos)

        return True, (
            f"Pedido '{pedido_id}' aprobado. Venta registrada: "
            f"{producto.nombre} x{pedido.cantidad} para {pedido.cliente_id}."
        )

    def rechazar_pedido(self, pedido_id: str) -> tuple[bool, str]:
        """Rechaza un pedido pendiente sin afectar el stock.

        Solo Administrador y Empleado pueden rechazar pedidos.
        """
        if not self.puede_gestionar_ventas():
            return False, "Solo el Administrador o Empleado pueden rechazar pedidos."

        pedido = self.buscar_pedido_por_id(pedido_id)
        if pedido is None:
            return False, f"No se encontró el pedido '{pedido_id}'."

        if not pedido.es_pendiente:
            return False, f"El pedido '{pedido_id}' ya fue {pedido.estado}."

        pedido.estado = "rechazado"
        pedido.fecha_resolucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.archivo_servicio.guardar_pedidos(self.pedidos)
        return True, f"Pedido '{pedido_id}' rechazado correctamente."

    # ── Ventas ────────────────────────────────────────────────

    def registrar_venta(self, usuario_id: str, producto_codigo: str, cantidad: int) -> tuple[bool, str]:
        """Valida y registra una venta directa (para Admin/Empleado).

        Flujo: validación → creación del objeto Venta → persistencia → respuesta.
        """
        usuario = self.buscar_usuario_por_id(usuario_id)
        if usuario is None:
            return False, f"Error: El usuario '{usuario_id}' no se encuentra registrado."

        producto = self.buscar_producto_por_codigo(producto_codigo)
        if producto is None:
            return False, f"Error: El producto con código '{producto_codigo}' no existe."

        try:
            cantidad_int = int(cantidad)
        except (TypeError, ValueError):
            return False, "Error: La cantidad debe ser un número entero válido."

        if cantidad_int <= 0:
            return False, "Error: La cantidad debe ser mayor que cero."

        if producto.stock < cantidad_int:
            return False, (
                f"Error: Stock insuficiente para '{producto.nombre}'. "
                f"Disponible: {producto.stock}, solicitado: {cantidad_int}."
            )

        venta = Venta(usuario.usuario, producto.codigo, cantidad_int)
        producto.stock -= cantidad_int
        self.ventas.append(venta)

        self.archivo_servicio.guardar_ventas(self.ventas)
        self.archivo_servicio.guardar_productos(self.productos)

        return True, (
            f"Venta registrada: {producto.nombre} (x{cantidad_int}) "
            f"para {usuario.nombre}. Stock actual: {producto.stock}"
        )

    def listar_ventas(self) -> list[Venta]:
        return list(self.ventas)

    def obtener_ventas_formateadas(self) -> list[str]:
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
