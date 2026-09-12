"""Vista principal de la aplicación."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class MainView:
    """Panel principal con acceso a productos, usuarios y opciones pendientes."""

    def __init__(self, parent: tk.Misc, controller: object, restaurante_servicio: object) -> None:
        self.parent = parent
        self.controller = controller
        self.restaurante_servicio = restaurante_servicio

        self.frame = tk.Frame(parent, padx=20, pady=20, bg="#eef4ff")
        self.frame.configure(highlightbackground="#c7d2fe", highlightthickness=2)

        self.title_label = tk.Label(
            self.frame,
            text="Panel principal del restaurante",
            font=("Arial", 18, "bold"),
            bg="#eef4ff",
            fg="#1e3a8a",
        )
        self.title_label.pack(anchor="w", pady=(0, 16))

        self.action_frame = ttk.Frame(self.frame)
        self.action_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(self.action_frame, text="Productos", command=self.mostrar_productos).pack(side="left", padx=(0, 8))
        ttk.Button(self.action_frame, text="Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=(0, 8))
        ttk.Button(self.action_frame, text="Ventas (pendiente)", state="disabled").pack(side="left", padx=(0, 8))
        ttk.Button(self.action_frame, text="Cerrar sesión", command=self.controller.cerrar_sesion).pack(side="right")

        self.listbox = tk.Listbox(self.frame, width=95, height=18, font=("Consolas", 10), activestyle="none")
        self.listbox.pack(fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.mostrar_productos()

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def mostrar_productos(self) -> None:
        self._cargar_lista(self.restaurante_servicio.obtener_productos_formateados(), "Productos registrados")

    def mostrar_usuarios(self) -> None:
        self._cargar_lista(self.restaurante_servicio.obtener_usuarios_formateados(), "Usuarios registrados")

    def _cargar_lista(self, elementos: list[str], titulo: str) -> None:
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, f"{titulo}:")
        self.listbox.insert(tk.END, "")
        for elemento in elementos:
            self.listbox.insert(tk.END, elemento)

    def limpiar(self) -> None:
        self.listbox.delete(0, tk.END)
