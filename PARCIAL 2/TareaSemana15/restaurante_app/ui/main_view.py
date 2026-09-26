"""Vista principal de la aplicación con secciones Productos, Usuarios y Ventas."""

from __future__ import annotations

import os
import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image, ImageTk


class MainView:
    """Panel principal con navegación por pestañas: Productos, Usuarios y Ventas.

    La sección de Ventas implementa el flujo de manejo de eventos:
    USUARIO → BOTÓN (command=) → CALLBACK → RestauranteServicio → PERSISTENCIA → RESPUESTA VISUAL
    """

    # ── Paleta de colores ─────────────────────────────────────
    BG_PRINCIPAL = "#0f172a"
    BG_PANEL = "#1e293b"
    BG_CARD = "#334155"
    FG_TITULO = "#f8fafc"
    FG_SUBTITULO = "#94a3b8"
    FG_TEXTO = "#cbd5e1"
    ACCENT = "#f59e0b"
    ACCENT_HOVER = "#fbbf24"
    SUCCESS = "#22c55e"
    ERROR = "#ef4444"
    BTN_BG = "#3b82f6"
    BTN_FG = "#ffffff"

    def __init__(self, parent: tk.Misc, controller: object, restaurante_servicio: object) -> None:
        self.parent = parent
        self.controller = controller
        self.servicio = restaurante_servicio

        # ── Cargar íconos desde assets/ ───────────────────────
        self.iconos: dict[str, ImageTk.PhotoImage] = {}
        self._cargar_iconos()

        # ── Frame contenedor principal ────────────────────────
        self.frame = tk.Frame(parent, bg=self.BG_PRINCIPAL)

        # ── Barra superior con logo y título ──────────────────
        self._crear_barra_superior()

        # ── Barra de navegación ───────────────────────────────
        self._crear_barra_navegacion()

        # ── Contenedor de contenido (paneles intercambiables) ─
        self.contenido_frame = tk.Frame(self.frame, bg=self.BG_PRINCIPAL)
        self.contenido_frame.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        # ── Paneles de cada sección ───────────────────────────
        self.panel_productos = self._crear_panel_productos()
        self.panel_usuarios = self._crear_panel_usuarios()
        self.panel_ventas = self._crear_panel_ventas()

        # Panel activo al inicio
        self._panel_activo: tk.Frame | None = None
        self.mostrar_seccion_productos()

    # ══════════════════════════════════════════════════════════
    #  CARGA DE ASSETS
    # ══════════════════════════════════════════════════════════

    def _cargar_iconos(self) -> None:
        """Carga los íconos PNG desde la carpeta assets/."""
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        archivos = {
            "logo": ("logo_restaurante.png", (48, 48)),
            "productos": ("icono_productos.png", (20, 20)),
            "usuarios": ("icono_usuarios.png", (20, 20)),
            "ventas": ("icono_ventas.png", (20, 20)),
            "logout": ("icono_logout.png", (20, 20)),
            "registrar": ("icono_registrar.png", (20, 20)),
        }
        for clave, (nombre_archivo, tamano) in archivos.items():
            ruta = os.path.join(assets_dir, nombre_archivo)
            if os.path.exists(ruta):
                try:
                    img = Image.open(ruta).resize(tamano, Image.LANCZOS)
                    self.iconos[clave] = ImageTk.PhotoImage(img)
                except Exception:
                    pass

    # ══════════════════════════════════════════════════════════
    #  BARRA SUPERIOR
    # ══════════════════════════════════════════════════════════

    def _crear_barra_superior(self) -> None:
        barra = tk.Frame(self.frame, bg=self.BG_PANEL, pady=10, padx=16)
        barra.pack(fill="x")

        # Logo
        if "logo" in self.iconos:
            logo_label = tk.Label(barra, image=self.iconos["logo"], bg=self.BG_PANEL)
            logo_label.pack(side="left", padx=(0, 12))

        tk.Label(
            barra,
            text="Restaurante App",
            font=("Segoe UI", 20, "bold"),
            bg=self.BG_PANEL,
            fg=self.ACCENT,
        ).pack(side="left")

        tk.Label(
            barra,
            text="— Semana 15",
            font=("Segoe UI", 12),
            bg=self.BG_PANEL,
            fg=self.FG_SUBTITULO,
        ).pack(side="left", padx=(8, 0))

        # Botón cerrar sesión
        btn_logout = tk.Button(
            barra,
            text="  Cerrar sesión",
            font=("Segoe UI", 10, "bold"),
            bg=self.ERROR,
            fg=self.BTN_FG,
            activebackground="#dc2626",
            activeforeground=self.BTN_FG,
            bd=0,
            padx=14,
            pady=6,
            cursor="hand2",
            command=self.controller.cerrar_sesion,
        )
        if "logout" in self.iconos:
            btn_logout.config(image=self.iconos["logout"], compound="left")
        btn_logout.pack(side="right")

    # ══════════════════════════════════════════════════════════
    #  BARRA DE NAVEGACIÓN
    # ══════════════════════════════════════════════════════════

    def _crear_barra_navegacion(self) -> None:
        nav = tk.Frame(self.frame, bg=self.BG_PRINCIPAL, pady=8, padx=16)
        nav.pack(fill="x")

        self.nav_buttons: dict[str, tk.Button] = {}

        secciones = [
            ("productos", "  Productos", self.mostrar_seccion_productos),
            ("usuarios", "  Usuarios", self.mostrar_seccion_usuarios),
            ("ventas", "  Ventas", self.mostrar_seccion_ventas),
        ]

        for clave, texto, comando in secciones:
            btn = tk.Button(
                nav,
                text=texto,
                font=("Segoe UI", 11, "bold"),
                bg=self.BG_CARD,
                fg=self.FG_TEXTO,
                activebackground=self.ACCENT,
                activeforeground=self.BG_PRINCIPAL,
                bd=0,
                padx=20,
                pady=8,
                cursor="hand2",
                command=comando,
            )
            if clave in self.iconos:
                btn.config(image=self.iconos[clave], compound="left")
            btn.pack(side="left", padx=(0, 6))
            self.nav_buttons[clave] = btn

    def _resaltar_boton_nav(self, clave_activa: str) -> None:
        """Resalta visualmente el botón de la sección activa."""
        for clave, btn in self.nav_buttons.items():
            if clave == clave_activa:
                btn.config(bg=self.ACCENT, fg=self.BG_PRINCIPAL)
            else:
                btn.config(bg=self.BG_CARD, fg=self.FG_TEXTO)

    # ══════════════════════════════════════════════════════════
    #  PANEL DE PRODUCTOS
    # ══════════════════════════════════════════════════════════

    def _crear_panel_productos(self) -> tk.Frame:
        panel = tk.Frame(self.contenido_frame, bg=self.BG_PANEL)

        tk.Label(
            panel, text="📦  Productos del menú", font=("Segoe UI", 15, "bold"),
            bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w",
        ).pack(fill="x", padx=16, pady=(16, 8))

        # Treeview de productos
        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tree_productos = ttk.Treeview(panel, columns=columnas, show="headings", height=14)
        for col, titulo, ancho in [
            ("codigo", "Código", 80), ("nombre", "Nombre", 180),
            ("categoria", "Categoría", 140), ("precio", "Precio ($)", 100),
            ("stock", "Stock", 80),
        ]:
            self.tree_productos.heading(col, text=titulo)
            self.tree_productos.column(col, width=ancho, anchor="center")

        scroll_prod = ttk.Scrollbar(panel, orient="vertical", command=self.tree_productos.yview)
        self.tree_productos.configure(yscrollcommand=scroll_prod.set)
        self.tree_productos.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        scroll_prod.pack(side="right", fill="y")

        return panel

    def _cargar_tabla_productos(self) -> None:
        """Llena el Treeview de productos con datos del servicio."""
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        for producto in self.servicio.listar_productos():
            self.tree_productos.insert("", "end", values=(
                producto.codigo, producto.nombre, producto.categoria,
                f"${producto.precio:.2f}", producto.stock,
            ))

    # ══════════════════════════════════════════════════════════
    #  PANEL DE USUARIOS
    # ══════════════════════════════════════════════════════════

    def _crear_panel_usuarios(self) -> tk.Frame:
        panel = tk.Frame(self.contenido_frame, bg=self.BG_PANEL)

        tk.Label(
            panel, text="👤  Usuarios registrados", font=("Segoe UI", 15, "bold"),
            bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w",
        ).pack(fill="x", padx=16, pady=(16, 8))

        columnas = ("usuario", "nombre", "rol")
        self.tree_usuarios = ttk.Treeview(panel, columns=columnas, show="headings", height=14)
        for col, titulo, ancho in [
            ("usuario", "Usuario", 140), ("nombre", "Nombre", 240),
            ("rol", "Rol", 140),
        ]:
            self.tree_usuarios.heading(col, text=titulo)
            self.tree_usuarios.column(col, width=ancho, anchor="center")

        scroll_usr = ttk.Scrollbar(panel, orient="vertical", command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscrollcommand=scroll_usr.set)
        self.tree_usuarios.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        scroll_usr.pack(side="right", fill="y")

        return panel

    def _cargar_tabla_usuarios(self) -> None:
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        for usuario in self.servicio.listar_usuarios():
            self.tree_usuarios.insert("", "end", values=(
                usuario.usuario, usuario.nombre, usuario.rol,
            ))

    # ══════════════════════════════════════════════════════════
    #  PANEL DE VENTAS  ← Flujo de eventos Semana 15
    # ══════════════════════════════════════════════════════════

    def _crear_panel_ventas(self) -> tk.Frame:
        panel = tk.Frame(self.contenido_frame, bg=self.BG_PANEL)

        tk.Label(
            panel, text="🛒  Registrar nueva venta", font=("Segoe UI", 15, "bold"),
            bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w",
        ).pack(fill="x", padx=16, pady=(16, 4))

        tk.Label(
            panel,
            text="Seleccione un usuario, un producto y la cantidad para registrar una venta.",
            font=("Segoe UI", 10),
            bg=self.BG_PANEL,
            fg=self.FG_SUBTITULO,
            anchor="w",
        ).pack(fill="x", padx=16, pady=(0, 10))

        # ── Formulario de selección ───────────────────────────
        form = tk.Frame(panel, bg=self.BG_CARD, padx=16, pady=14)
        form.pack(fill="x", padx=16, pady=(0, 8))

        # Fila 1: Usuario
        tk.Label(form, text="Usuario:", font=("Segoe UI", 11, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=0, column=0, sticky="w", pady=6, padx=(0, 10))
        self.combo_usuario = ttk.Combobox(form, state="readonly", width=32, font=("Segoe UI", 10))
        self.combo_usuario.grid(row=0, column=1, sticky="ew", pady=6)

        # Fila 2: Producto
        tk.Label(form, text="Producto:", font=("Segoe UI", 11, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=1, column=0, sticky="w", pady=6, padx=(0, 10))
        self.combo_producto = ttk.Combobox(form, state="readonly", width=32, font=("Segoe UI", 10))
        self.combo_producto.grid(row=1, column=1, sticky="ew", pady=6)

        # Fila 3: Cantidad
        tk.Label(form, text="Cantidad:", font=("Segoe UI", 11, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=2, column=0, sticky="w", pady=6, padx=(0, 10))
        self.spin_cantidad = ttk.Spinbox(form, from_=1, to=999, width=10, font=("Segoe UI", 10))
        self.spin_cantidad.set(1)
        self.spin_cantidad.grid(row=2, column=1, sticky="w", pady=6)

        form.columnconfigure(1, weight=1)

        # ── Botón "Registrar venta" ──────────────────────────
        # CLAVE: se usa command=self._callback_registrar_venta (sin paréntesis)
        # para vincular la acción del usuario al callback.
        btn_frame = tk.Frame(panel, bg=self.BG_PANEL)
        btn_frame.pack(fill="x", padx=16, pady=(4, 6))

        self.btn_registrar = tk.Button(
            btn_frame,
            text="  Registrar venta",
            font=("Segoe UI", 12, "bold"),
            bg=self.SUCCESS,
            fg=self.BTN_FG,
            activebackground="#16a34a",
            activeforeground=self.BTN_FG,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self._callback_registrar_venta,   # ← command= vincula el callback
        )
        if "registrar" in self.iconos:
            self.btn_registrar.config(image=self.iconos["registrar"], compound="left")
        self.btn_registrar.pack(side="left")

        # ── Etiqueta de resultado ─────────────────────────────
        self.lbl_resultado_venta = tk.Label(
            btn_frame, text="", font=("Segoe UI", 10, "bold"),
            bg=self.BG_PANEL, fg=self.SUCCESS, anchor="w",
        )
        self.lbl_resultado_venta.pack(side="left", padx=(16, 0), fill="x", expand=True)

        # ── Tabla de ventas registradas ───────────────────────
        tk.Label(
            panel, text="📋  Historial de ventas", font=("Segoe UI", 13, "bold"),
            bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w",
        ).pack(fill="x", padx=16, pady=(8, 4))

        columnas_ventas = ("fecha", "usuario", "producto", "cantidad")
        self.tree_ventas = ttk.Treeview(panel, columns=columnas_ventas, show="headings", height=8)
        for col, titulo, ancho in [
            ("fecha", "Fecha", 160), ("usuario", "Usuario", 160),
            ("producto", "Producto", 200), ("cantidad", "Cantidad", 90),
        ]:
            self.tree_ventas.heading(col, text=titulo)
            self.tree_ventas.column(col, width=ancho, anchor="center")

        scroll_v = ttk.Scrollbar(panel, orient="vertical", command=self.tree_ventas.yview)
        self.tree_ventas.configure(yscrollcommand=scroll_v.set)
        self.tree_ventas.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        scroll_v.pack(side="right", fill="y")

        return panel

    def _poblar_combos_ventas(self) -> None:
        """Llena los Combobox de usuarios y productos con datos actuales."""
        usuarios = self.servicio.listar_usuarios()
        self.combo_usuario["values"] = [
            f"{u.usuario} — {u.nombre}" for u in usuarios
        ]
        if usuarios:
            self.combo_usuario.current(0)

        productos = self.servicio.listar_productos()
        self.combo_producto["values"] = [
            f"{p.codigo} — {p.nombre} (${p.precio:.2f}) [Stock: {p.stock}]" for p in productos
        ]
        if productos:
            self.combo_producto.current(0)

    def _cargar_tabla_ventas(self) -> None:
        """Actualiza el Treeview de ventas con la información del servicio."""
        for item in self.tree_ventas.get_children():
            self.tree_ventas.delete(item)

        for venta in self.servicio.listar_ventas():
            producto = self.servicio.buscar_producto_por_codigo(venta.producto_codigo)
            nombre_producto = producto.nombre if producto else venta.producto_codigo
            usuario = self.servicio.buscar_usuario_por_id(venta.usuario_id)
            nombre_usuario = usuario.nombre if usuario else venta.usuario_id

            self.tree_ventas.insert("", "end", values=(
                venta.fecha, nombre_usuario, nombre_producto, venta.cantidad,
            ))

    # ── CALLBACK DE VENTA ─────────────────────────────────────
    # Este método es el callback que se ejecuta cuando el usuario
    # presiona el botón "Registrar venta". Coordina:
    # 1. Obtener datos de la interfaz (Combobox + Spinbox).
    # 2. Delegar la operación a RestauranteServicio.
    # 3. Actualizar la vista y mostrar el resultado.

    def _callback_registrar_venta(self) -> None:
        """Callback invocado mediante command= del botón Registrar venta.

        Flujo de eventos:
        BOTÓN → command= → callback → RestauranteServicio → persistencia → respuesta visual.
        """
        # 1. Obtener las selecciones de la interfaz
        sel_usuario = self.combo_usuario.get()
        sel_producto = self.combo_producto.get()

        if not sel_usuario:
            self._mostrar_resultado_venta("Seleccione un usuario.", error=True)
            return

        if not sel_producto:
            self._mostrar_resultado_venta("Seleccione un producto.", error=True)
            return

        # Extraer identificadores de las selecciones (formato: "id — nombre ...")
        usuario_id = sel_usuario.split(" — ")[0].strip()
        producto_codigo = sel_producto.split(" — ")[0].strip()

        try:
            cantidad = int(self.spin_cantidad.get())
        except ValueError:
            self._mostrar_resultado_venta("Ingrese una cantidad válida.", error=True)
            return

        # 2. Delegar la operación a RestauranteServicio
        ok, mensaje = self.servicio.registrar_venta(usuario_id, producto_codigo, cantidad)

        # 3. Actualizar la vista y mostrar respuesta visual
        if ok:
            self._mostrar_resultado_venta(mensaje, error=False)
            self._cargar_tabla_ventas()
            self._poblar_combos_ventas()  # refrescar stock en el combo
            self.spin_cantidad.set(1)
        else:
            self._mostrar_resultado_venta(mensaje, error=True)

    def _mostrar_resultado_venta(self, mensaje: str, error: bool = False) -> None:
        """Muestra el resultado de la operación de venta en la interfaz."""
        color = self.ERROR if error else self.SUCCESS
        self.lbl_resultado_venta.config(text=mensaje, fg=color)

    # ══════════════════════════════════════════════════════════
    #  NAVEGACIÓN ENTRE SECCIONES
    # ══════════════════════════════════════════════════════════

    def _mostrar_panel(self, panel: tk.Frame) -> None:
        """Oculta el panel activo y muestra el indicado."""
        if self._panel_activo is not None:
            self._panel_activo.pack_forget()
        panel.pack(in_=self.contenido_frame, fill="both", expand=True)
        self._panel_activo = panel

    def mostrar_seccion_productos(self) -> None:
        self._resaltar_boton_nav("productos")
        self._cargar_tabla_productos()
        self._mostrar_panel(self.panel_productos)

    def mostrar_seccion_usuarios(self) -> None:
        self._resaltar_boton_nav("usuarios")
        self._cargar_tabla_usuarios()
        self._mostrar_panel(self.panel_usuarios)

    def mostrar_seccion_ventas(self) -> None:
        self._resaltar_boton_nav("ventas")
        self._poblar_combos_ventas()
        self._cargar_tabla_ventas()
        self._mostrar_panel(self.panel_ventas)

    # ══════════════════════════════════════════════════════════
    #  VISIBILIDAD
    # ══════════════════════════════════════════════════════════

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def limpiar(self) -> None:
        pass
