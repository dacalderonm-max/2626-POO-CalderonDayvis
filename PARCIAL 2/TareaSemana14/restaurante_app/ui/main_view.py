"""Vista principal de la aplicación."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class MainView:
    """Panel principal con navegación, formularios y contenido del restaurante."""

    def __init__(self, parent: tk.Misc, controller: object, restaurante_servicio: object) -> None:
        self.parent = parent
        self.controller = controller
        self.restaurante_servicio = restaurante_servicio

        self.frame = tk.Frame(parent, padx=18, pady=18, bg="#f4f7fb")
        self.frame.configure(highlightbackground="#c7d2fe", highlightthickness=2)

        self.title_label = tk.Label(
            self.frame,
            text="Panel principal del restaurante",
            font=("Arial", 18, "bold"),
            bg="#f4f7fb",
            fg="#1e3a8a",
        )
        self.title_label.pack(anchor="w", pady=(0, 16))

        self.body = tk.Frame(self.frame, bg="#f4f7fb")
        self.body.pack(fill="both", expand=True)

        self.nav_frame = ttk.Frame(self.body, padding=10)
        self.nav_frame.pack(side="left", fill="y", padx=(0, 16))

        self.nav_title = tk.Label(
            self.nav_frame,
            text="Navegación",
            font=("Arial", 12, "bold"),
            bg="#e2e8f0",
            fg="#1f2937",
        )
        self.nav_title.pack(fill="x", pady=(0, 12))

        ttk.Button(self.nav_frame, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=(0, 8))
        ttk.Button(self.nav_frame, text="Usuarios", command=self.mostrar_usuarios).pack(fill="x", pady=(0, 8))
        ttk.Button(self.nav_frame, text="Ventas", command=self.mostrar_ventas).pack(fill="x", pady=(0, 8))
        ttk.Button(self.nav_frame, text="Cerrar sesión", command=self.controller.cerrar_sesion).pack(fill="x", pady=(18, 0))

        self.content_frame = tk.Frame(self.body, bg="#ffffff")
        self.content_frame.pack(side="left", fill="both", expand=True)
        self.content_frame.configure(highlightbackground="#dbeafe", highlightthickness=1)

        self.productos_frame = ttk.Frame(self.content_frame, padding=12)
        self.usuarios_frame = ttk.Frame(self.content_frame, padding=12)
        self.ventas_frame = ttk.Frame(self.content_frame, padding=12)
        self.productos_frame.pack(fill="both", expand=True)
        self.usuarios_frame.pack(fill="both", expand=True)
        self.ventas_frame.pack(fill="both", expand=True)
        self.productos_frame.pack_forget()
        self.usuarios_frame.pack_forget()
        self.ventas_frame.pack_forget()

        self._crear_formulario_productos()
        self._crear_formulario_usuarios()
        self._crear_formulario_ventas()
        self._actualizar_lista_productos()
        self._actualizar_lista_usuarios()
        self._actualizar_lista_ventas()
        self.mostrar_productos()

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def mostrar_productos(self) -> None:
        self.productos_frame.pack(fill="both", expand=True)
        self.usuarios_frame.pack_forget()
        self.ventas_frame.pack_forget()
        self._actualizar_lista_productos()

    def mostrar_usuarios(self) -> None:
        self.usuarios_frame.pack(fill="both", expand=True)
        self.productos_frame.pack_forget()
        self.ventas_frame.pack_forget()
        self._actualizar_lista_usuarios()

    def mostrar_ventas(self) -> None:
        self.ventas_frame.pack(fill="both", expand=True)
        self.productos_frame.pack_forget()
        self.usuarios_frame.pack_forget()
        self._actualizar_lista_ventas()

    def _crear_formulario_productos(self) -> None:
        self.form_title = tk.Label(
            self.productos_frame,
            text="Gestión de productos",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="#1f2937",
        )
        self.form_title.pack(anchor="w", pady=(0, 12))

        self.formulario = ttk.LabelFrame(self.productos_frame, text="Datos del producto", padding=(12, 10))
        self.formulario.pack(fill="x", pady=(0, 12))

        self.codigo_entry = ttk.Entry(self.formulario, width=30)
        self.nombre_entry = ttk.Entry(self.formulario, width=30)
        self.categoria_entry = ttk.Entry(self.formulario, width=30)
        self.precio_entry = ttk.Entry(self.formulario, width=30)
        self.stock_entry = ttk.Entry(self.formulario, width=30)

        labels = [
            ("Código:", self.codigo_entry, 0),
            ("Nombre:", self.nombre_entry, 1),
            ("Categoría:", self.categoria_entry, 2),
            ("Precio:", self.precio_entry, 3),
            ("Stock:", self.stock_entry, 4),
        ]

        for texto, entry, fila in labels:
            ttk.Label(self.formulario, text=texto).grid(row=fila, column=0, sticky="w", padx=(0, 10), pady=6)
            entry.grid(row=fila, column=1, sticky="ew", pady=6)

        self.formulario.columnconfigure(1, weight=1)

        self.btn_frame = ttk.Frame(self.productos_frame)
        self.btn_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(self.btn_frame, text="Registrar", command=self.registrar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(self.btn_frame, text="Consultar", command=self.consultar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(self.btn_frame, text="Actualizar", command=self.actualizar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(self.btn_frame, text="Eliminar", command=self.eliminar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(self.btn_frame, text="Limpiar", command=self.limpiar_formulario).pack(side="left")

        self.message_label = tk.Label(
            self.productos_frame,
            text="",
            bg="#ffffff",
            fg="#1f2937",
            font=("Arial", 10, "bold"),
            anchor="w",
            justify="left",
            wraplength=600,
        )
        self.message_label.pack(fill="x", pady=(0, 12))

        self.product_tree = ttk.Treeview(
            self.productos_frame,
            columns=("codigo", "nombre", "categoria", "precio", "stock"),
            show="headings",
            height=11,
        )
        self.product_tree.heading("codigo", text="Código")
        self.product_tree.heading("nombre", text="Nombre")
        self.product_tree.heading("categoria", text="Categoría")
        self.product_tree.heading("precio", text="Precio")
        self.product_tree.heading("stock", text="Stock")

        self.product_tree.column("codigo", width=90, anchor="center")
        self.product_tree.column("nombre", width=220, anchor="w")
        self.product_tree.column("categoria", width=180, anchor="w")
        self.product_tree.column("precio", width=90, anchor="center")
        self.product_tree.column("stock", width=80, anchor="center")

        self.product_tree.pack(fill="both", expand=True)

    def _crear_formulario_usuarios(self) -> None:
        self.usuarios_title = tk.Label(
            self.usuarios_frame,
            text="Gestión de usuarios",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="#1f2937",
        )
        self.usuarios_title.pack(anchor="w", pady=(0, 12))

        self.user_form = ttk.LabelFrame(self.usuarios_frame, text="Datos del usuario", padding=(12, 10))
        self.user_form.pack(fill="x", pady=(0, 12))

        self.user_usuario_entry = ttk.Entry(self.user_form, width=30)
        self.user_password_entry = ttk.Entry(self.user_form, width=30, show="*")
        self.user_nombre_entry = ttk.Entry(self.user_form, width=30)
        self.user_rol_entry = ttk.Entry(self.user_form, width=30)

        for fila, (texto, entry) in enumerate(
            [
                ("Usuario:", self.user_usuario_entry),
                ("Contraseña:", self.user_password_entry),
                ("Nombre:", self.user_nombre_entry),
                ("Rol:", self.user_rol_entry),
            ]
        ):
            ttk.Label(self.user_form, text=texto).grid(row=fila, column=0, sticky="w", padx=(0, 10), pady=6)
            entry.grid(row=fila, column=1, sticky="ew", pady=6)

        self.user_form.columnconfigure(1, weight=1)

        self.user_btn_frame = ttk.Frame(self.usuarios_frame)
        self.user_btn_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(self.user_btn_frame, text="Registrar", command=self.registrar_usuario).pack(side="left", padx=(0, 8))
        ttk.Button(self.user_btn_frame, text="Consultar", command=self.consultar_usuario).pack(side="left", padx=(0, 8))
        ttk.Button(self.user_btn_frame, text="Actualizar", command=self.actualizar_usuario).pack(side="left", padx=(0, 8))
        ttk.Button(self.user_btn_frame, text="Eliminar", command=self.eliminar_usuario).pack(side="left", padx=(0, 8))
        ttk.Button(self.user_btn_frame, text="Limpiar", command=self.limpiar_formulario_usuario).pack(side="left")

        self.user_message = tk.Label(
            self.usuarios_frame,
            text="",
            bg="#ffffff",
            fg="#1f2937",
            font=("Arial", 10, "bold"),
            anchor="w",
            justify="left",
            wraplength=600,
        )
        self.user_message.pack(fill="x", pady=(0, 12))

        self.usuarios_text = tk.Text(self.usuarios_frame, height=14, wrap="word", state="disabled", font=("Consolas", 10))
        self.usuarios_text.pack(fill="both", expand=True)

    def _crear_formulario_ventas(self) -> None:
        self.ventas_title = tk.Label(
            self.ventas_frame,
            text="Gestión de ventas",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="#1f2937",
        )
        self.ventas_title.pack(anchor="w", pady=(0, 12))

        self.venta_form = ttk.LabelFrame(self.ventas_frame, text="Datos de la venta", padding=(12, 10))
        self.venta_form.pack(fill="x", pady=(0, 12))

        self.venta_usuario_entry = ttk.Entry(self.venta_form, width=30)
        self.venta_producto_entry = ttk.Entry(self.venta_form, width=30)
        self.venta_cantidad_entry = ttk.Entry(self.venta_form, width=30)

        for fila, (texto, entry) in enumerate(
            [
                ("Usuario:", self.venta_usuario_entry),
                ("Producto:", self.venta_producto_entry),
                ("Cantidad:", self.venta_cantidad_entry),
            ]
        ):
            ttk.Label(self.venta_form, text=texto).grid(row=fila, column=0, sticky="w", padx=(0, 10), pady=6)
            entry.grid(row=fila, column=1, sticky="ew", pady=6)

        self.venta_form.columnconfigure(1, weight=1)

        self.venta_btn_frame = ttk.Frame(self.ventas_frame)
        self.venta_btn_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(self.venta_btn_frame, text="Registrar", command=self.registrar_venta).pack(side="left", padx=(0, 8))
        ttk.Button(self.venta_btn_frame, text="Consultar", command=self.consultar_ventas).pack(side="left", padx=(0, 8))
        ttk.Button(self.venta_btn_frame, text="Limpiar", command=self.limpiar_formulario_venta).pack(side="left")

        self.ventas_message = tk.Label(
            self.ventas_frame,
            text="",
            bg="#ffffff",
            fg="#1f2937",
            font=("Arial", 10, "bold"),
            anchor="w",
            justify="left",
            wraplength=600,
        )
        self.ventas_message.pack(fill="x", pady=(0, 12))

        self.ventas_text = tk.Text(self.ventas_frame, height=14, wrap="word", state="disabled", font=("Consolas", 10))
        self.ventas_text.pack(fill="both", expand=True)

    def registrar_producto(self) -> None:
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()

        ok, mensaje = self.restaurante_servicio.registrar_producto(codigo, nombre, categoria, precio, stock)
        self._mostrar_mensaje(mensaje, ok)

        if ok:
            self.limpiar_formulario()
            self._actualizar_lista_productos()

    def consultar_producto(self) -> None:
        codigo = self.codigo_entry.get().strip()
        if not codigo:
            self._mostrar_mensaje("Ingrese el código del producto a consultar.", False)
            return

        producto = self.restaurante_servicio.consultar_producto(codigo)
        if producto is None:
            self._mostrar_mensaje(f"No existe el producto con código '{codigo}'.", False)
            return

        self.codigo_entry.delete(0, tk.END)
        self.codigo_entry.insert(0, producto.codigo)
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, producto.nombre)
        self.categoria_entry.delete(0, tk.END)
        self.categoria_entry.insert(0, producto.categoria)
        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, f"{producto.precio:.2f}")
        self.stock_entry.delete(0, tk.END)
        self.stock_entry.insert(0, str(producto.stock))
        self._mostrar_mensaje(f"Producto encontrado: {producto.mostrar_informacion()}", True)

    def actualizar_producto(self) -> None:
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()

        ok, mensaje = self.restaurante_servicio.actualizar_producto(codigo, nombre, categoria, precio, stock)
        self._mostrar_mensaje(mensaje, ok)

        if ok:
            self._actualizar_lista_productos()

    def eliminar_producto(self) -> None:
        codigo = self.codigo_entry.get().strip()
        if not codigo:
            self._mostrar_mensaje("Ingrese el código del producto a eliminar.", False)
            return

        ok, mensaje = self.restaurante_servicio.eliminar_producto(codigo)
        self._mostrar_mensaje(mensaje, ok)

        if ok:
            self.limpiar_formulario()
            self._actualizar_lista_productos()

    def registrar_usuario(self) -> None:
        usuario = self.user_usuario_entry.get()
        password = self.user_password_entry.get()
        nombre = self.user_nombre_entry.get()
        rol = self.user_rol_entry.get()

        ok, mensaje = self.restaurante_servicio.registrar_usuario(usuario, password, nombre, rol)
        self._mostrar_usuario_mensaje(mensaje, ok)

        if ok:
            self.limpiar_formulario_usuario()
            self._actualizar_lista_usuarios()

    def consultar_usuario(self) -> None:
        usuario = self.user_usuario_entry.get().strip()
        if not usuario:
            self._mostrar_usuario_mensaje("Ingrese el usuario a consultar.", False)
            return

        usuario_obj = self.restaurante_servicio.consultar_usuario(usuario)
        if usuario_obj is None:
            self._mostrar_usuario_mensaje(f"No existe el usuario '{usuario}'.", False)
            return

        self.user_usuario_entry.delete(0, tk.END)
        self.user_usuario_entry.insert(0, usuario_obj.usuario)
        self.user_password_entry.delete(0, tk.END)
        self.user_password_entry.insert(0, usuario_obj.password)
        self.user_nombre_entry.delete(0, tk.END)
        self.user_nombre_entry.insert(0, usuario_obj.nombre)
        self.user_rol_entry.delete(0, tk.END)
        self.user_rol_entry.insert(0, usuario_obj.rol)
        self._mostrar_usuario_mensaje(f"Usuario encontrado: {usuario_obj.mostrar_informacion()}", True)

    def actualizar_usuario(self) -> None:
        usuario = self.user_usuario_entry.get()
        password = self.user_password_entry.get()
        nombre = self.user_nombre_entry.get()
        rol = self.user_rol_entry.get()

        ok, mensaje = self.restaurante_servicio.actualizar_usuario(usuario, password, nombre, rol)
        self._mostrar_usuario_mensaje(mensaje, ok)

        if ok:
            self._actualizar_lista_usuarios()

    def eliminar_usuario(self) -> None:
        usuario = self.user_usuario_entry.get().strip()
        if not usuario:
            self._mostrar_usuario_mensaje("Ingrese el usuario a eliminar.", False)
            return

        ok, mensaje = self.restaurante_servicio.eliminar_usuario(usuario)
        self._mostrar_usuario_mensaje(mensaje, ok)

        if ok:
            self.limpiar_formulario_usuario()
            self._actualizar_lista_usuarios()

    def registrar_venta(self) -> None:
        usuario = self.venta_usuario_entry.get()
        producto = self.venta_producto_entry.get()
        cantidad = self.venta_cantidad_entry.get()

        ok, mensaje = self.restaurante_servicio.registrar_venta(usuario, producto, cantidad)
        self._mostrar_ventas_mensaje(mensaje, ok)

        if ok:
            self.limpiar_formulario_venta()
            self._actualizar_lista_ventas()
            self._actualizar_lista_productos()

    def consultar_ventas(self) -> None:
        usuario = self.venta_usuario_entry.get().strip()
        if not usuario:
            self._mostrar_ventas_mensaje("Ingrese el usuario para consultar sus ventas.", False)
            return

        ventas = self.restaurante_servicio.listar_ventas_por_usuario(usuario)
        self._mostrar_ventas_mensaje(f"Ventas para el usuario '{usuario}':", True)
        self.ventas_text.config(state="normal")
        self.ventas_text.delete("1.0", tk.END)
        for venta in ventas:
            self.ventas_text.insert(tk.END, venta + "\n")
        self.ventas_text.config(state="disabled")

    def limpiar_formulario(self) -> None:
        for entry in (self.codigo_entry, self.nombre_entry, self.categoria_entry, self.precio_entry, self.stock_entry):
            entry.delete(0, tk.END)
        self._mostrar_mensaje("", True)

    def limpiar_formulario_usuario(self) -> None:
        for entry in (self.user_usuario_entry, self.user_password_entry, self.user_nombre_entry, self.user_rol_entry):
            entry.delete(0, tk.END)
        self._mostrar_usuario_mensaje("", True)

    def limpiar_formulario_venta(self) -> None:
        for entry in (self.venta_usuario_entry, self.venta_producto_entry, self.venta_cantidad_entry):
            entry.delete(0, tk.END)
        self._mostrar_ventas_mensaje("", True)

    def _mostrar_mensaje(self, mensaje: str, ok: bool) -> None:
        self.message_label.config(text=mensaje, fg="#14532d" if ok else "#b91c1c")

    def _mostrar_usuario_mensaje(self, mensaje: str, ok: bool) -> None:
        self.user_message.config(text=mensaje, fg="#14532d" if ok else "#b91c1c")

    def _mostrar_ventas_mensaje(self, mensaje: str, ok: bool) -> None:
        self.ventas_message.config(text=mensaje, fg="#14532d" if ok else "#b91c1c")

    def _actualizar_lista_productos(self) -> None:
        for item in self.product_tree.get_children():
            self.product_tree.delete(item)

        for producto in self.restaurante_servicio.listar_productos():
            self.product_tree.insert(
                "",
                tk.END,
                values=(producto.codigo, producto.nombre, producto.categoria, f"{producto.precio:.2f}", producto.stock),
            )

    def _actualizar_lista_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.obtener_usuarios_formateados()
        self.usuarios_text.config(state="normal")
        self.usuarios_text.delete("1.0", tk.END)
        for usuario in usuarios:
            self.usuarios_text.insert(tk.END, usuario + "\n")
        self.usuarios_text.config(state="disabled")

    def _actualizar_lista_ventas(self) -> None:
        ventas = self.restaurante_servicio.obtener_ventas_formateadas()
        self.ventas_text.config(state="normal")
        self.ventas_text.delete("1.0", tk.END)
        for venta in ventas:
            self.ventas_text.insert(tk.END, venta + "\n")
        self.ventas_text.config(state="disabled")

    def limpiar(self) -> None:
        self.limpiar_formulario()
        self.limpiar_formulario_usuario()
        self.limpiar_formulario_venta()
        self._actualizar_lista_productos()
        self._actualizar_lista_usuarios()
        self._actualizar_lista_ventas()
