"""Vista de acceso de la aplicación."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class LoginView:
    """Pantalla de autenticación simulada para la app del restaurante."""

    def __init__(self, parent: tk.Misc, controller: object) -> None:
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, padx=24, pady=28, bg="#f3f6fb")
        self.frame.configure(highlightbackground="#d9e2f3", highlightthickness=2)

        self.title_label = tk.Label(
            self.frame,
            text="Acceso al restaurante",
            font=("Arial", 18, "bold"),
            bg="#f3f6fb",
            fg="#1f2937",
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 18))

        tk.Label(self.frame, text="Usuario:", bg="#f3f6fb", font=("Arial", 11, "bold")).grid(
            row=1, column=0, sticky="w", pady=(0, 8)
        )
        self.usuario_entry = ttk.Entry(self.frame, width=30)
        self.usuario_entry.grid(row=1, column=1, padx=(0, 8), pady=(0, 8), sticky="ew")

        tk.Label(self.frame, text="Contraseña:", bg="#f3f6fb", font=("Arial", 11, "bold")).grid(
            row=2, column=0, sticky="w", pady=(0, 12)
        )
        self.password_entry = ttk.Entry(self.frame, width=30, show="*")
        self.password_entry.grid(row=2, column=1, padx=(0, 8), pady=(0, 12), sticky="ew")

        self.message_label = tk.Label(
            self.frame,
            text="",
            bg="#f3f6fb",
            fg="#b91c1c",
            font=("Arial", 10, "bold"),
            wraplength=320,
            justify="left",
        )
        self.message_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 12))

        self.login_button = ttk.Button(self.frame, text="Ingresar", command=self._login)
        self.login_button.grid(row=4, column=0, columnspan=2, sticky="ew")

        self.frame.columnconfigure(1, weight=1)

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)
        self.usuario_entry.focus_set()

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def limpiar(self) -> None:
        self.usuario_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.mostrar_mensaje("")

    def mostrar_mensaje(self, mensaje: str, color: str = "#b91c1c") -> None:
        self.message_label.config(text=mensaje, fg=color)

    def _login(self) -> None:
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()
        resultado = self.controller.iniciar_sesion(usuario, password)
        # controller returns tuple (ok, mensaje)
        if isinstance(resultado, tuple) and len(resultado) == 2:
            ok, mensaje = resultado
            if not ok:
                self.mostrar_mensaje(mensaje)
            else:
                self.mostrar_mensaje("")
        else:
            # backward compatibility: falsy means error
            if not resultado:
                self.mostrar_mensaje("Usuario o contraseña incorrectos.")
