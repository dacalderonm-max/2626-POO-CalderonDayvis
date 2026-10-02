"""Vista principal de la aplicación con secciones Productos, Usuarios y Ventas/Pedidos.

Semana 16: se incorpora manejo de eventos en la sección de Usuarios y un
sistema de pedidos en la sección de Ventas con vista diferenciada por rol.

VISTA VENTAS según rol:
  Administrador / Empleado → "Registrar venta directa" + "Pedidos pendientes" (Aprobar/Rechazar)
  Cliente                  → "Hacer mi pedido" + "Mis pedidos" (historial con estado)

Eventos implementados:
  <<TreeviewSelect>>     → cargar usuario en formulario (Usuarios)
                         → seleccionar pedido pendiente (Ventas Admin/Empleado)
  <Return>               → confirmar registro de usuario / enviar pedido (Cliente)
  <Escape>               → limpiar formulario de usuario
  <<ComboboxSelected>>   → responder al cambio de rol / cambio de producto
  command=               → todos los botones de acción principal
"""

from __future__ import annotations

import os
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class MainView:
    """Panel principal con navegación: Productos, Usuarios y Ventas/Pedidos."""

    # ── Paleta de colores ─────────────────────────────────────
    BG_PRINCIPAL = "#0f172a"
    BG_PANEL = "#1e293b"
    BG_CARD = "#334155"
    FG_TITULO = "#f8fafc"
    FG_SUBTITULO = "#94a3b8"
    FG_TEXTO = "#cbd5e1"
    ACCENT = "#f59e0b"
    SUCCESS = "#22c55e"
    ERROR = "#ef4444"
    BTN_BG = "#3b82f6"
    BTN_FG = "#ffffff"
    BTN_DANGER = "#ef4444"
    BTN_WARNING = "#f59e0b"
    BTN_NEUTRAL = "#475569"
    COLOR_PENDIENTE = "#f59e0b"
    COLOR_APROBADO = "#22c55e"
    COLOR_RECHAZADO = "#ef4444"

    def __init__(self, parent: tk.Misc, controller: object, restaurante_servicio: object) -> None:
        self.parent = parent
        self.controller = controller
        self.servicio = restaurante_servicio

        self._usuario_seleccionado_id: str | None = None
        self._pedido_seleccionado_id: str | None = None

        self.iconos: dict[str, ImageTk.PhotoImage] = {}
        self._cargar_iconos()

        self.frame = tk.Frame(parent, bg=self.BG_PRINCIPAL)
        self._crear_barra_superior()
        self._crear_barra_navegacion()

        self.contenido_frame = tk.Frame(self.frame, bg=self.BG_PRINCIPAL)
        self.contenido_frame.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        self.panel_productos = self._crear_panel_productos()
        self.panel_usuarios = self._crear_panel_usuarios()
        self.panel_ventas = self._crear_panel_ventas()

        self._panel_activo: tk.Frame | None = None
        self.mostrar_seccion_productos()

    # ══════════════════════════════════════════════════════════
    #  ASSETS
    # ══════════════════════════════════════════════════════════

    def _cargar_iconos(self) -> None:
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

        if "logo" in self.iconos:
            tk.Label(barra, image=self.iconos["logo"], bg=self.BG_PANEL).pack(side="left", padx=(0, 12))

        tk.Label(barra, text="Restaurante App", font=("Segoe UI", 20, "bold"),
                 bg=self.BG_PANEL, fg=self.ACCENT).pack(side="left")
        tk.Label(barra, text="— Semana 16", font=("Segoe UI", 12),
                 bg=self.BG_PANEL, fg=self.FG_SUBTITULO).pack(side="left", padx=(8, 0))

        btn_logout = tk.Button(
            barra, text="  Cerrar sesión", font=("Segoe UI", 10, "bold"),
            bg=self.ERROR, fg=self.BTN_FG, activebackground="#dc2626",
            activeforeground=self.BTN_FG, bd=0, padx=14, pady=6,
            cursor="hand2", command=self.controller.cerrar_sesion,
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
            ("ventas", "  Ventas / Pedidos", self.mostrar_seccion_ventas),
        ]
        for clave, texto, comando in secciones:
            btn = tk.Button(nav, text=texto, font=("Segoe UI", 11, "bold"),
                            bg=self.BG_CARD, fg=self.FG_TEXTO,
                            activebackground=self.ACCENT, activeforeground=self.BG_PRINCIPAL,
                            bd=0, padx=20, pady=8, cursor="hand2", command=comando)
            if clave in self.iconos:
                btn.config(image=self.iconos[clave], compound="left")
            btn.pack(side="left", padx=(0, 6))
            self.nav_buttons[clave] = btn

    def _resaltar_boton_nav(self, clave_activa: str) -> None:
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
        tk.Label(panel, text="📦  Productos del menú", font=("Segoe UI", 15, "bold"),
                 bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w").pack(fill="x", padx=16, pady=(16, 8))

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tree_productos = ttk.Treeview(panel, columns=columnas, show="headings", height=14)
        for col, titulo, ancho in [
            ("codigo", "Código", 80), ("nombre", "Nombre", 180),
            ("categoria", "Categoría", 140), ("precio", "Precio ($)", 100), ("stock", "Stock", 80),
        ]:
            self.tree_productos.heading(col, text=titulo)
            self.tree_productos.column(col, width=ancho, anchor="center")

        scroll_prod = ttk.Scrollbar(panel, orient="vertical", command=self.tree_productos.yview)
        self.tree_productos.configure(yscrollcommand=scroll_prod.set)
        self.tree_productos.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        scroll_prod.pack(side="right", fill="y")
        return panel

    def _cargar_tabla_productos(self) -> None:
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        for producto in self.servicio.listar_productos():
            self.tree_productos.insert("", "end", values=(
                producto.codigo, producto.nombre, producto.categoria,
                f"${producto.precio:.2f}", producto.stock,
            ))

    # ══════════════════════════════════════════════════════════
    #  PANEL DE USUARIOS  ← Gestión de eventos Semana 16
    # ══════════════════════════════════════════════════════════

    def _crear_panel_usuarios(self) -> tk.Frame:
        panel = tk.Frame(self.contenido_frame, bg=self.BG_PANEL)

        tk.Label(panel, text="👤  Gestión de Usuarios", font=("Segoe UI", 15, "bold"),
                 bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w").pack(fill="x", padx=16, pady=(16, 4))
        tk.Label(panel, text="Solo el Administrador puede registrar, actualizar y eliminar usuarios.",
                 font=("Segoe UI", 9), bg=self.BG_PANEL, fg=self.FG_SUBTITULO, anchor="w").pack(fill="x", padx=16, pady=(0, 10))

        main_frame = tk.Frame(panel, bg=self.BG_PANEL)
        main_frame.pack(fill="both", expand=True, padx=16, pady=(0, 12))

        # ─── FORMULARIO ──────────────────────────────────────
        form_wrapper = tk.Frame(main_frame, bg=self.BG_CARD, padx=16, pady=14, width=320)
        form_wrapper.pack(side="left", fill="y", padx=(0, 12))
        form_wrapper.pack_propagate(False)

        tk.Label(form_wrapper, text="Formulario de Usuario", font=("Segoe UI", 12, "bold"),
                 bg=self.BG_CARD, fg=self.ACCENT).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.lbl_modo_usuario = tk.Label(form_wrapper, text="Modo: Nuevo registro",
                                          font=("Segoe UI", 9, "italic"), bg=self.BG_CARD, fg=self.FG_SUBTITULO)
        self.lbl_modo_usuario.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 8))

        tk.Label(form_wrapper, text="Usuario *", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=2, column=0, sticky="w", pady=(4, 2))
        self.entry_usuario_id = ttk.Entry(form_wrapper, width=26, font=("Segoe UI", 10))
        self.entry_usuario_id.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 6))

        tk.Label(form_wrapper, text="Nombre completo *", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=4, column=0, sticky="w", pady=(4, 2))
        self.entry_nombre_usuario = ttk.Entry(form_wrapper, width=26, font=("Segoe UI", 10))
        self.entry_nombre_usuario.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 6))

        tk.Label(form_wrapper, text="Contraseña *", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=6, column=0, sticky="w", pady=(4, 2))
        self.entry_password_usuario = ttk.Entry(form_wrapper, width=26, show="•", font=("Segoe UI", 10))
        self.entry_password_usuario.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(0, 6))

        tk.Label(form_wrapper, text="Rol *", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).grid(row=8, column=0, sticky="w", pady=(4, 2))
        self.combo_rol_usuario = ttk.Combobox(form_wrapper, values=("Empleado", "Cliente"),
                                               state="readonly", width=24, font=("Segoe UI", 10))
        self.combo_rol_usuario.set("Empleado")
        self.combo_rol_usuario.grid(row=9, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        self.lbl_rol_info = tk.Label(form_wrapper, text="ℹ️  Empleado: acceso al sistema.",
                                      font=("Segoe UI", 8, "italic"), bg=self.BG_CARD, fg=self.FG_SUBTITULO,
                                      wraplength=260, justify="left")
        self.lbl_rol_info.grid(row=10, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.lbl_resultado_usuario = tk.Label(form_wrapper, text="", font=("Segoe UI", 9, "bold"),
                                               bg=self.BG_CARD, fg=self.SUCCESS, wraplength=260, justify="left")
        self.lbl_resultado_usuario.grid(row=11, column=0, columnspan=2, sticky="w", pady=(0, 8))

        btn_frame = tk.Frame(form_wrapper, bg=self.BG_CARD)
        btn_frame.grid(row=12, column=0, columnspan=2, sticky="ew", pady=(4, 0))

        self.btn_registrar_usuario = tk.Button(btn_frame, text="✚ Registrar", font=("Segoe UI", 10, "bold"),
            bg=self.SUCCESS, fg=self.BTN_FG, activebackground="#16a34a", activeforeground=self.BTN_FG,
            bd=0, padx=10, pady=6, cursor="hand2", width=10, command=self._cb_registrar_usuario)
        self.btn_registrar_usuario.grid(row=0, column=0, padx=(0, 4), pady=2, sticky="ew")

        self.btn_actualizar_usuario = tk.Button(btn_frame, text="✎ Actualizar", font=("Segoe UI", 10, "bold"),
            bg=self.BTN_WARNING, fg=self.BG_PRINCIPAL, activebackground="#d97706",
            activeforeground=self.BG_PRINCIPAL, bd=0, padx=10, pady=6, cursor="hand2", width=10,
            command=self._cb_actualizar_usuario)
        self.btn_actualizar_usuario.grid(row=0, column=1, padx=(0, 4), pady=2, sticky="ew")

        self.btn_eliminar_usuario = tk.Button(btn_frame, text="✖ Eliminar", font=("Segoe UI", 10, "bold"),
            bg=self.BTN_DANGER, fg=self.BTN_FG, activebackground="#dc2626", activeforeground=self.BTN_FG,
            bd=0, padx=10, pady=6, cursor="hand2", width=10, command=self._cb_eliminar_usuario)
        self.btn_eliminar_usuario.grid(row=1, column=0, padx=(0, 4), pady=2, sticky="ew")

        self.btn_limpiar_usuario = tk.Button(btn_frame, text="↺ Limpiar", font=("Segoe UI", 10, "bold"),
            bg=self.BTN_NEUTRAL, fg=self.BTN_FG, activebackground="#64748b", activeforeground=self.BTN_FG,
            bd=0, padx=10, pady=6, cursor="hand2", width=10, command=self._cb_limpiar_formulario_usuario)
        self.btn_limpiar_usuario.grid(row=1, column=1, padx=(0, 4), pady=2, sticky="ew")

        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        tk.Label(form_wrapper, text="Tip: Enter registra · Esc limpia", font=("Segoe UI", 8),
                 bg=self.BG_CARD, fg="#475569").grid(row=13, column=0, columnspan=2, sticky="w", pady=(8, 0))

        # ─── TABLA ───────────────────────────────────────────
        tabla_frame = tk.Frame(main_frame, bg=self.BG_PANEL)
        tabla_frame.pack(side="left", fill="both", expand=True)

        tk.Label(tabla_frame, text="📋  Usuarios registrados", font=("Segoe UI", 12, "bold"),
                 bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w").pack(fill="x", pady=(0, 6))

        columnas = ("id", "nombre", "rol")
        self.tree_usuarios = ttk.Treeview(tabla_frame, columns=columnas, show="headings",
                                           height=16, selectmode="browse")
        for col, titulo, ancho in [
            ("id", "Usuario", 130), ("nombre", "Nombre completo", 220), ("rol", "Rol", 110),
        ]:
            self.tree_usuarios.heading(col, text=titulo)
            self.tree_usuarios.column(col, width=ancho, anchor="center")

        scroll_usr = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscrollcommand=scroll_usr.set)
        self.tree_usuarios.pack(side="left", fill="both", expand=True)
        scroll_usr.pack(side="right", fill="y")

        # ══ BIND de eventos ══
        self.tree_usuarios.bind("<<TreeviewSelect>>", self._on_treeview_select_usuario)
        for widget in (self.entry_usuario_id, self.entry_nombre_usuario, self.entry_password_usuario):
            widget.bind("<Return>", self._on_return_usuarios)
            widget.bind("<Escape>", self._on_escape_usuarios)
        self.combo_rol_usuario.bind("<<ComboboxSelected>>", self._on_rol_seleccionado)

        return panel

    # ── Tabla usuarios ────────────────────────────────────────

    def _cargar_tabla_usuarios(self) -> None:
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        for usuario in self.servicio.listar_usuarios():
            self.tree_usuarios.insert("", "end", iid=usuario.usuario, values=(
                usuario.usuario, usuario.nombre, usuario.rol,
            ))

    # ── Callbacks bind() — Usuarios ───────────────────────────

    def _on_treeview_select_usuario(self, event) -> None:
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            return
        usuario_id = seleccion[0]
        self._usuario_seleccionado_id = usuario_id
        usuario = self.servicio.buscar_usuario_por_id(usuario_id)
        if usuario is None:
            return
        self.entry_usuario_id.config(state="normal")
        self.entry_usuario_id.delete(0, tk.END)
        self.entry_usuario_id.insert(0, usuario.usuario)
        self.entry_usuario_id.config(state="disabled")
        self.entry_nombre_usuario.delete(0, tk.END)
        self.entry_nombre_usuario.insert(0, usuario.nombre)
        self.entry_password_usuario.delete(0, tk.END)
        rol_actual = usuario.rol
        valores_combo = list(self.combo_rol_usuario["values"])
        if rol_actual not in valores_combo:
            self.combo_rol_usuario.config(values=list(valores_combo) + [rol_actual])
        self.combo_rol_usuario.set(rol_actual)
        self.lbl_modo_usuario.config(text=f"Modo: Editando → {usuario.usuario}", fg=self.ACCENT)
        self._actualizar_descripcion_rol(rol_actual)
        self.lbl_resultado_usuario.config(text="")

    def _on_return_usuarios(self, event) -> None:
        if self._usuario_seleccionado_id is not None:
            self._cb_actualizar_usuario()
        else:
            self._cb_registrar_usuario()

    def _on_escape_usuarios(self, event) -> None:
        self._cb_limpiar_formulario_usuario()

    def _on_rol_seleccionado(self, event) -> None:
        self._actualizar_descripcion_rol(self.combo_rol_usuario.get())

    # ── Callbacks command= — Usuarios ─────────────────────────

    def _cb_registrar_usuario(self) -> None:
        if not self.servicio.es_administrador_activo():
            self._mostrar_resultado_usuario("⚠ Solo el Administrador puede registrar usuarios.", error=True)
            return
        ok, mensaje = self.servicio.registrar_usuario(
            self.entry_usuario_id.get().strip(),
            self.entry_password_usuario.get().strip(),
            self.entry_nombre_usuario.get().strip(),
            self.combo_rol_usuario.get().strip(),
        )
        if ok:
            self._mostrar_resultado_usuario(f"✔ {mensaje}", error=False)
            self._cargar_tabla_usuarios()
            self._cb_limpiar_formulario_usuario()
        else:
            self._mostrar_resultado_usuario(f"✖ {mensaje}", error=True)

    def _cb_actualizar_usuario(self) -> None:
        if not self.servicio.es_administrador_activo():
            self._mostrar_resultado_usuario("⚠ Solo el Administrador puede actualizar usuarios.", error=True)
            return
        if self._usuario_seleccionado_id is None:
            self._mostrar_resultado_usuario("Seleccione un usuario en la tabla primero.", error=True)
            return
        password = self.entry_password_usuario.get().strip()
        if not password:
            u = self.servicio.buscar_usuario_por_id(self._usuario_seleccionado_id)
            if u:
                password = u.password
        ok, mensaje = self.servicio.actualizar_usuario(
            self._usuario_seleccionado_id,
            self.entry_nombre_usuario.get().strip(),
            password,
            self.combo_rol_usuario.get().strip(),
        )
        if ok:
            self._mostrar_resultado_usuario(f"✔ {mensaje}", error=False)
            self._cargar_tabla_usuarios()
            self._cb_limpiar_formulario_usuario()
        else:
            self._mostrar_resultado_usuario(f"✖ {mensaje}", error=True)

    def _cb_eliminar_usuario(self) -> None:
        if not self.servicio.es_administrador_activo():
            self._mostrar_resultado_usuario("⚠ Solo el Administrador puede eliminar usuarios.", error=True)
            return
        if self._usuario_seleccionado_id is None:
            self._mostrar_resultado_usuario("Seleccione un usuario en la tabla primero.", error=True)
            return
        if not messagebox.askyesno("Confirmar eliminación",
                                   f"¿Eliminar el usuario '{self._usuario_seleccionado_id}'?\n"
                                   "Esta acción no se puede deshacer.", icon="warning"):
            return
        ok, mensaje = self.servicio.eliminar_usuario(self._usuario_seleccionado_id)
        if ok:
            self._mostrar_resultado_usuario(f"✔ {mensaje}", error=False)
            self._cargar_tabla_usuarios()
            self._cb_limpiar_formulario_usuario()
        else:
            self._mostrar_resultado_usuario(f"✖ {mensaje}", error=True)

    def _cb_limpiar_formulario_usuario(self) -> None:
        self._usuario_seleccionado_id = None
        self.entry_usuario_id.config(state="normal")
        self.entry_usuario_id.delete(0, tk.END)
        self.entry_nombre_usuario.delete(0, tk.END)
        self.entry_password_usuario.delete(0, tk.END)
        self.combo_rol_usuario.config(values=("Empleado", "Cliente"))
        self.combo_rol_usuario.set("Empleado")
        self.tree_usuarios.selection_remove(self.tree_usuarios.selection())
        self.lbl_modo_usuario.config(text="Modo: Nuevo registro", fg=self.FG_SUBTITULO)
        self.lbl_resultado_usuario.config(text="")
        self._actualizar_descripcion_rol("Empleado")
        self.entry_usuario_id.focus_set()

    def _actualizar_descripcion_rol(self, rol: str) -> None:
        descripciones = {
            "Empleado": "ℹ️  Empleado: puede operar el sistema (ventas, productos).",
            "Cliente": "ℹ️  Cliente: puede hacer pedidos para aprobación del personal.",
            "Administrador": "⚠️  Administrador: acceso total. No puede asignarse desde aquí.",
        }
        self.lbl_rol_info.config(text=descripciones.get(rol, f"ℹ️  Rol: {rol}"))

    def _mostrar_resultado_usuario(self, mensaje: str, error: bool = False) -> None:
        self.lbl_resultado_usuario.config(text=mensaje, fg=self.ERROR if error else self.SUCCESS)

    def _configurar_acceso_usuarios(self) -> None:
        es_admin = self.servicio.es_administrador_activo()
        estado = "normal" if es_admin else "disabled"
        for widget in (self.entry_nombre_usuario, self.entry_password_usuario,
                       self.combo_rol_usuario, self.btn_registrar_usuario,
                       self.btn_actualizar_usuario, self.btn_eliminar_usuario):
            widget.config(state=estado)
        self.entry_usuario_id.config(state=estado)
        if not es_admin:
            self.lbl_resultado_usuario.config(
                text="ℹ️  Vista de solo lectura (requiere Administrador para modificar).",
                fg=self.FG_SUBTITULO)
        else:
            self.lbl_resultado_usuario.config(text="")

    # ══════════════════════════════════════════════════════════
    #  PANEL DE VENTAS / PEDIDOS  ← Vista dinámica por rol
    # ══════════════════════════════════════════════════════════

    def _crear_panel_ventas(self) -> tk.Frame:
        """Crea el contenedor principal de Ventas/Pedidos.

        Contiene dos sub-frames:
          _frame_ventas_personal  → para Admin y Empleado (venta directa + pedidos pendientes)
          _frame_ventas_cliente   → para Cliente (hacer pedido + mis pedidos)
        Solo uno es visible a la vez según el rol activo.
        """
        panel = tk.Frame(self.contenido_frame, bg=self.BG_PANEL)

        # ── Sub-frame Admin/Empleado ──────────────────────────
        self._frame_ventas_personal = self._crear_subframe_ventas_personal(panel)
        # ── Sub-frame Cliente ─────────────────────────────────
        self._frame_ventas_cliente = self._crear_subframe_ventas_cliente(panel)

        return panel

    # ── Sub-frame Admin/Empleado: venta directa + pedidos pendientes ──

    def _crear_subframe_ventas_personal(self, parent: tk.Frame) -> tk.Frame:
        frame = tk.Frame(parent, bg=self.BG_PANEL)

        # Título
        tk.Label(frame, text="🛒  Ventas y Pedidos pendientes",
                 font=("Segoe UI", 15, "bold"), bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w"
                 ).pack(fill="x", padx=16, pady=(16, 4))
        tk.Label(frame, text="Registre ventas directas o gestione los pedidos enviados por los clientes.",
                 font=("Segoe UI", 9), bg=self.BG_PANEL, fg=self.FG_SUBTITULO, anchor="w"
                 ).pack(fill="x", padx=16, pady=(0, 10))

        # Layout: izquierda = formulario | derecha = pedidos pendientes
        main = tk.Frame(frame, bg=self.BG_PANEL)
        main.pack(fill="both", expand=True, padx=16, pady=(0, 8))

        # ─── FORMULARIO VENTA DIRECTA (izquierda) ────────────
        form_card = tk.Frame(main, bg=self.BG_CARD, padx=16, pady=14, width=320)
        form_card.pack(side="left", fill="y", padx=(0, 12))
        form_card.pack_propagate(False)

        tk.Label(form_card, text="Registrar venta directa", font=("Segoe UI", 12, "bold"),
                 bg=self.BG_CARD, fg=self.ACCENT).pack(anchor="w", pady=(0, 10))

        tk.Label(form_card, text="Usuario:", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).pack(anchor="w")
        self.combo_usuario = ttk.Combobox(form_card, state="readonly", width=30, font=("Segoe UI", 10))
        self.combo_usuario.pack(fill="x", pady=(2, 8))

        tk.Label(form_card, text="Producto:", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).pack(anchor="w")
        self.combo_producto = ttk.Combobox(form_card, state="readonly", width=30, font=("Segoe UI", 10))
        self.combo_producto.pack(fill="x", pady=(2, 8))

        tk.Label(form_card, text="Cantidad:", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).pack(anchor="w")
        self.spin_cantidad = ttk.Spinbox(form_card, from_=1, to=999, width=10, font=("Segoe UI", 10))
        self.spin_cantidad.set(1)
        self.spin_cantidad.pack(anchor="w", pady=(2, 12))

        self.btn_registrar = tk.Button(
            form_card, text="  Registrar venta", font=("Segoe UI", 11, "bold"),
            bg=self.SUCCESS, fg=self.BTN_FG, activebackground="#16a34a",
            activeforeground=self.BTN_FG, bd=0, padx=16, pady=8, cursor="hand2",
            command=self._callback_registrar_venta,
        )
        if "registrar" in self.iconos:
            self.btn_registrar.config(image=self.iconos["registrar"], compound="left")
        self.btn_registrar.pack(fill="x")

        self.lbl_resultado_venta = tk.Label(
            form_card, text="", font=("Segoe UI", 9, "bold"),
            bg=self.BG_CARD, fg=self.SUCCESS, wraplength=260, justify="left")
        self.lbl_resultado_venta.pack(fill="x", pady=(8, 0))

        # ─── PEDIDOS PENDIENTES (derecha) ─────────────────────
        pedidos_frame = tk.Frame(main, bg=self.BG_PANEL)
        pedidos_frame.pack(side="left", fill="both", expand=True)

        encabezado = tk.Frame(pedidos_frame, bg=self.BG_PANEL)
        encabezado.pack(fill="x", pady=(0, 6))
        tk.Label(encabezado, text="📥  Pedidos de clientes", font=("Segoe UI", 12, "bold"),
                 bg=self.BG_PANEL, fg=self.FG_TITULO).pack(side="left")

        self.lbl_contador_pedidos = tk.Label(encabezado, text="", font=("Segoe UI", 10, "bold"),
                                              bg=self.BG_PANEL, fg=self.COLOR_PENDIENTE)
        self.lbl_contador_pedidos.pack(side="left", padx=(10, 0))

        cols_ped = ("pedido_id", "cliente", "producto", "cantidad", "fecha", "estado")
        self.tree_pedidos = ttk.Treeview(pedidos_frame, columns=cols_ped, show="headings",
                                          height=10, selectmode="browse")
        for col, titulo, ancho in [
            ("pedido_id", "ID Pedido", 140), ("cliente", "Cliente", 100),
            ("producto", "Producto", 160), ("cantidad", "Cant.", 55),
            ("fecha", "Fecha", 130), ("estado", "Estado", 90),
        ]:
            self.tree_pedidos.heading(col, text=titulo)
            self.tree_pedidos.column(col, width=ancho, anchor="center")

        # Etiquetas de color por estado
        self.tree_pedidos.tag_configure("pendiente", foreground=self.COLOR_PENDIENTE)
        self.tree_pedidos.tag_configure("aprobado", foreground=self.COLOR_APROBADO)
        self.tree_pedidos.tag_configure("rechazado", foreground=self.COLOR_RECHAZADO)

        scroll_ped = ttk.Scrollbar(pedidos_frame, orient="vertical", command=self.tree_pedidos.yview)
        self.tree_pedidos.configure(yscrollcommand=scroll_ped.set)
        self.tree_pedidos.pack(side="left", fill="both", expand=True)
        scroll_ped.pack(side="right", fill="y")

        # Botones Aprobar / Rechazar
        btn_ped_frame = tk.Frame(pedidos_frame, bg=self.BG_PANEL)
        btn_ped_frame.pack(fill="x", pady=(6, 0))

        self.btn_aprobar_pedido = tk.Button(
            btn_ped_frame, text="✔ Aprobar pedido", font=("Segoe UI", 10, "bold"),
            bg=self.SUCCESS, fg=self.BTN_FG, activebackground="#16a34a",
            activeforeground=self.BTN_FG, bd=0, padx=14, pady=7, cursor="hand2",
            command=self._cb_aprobar_pedido,
        )
        self.btn_aprobar_pedido.pack(side="left", padx=(0, 6))

        self.btn_rechazar_pedido = tk.Button(
            btn_ped_frame, text="✖ Rechazar pedido", font=("Segoe UI", 10, "bold"),
            bg=self.BTN_DANGER, fg=self.BTN_FG, activebackground="#dc2626",
            activeforeground=self.BTN_FG, bd=0, padx=14, pady=7, cursor="hand2",
            command=self._cb_rechazar_pedido,
        )
        self.btn_rechazar_pedido.pack(side="left")

        self.lbl_resultado_pedido_admin = tk.Label(
            btn_ped_frame, text="", font=("Segoe UI", 9, "bold"),
            bg=self.BG_PANEL, fg=self.SUCCESS)
        self.lbl_resultado_pedido_admin.pack(side="left", padx=(12, 0))

        # Bind: seleccionar un pedido en la tabla
        self.tree_pedidos.bind("<<TreeviewSelect>>", self._on_treeview_select_pedido)

        return frame

    # ── Sub-frame Cliente: hacer pedido + mis pedidos ─────────

    def _crear_subframe_ventas_cliente(self, parent: tk.Frame) -> tk.Frame:
        frame = tk.Frame(parent, bg=self.BG_PANEL)

        tk.Label(frame, text="🛍️  Hacer un pedido", font=("Segoe UI", 15, "bold"),
                 bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w").pack(fill="x", padx=16, pady=(16, 4))
        tk.Label(frame,
                 text="Seleccione un producto y la cantidad. El personal del restaurante aprobará su pedido.",
                 font=("Segoe UI", 9), bg=self.BG_PANEL, fg=self.FG_SUBTITULO, anchor="w"
                 ).pack(fill="x", padx=16, pady=(0, 10))

        main = tk.Frame(frame, bg=self.BG_PANEL)
        main.pack(fill="both", expand=True, padx=16, pady=(0, 8))

        # ─── FORMULARIO PEDIDO (izquierda) ────────────────────
        form_cli = tk.Frame(main, bg=self.BG_CARD, padx=16, pady=14, width=320)
        form_cli.pack(side="left", fill="y", padx=(0, 12))
        form_cli.pack_propagate(False)

        tk.Label(form_cli, text="Nuevo pedido", font=("Segoe UI", 12, "bold"),
                 bg=self.BG_CARD, fg=self.ACCENT).pack(anchor="w", pady=(0, 10))

        tk.Label(form_cli, text="Producto:", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).pack(anchor="w")
        self.combo_producto_cliente = ttk.Combobox(form_cli, state="readonly", width=30, font=("Segoe UI", 10))
        self.combo_producto_cliente.pack(fill="x", pady=(2, 8))

        # Descripción del producto seleccionado
        self.lbl_info_producto_cliente = tk.Label(
            form_cli, text="", font=("Segoe UI", 9, "italic"),
            bg=self.BG_CARD, fg=self.FG_SUBTITULO, wraplength=260, justify="left")
        self.lbl_info_producto_cliente.pack(anchor="w", pady=(0, 8))

        tk.Label(form_cli, text="Cantidad:", font=("Segoe UI", 10, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TEXTO).pack(anchor="w")
        self.spin_cantidad_cliente = ttk.Spinbox(form_cli, from_=1, to=999, width=10, font=("Segoe UI", 10))
        self.spin_cantidad_cliente.set(1)
        self.spin_cantidad_cliente.pack(anchor="w", pady=(2, 14))

        self.btn_enviar_pedido = tk.Button(
            form_cli, text="📤 Enviar pedido", font=("Segoe UI", 11, "bold"),
            bg=self.BTN_BG, fg=self.BTN_FG, activebackground="#2563eb",
            activeforeground=self.BTN_FG, bd=0, padx=16, pady=8, cursor="hand2",
            command=self._cb_crear_pedido,
        )
        self.btn_enviar_pedido.pack(fill="x")

        self.lbl_resultado_pedido_cliente = tk.Label(
            form_cli, text="", font=("Segoe UI", 9, "bold"),
            bg=self.BG_CARD, fg=self.SUCCESS, wraplength=260, justify="left")
        self.lbl_resultado_pedido_cliente.pack(fill="x", pady=(8, 0))

        tk.Label(form_cli, text="Tip: Enter envía el pedido",
                 font=("Segoe UI", 8), bg=self.BG_CARD, fg="#475569").pack(anchor="w", pady=(8, 0))

        # ─── MIS PEDIDOS (derecha) ────────────────────────────
        mis_pedidos_frame = tk.Frame(main, bg=self.BG_PANEL)
        mis_pedidos_frame.pack(side="left", fill="both", expand=True)

        tk.Label(mis_pedidos_frame, text="📋  Mis pedidos", font=("Segoe UI", 12, "bold"),
                 bg=self.BG_PANEL, fg=self.FG_TITULO).pack(anchor="w", pady=(0, 6))

        cols_mis = ("pedido_id", "producto", "cantidad", "fecha", "estado")
        self.tree_mis_pedidos = ttk.Treeview(mis_pedidos_frame, columns=cols_mis, show="headings",
                                              height=14, selectmode="none")
        for col, titulo, ancho in [
            ("pedido_id", "ID Pedido", 150), ("producto", "Producto", 200),
            ("cantidad", "Cant.", 60), ("fecha", "Fecha", 140), ("estado", "Estado", 100),
        ]:
            self.tree_mis_pedidos.heading(col, text=titulo)
            self.tree_mis_pedidos.column(col, width=ancho, anchor="center")

        self.tree_mis_pedidos.tag_configure("pendiente", foreground=self.COLOR_PENDIENTE)
        self.tree_mis_pedidos.tag_configure("aprobado", foreground=self.COLOR_APROBADO)
        self.tree_mis_pedidos.tag_configure("rechazado", foreground=self.COLOR_RECHAZADO)

        scroll_mis = ttk.Scrollbar(mis_pedidos_frame, orient="vertical", command=self.tree_mis_pedidos.yview)
        self.tree_mis_pedidos.configure(yscrollcommand=scroll_mis.set)
        self.tree_mis_pedidos.pack(side="left", fill="both", expand=True)
        scroll_mis.pack(side="right", fill="y")

        # Binds para la vista cliente
        self.combo_producto_cliente.bind("<<ComboboxSelected>>", self._on_producto_cliente_seleccionado)
        self.spin_cantidad_cliente.bind("<Return>", self._on_return_pedido_cliente)

        return frame

    # ── Carga de datos — Ventas/Pedidos ───────────────────────

    def _poblar_combos_ventas(self) -> None:
        usuarios = self.servicio.listar_usuarios()
        self.combo_usuario["values"] = [f"{u.usuario} — {u.nombre}" for u in usuarios]
        if usuarios:
            self.combo_usuario.current(0)

        productos = self.servicio.listar_productos()
        self.combo_producto["values"] = [
            f"{p.codigo} — {p.nombre} (${p.precio:.2f}) [Stock: {p.stock}]" for p in productos
        ]
        if productos:
            self.combo_producto.current(0)

    def _poblar_combo_productos_cliente(self) -> None:
        productos = self.servicio.listar_productos()
        self.combo_producto_cliente["values"] = [
            f"{p.codigo} — {p.nombre} (${p.precio:.2f})" for p in productos
        ]
        if productos:
            self.combo_producto_cliente.current(0)
            self._actualizar_info_producto_cliente()

    def _cargar_tabla_ventas(self) -> None:
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

    def _cargar_tabla_pedidos_admin(self) -> None:
        """Carga TODOS los pedidos en la tabla de Admin/Empleado (con colores por estado)."""
        for item in self.tree_pedidos.get_children():
            self.tree_pedidos.delete(item)
        pedidos = self.servicio.listar_pedidos()
        for pedido in reversed(pedidos):  # más recientes primero
            producto = self.servicio.buscar_producto_por_codigo(pedido.producto_codigo)
            nombre_prod = producto.nombre if producto else pedido.producto_codigo
            self.tree_pedidos.insert("", "end", iid=pedido.pedido_id, values=(
                pedido.pedido_id, pedido.cliente_id, nombre_prod,
                pedido.cantidad, pedido.fecha, pedido.estado.capitalize(),
            ), tags=(pedido.estado,))

        pendientes = len(self.servicio.listar_pedidos_pendientes())
        self.lbl_contador_pedidos.config(
            text=f"({pendientes} pendiente{'s' if pendientes != 1 else ''})" if pendientes else "")

    def _cargar_tabla_mis_pedidos(self, cliente_id: str) -> None:
        """Carga los pedidos del cliente activo en su tabla personal."""
        for item in self.tree_mis_pedidos.get_children():
            self.tree_mis_pedidos.delete(item)
        pedidos = self.servicio.listar_pedidos_de_cliente(cliente_id)
        for pedido in reversed(pedidos):
            producto = self.servicio.buscar_producto_por_codigo(pedido.producto_codigo)
            nombre_prod = producto.nombre if producto else pedido.producto_codigo
            self.tree_mis_pedidos.insert("", "end", values=(
                pedido.pedido_id, nombre_prod, pedido.cantidad,
                pedido.fecha, pedido.estado.capitalize(),
            ), tags=(pedido.estado,))

    def _actualizar_info_producto_cliente(self) -> None:
        """Muestra precio y stock del producto seleccionado por el Cliente."""
        sel = self.combo_producto_cliente.get()
        if not sel:
            return
        codigo = sel.split(" — ")[0].strip()
        producto = self.servicio.buscar_producto_por_codigo(codigo)
        if producto:
            self.lbl_info_producto_cliente.config(
                text=f"Categoría: {producto.categoria} · Stock disponible: {producto.stock}")
        else:
            self.lbl_info_producto_cliente.config(text="")

    # ── Callbacks bind() — Ventas/Pedidos ─────────────────────

    def _on_treeview_select_pedido(self, event) -> None:
        """<<TreeviewSelect>> en la tabla de pedidos: guarda el pedido_id seleccionado."""
        seleccion = self.tree_pedidos.selection()
        if not seleccion:
            self._pedido_seleccionado_id = None
            return
        self._pedido_seleccionado_id = seleccion[0]
        self.lbl_resultado_pedido_admin.config(text="")

    def _on_producto_cliente_seleccionado(self, event) -> None:
        """<<ComboboxSelected>> en el combo de productos del cliente."""
        self._actualizar_info_producto_cliente()

    def _on_return_pedido_cliente(self, event) -> None:
        """<Return> en el spinner de cantidad del cliente: envía el pedido."""
        self._cb_crear_pedido()

    # ── Callbacks command= — Ventas ───────────────────────────

    def _callback_registrar_venta(self) -> None:
        sel_usuario = self.combo_usuario.get()
        sel_producto = self.combo_producto.get()
        if not sel_usuario:
            self._mostrar_resultado_venta("Seleccione un usuario.", error=True)
            return
        if not sel_producto:
            self._mostrar_resultado_venta("Seleccione un producto.", error=True)
            return
        usuario_id = sel_usuario.split(" — ")[0].strip()
        producto_codigo = sel_producto.split(" — ")[0].strip()
        try:
            cantidad = int(self.spin_cantidad.get())
        except ValueError:
            self._mostrar_resultado_venta("Ingrese una cantidad válida.", error=True)
            return
        ok, mensaje = self.servicio.registrar_venta(usuario_id, producto_codigo, cantidad)
        if ok:
            self._mostrar_resultado_venta(mensaje, error=False)
            self._poblar_combos_ventas()
            self.spin_cantidad.set(1)
        else:
            self._mostrar_resultado_venta(mensaje, error=True)

    def _mostrar_resultado_venta(self, mensaje: str, error: bool = False) -> None:
        self.lbl_resultado_venta.config(text=mensaje, fg=self.ERROR if error else self.SUCCESS)

    # ── Callbacks command= — Pedidos Admin/Empleado ───────────

    def _cb_aprobar_pedido(self) -> None:
        if self._pedido_seleccionado_id is None:
            self.lbl_resultado_pedido_admin.config(
                text="Seleccione un pedido pendiente en la tabla.", fg=self.ERROR)
            return
        ok, mensaje = self.servicio.aprobar_pedido(self._pedido_seleccionado_id)
        color = self.SUCCESS if ok else self.ERROR
        self.lbl_resultado_pedido_admin.config(text=f"{'✔' if ok else '✖'} {mensaje}", fg=color)
        if ok:
            self._cargar_tabla_pedidos_admin()
            self._poblar_combos_ventas()
            self._pedido_seleccionado_id = None

    def _cb_rechazar_pedido(self) -> None:
        if self._pedido_seleccionado_id is None:
            self.lbl_resultado_pedido_admin.config(
                text="Seleccione un pedido en la tabla.", fg=self.ERROR)
            return
        if not messagebox.askyesno("Confirmar rechazo",
                                   f"¿Rechazar el pedido '{self._pedido_seleccionado_id}'?",
                                   icon="warning"):
            return
        ok, mensaje = self.servicio.rechazar_pedido(self._pedido_seleccionado_id)
        color = self.SUCCESS if ok else self.ERROR
        self.lbl_resultado_pedido_admin.config(text=f"{'✔' if ok else '✖'} {mensaje}", fg=color)
        if ok:
            self._cargar_tabla_pedidos_admin()
            self._pedido_seleccionado_id = None

    # ── Callbacks command= — Pedidos Cliente ──────────────────

    def _cb_crear_pedido(self) -> None:
        """El Cliente envía un pedido para aprobación."""
        usuario_activo = self.servicio.obtener_usuario_activo()
        if usuario_activo is None:
            return

        sel = self.combo_producto_cliente.get()
        if not sel:
            self.lbl_resultado_pedido_cliente.config(
                text="Seleccione un producto.", fg=self.ERROR)
            return

        codigo = sel.split(" — ")[0].strip()
        try:
            cantidad = int(self.spin_cantidad_cliente.get())
        except ValueError:
            self.lbl_resultado_pedido_cliente.config(
                text="Ingrese una cantidad válida.", fg=self.ERROR)
            return

        ok, mensaje = self.servicio.crear_pedido(usuario_activo.usuario, codigo, cantidad)
        color = self.SUCCESS if ok else self.ERROR
        self.lbl_resultado_pedido_cliente.config(text=f"{'✔' if ok else '✖'} {mensaje}", fg=color)

        if ok:
            self.spin_cantidad_cliente.set(1)
            self._poblar_combo_productos_cliente()
            self._cargar_tabla_mis_pedidos(usuario_activo.usuario)

    # ── Añadir tabla historial ventas al sub-frame personal ───

    def _agregar_tabla_ventas_al_frame(self) -> None:
        """Añade la tabla de historial de ventas debajo del sub-frame personal.

        Se llama una sola vez durante la creación (necesita acceso al frame ya creado).
        """
        tk.Label(self._frame_ventas_personal, text="📋  Historial de ventas",
                 font=("Segoe UI", 12, "bold"), bg=self.BG_PANEL, fg=self.FG_TITULO, anchor="w"
                 ).pack(fill="x", padx=16, pady=(8, 4))

        cols_v = ("fecha", "usuario", "producto", "cantidad")
        self.tree_ventas = ttk.Treeview(self._frame_ventas_personal, columns=cols_v,
                                         show="headings", height=5)
        for col, titulo, ancho in [
            ("fecha", "Fecha", 160), ("usuario", "Usuario", 150),
            ("producto", "Producto", 200), ("cantidad", "Cantidad", 90),
        ]:
            self.tree_ventas.heading(col, text=titulo)
            self.tree_ventas.column(col, width=ancho, anchor="center")

        scroll_v = ttk.Scrollbar(self._frame_ventas_personal, orient="vertical",
                                  command=self.tree_ventas.yview)
        self.tree_ventas.configure(yscrollcommand=scroll_v.set)
        self.tree_ventas.pack(fill="both", expand=True, padx=16, pady=(0, 8))
        scroll_v.pack(side="right", fill="y")

    # ══════════════════════════════════════════════════════════
    #  NAVEGACIÓN ENTRE SECCIONES
    # ══════════════════════════════════════════════════════════

    def _mostrar_panel(self, panel: tk.Frame) -> None:
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
        self._cb_limpiar_formulario_usuario()
        self._configurar_acceso_usuarios()
        self._mostrar_panel(self.panel_usuarios)

    def mostrar_seccion_ventas(self) -> None:
        self._resaltar_boton_nav("ventas")
        self._mostrar_panel(self.panel_ventas)
        self._configurar_vista_ventas()

    def _configurar_vista_ventas(self) -> None:
        """Muestra el sub-frame correcto según el rol del usuario activo."""
        es_cliente = self.servicio.es_cliente_activo()

        if es_cliente:
            # Ocultar vista personal, mostrar vista cliente
            self._frame_ventas_personal.pack_forget()
            self._frame_ventas_cliente.pack(fill="both", expand=True)
            self._poblar_combo_productos_cliente()
            usuario = self.servicio.obtener_usuario_activo()
            if usuario:
                self._cargar_tabla_mis_pedidos(usuario.usuario)
        else:
            # Ocultar vista cliente, mostrar vista personal
            self._frame_ventas_cliente.pack_forget()
            self._frame_ventas_personal.pack(fill="both", expand=True)
            # Asegurar que la tabla de ventas existe (creación diferida)
            if not hasattr(self, "tree_ventas"):
                self._agregar_tabla_ventas_al_frame()
            self._poblar_combos_ventas()
            self._cargar_tabla_ventas()
            self._cargar_tabla_pedidos_admin()

    # ══════════════════════════════════════════════════════════
    #  VISIBILIDAD
    # ══════════════════════════════════════════════════════════

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def limpiar(self) -> None:
        pass
