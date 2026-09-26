"""Vista de acceso de la aplicación."""

from __future__ import annotations

import os
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


class LoginView:
    """Pantalla de autenticación para la app del restaurante.

    Utiliza el logo desde assets/ y presenta un diseño visual
    coherente con el tema oscuro de MainView.
    """

    BG = "#0f172a"
    BG_CARD = "#1e293b"
    FG_TITULO = "#f8fafc"
    FG_SUBTITULO = "#94a3b8"
    ACCENT = "#f59e0b"
    ERROR_COLOR = "#ef4444"
    SUCCESS_COLOR = "#22c55e"
    BTN_BG = "#3b82f6"
    BTN_FG = "#ffffff"

    def __init__(self, parent: tk.Misc, controller: object) -> None:
        self.parent = parent
        self.controller = controller

        # Cargar logo
        self.logo_image = None
        self._cargar_logo()

        # ── Contenedor centrado ───────────────────────────────
        self.frame = tk.Frame(parent, bg=self.BG)

        # Panel tipo tarjeta central
        card = tk.Frame(self.frame, bg=self.BG_CARD, padx=40, pady=32,
                        highlightbackground="#334155", highlightthickness=2)
        card.place(relx=0.5, rely=0.5, anchor="center")

        # Logo
        if self.logo_image is not None:
            tk.Label(card, image=self.logo_image, bg=self.BG_CARD).pack(pady=(0, 8))

        tk.Label(
            card, text="Restaurante App",
            font=("Segoe UI", 22, "bold"), bg=self.BG_CARD, fg=self.ACCENT,
        ).pack(pady=(0, 4))

        tk.Label(
            card, text="Inicia sesión para continuar",
            font=("Segoe UI", 10), bg=self.BG_CARD, fg=self.FG_SUBTITULO,
        ).pack(pady=(0, 20))

        # Usuario
        tk.Label(card, text="Usuario", font=("Segoe UI", 11, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TITULO, anchor="w").pack(fill="x")
        self.usuario_entry = ttk.Entry(card, width=32, font=("Segoe UI", 11))
        self.usuario_entry.pack(fill="x", pady=(4, 12))

        # Contraseña
        tk.Label(card, text="Contraseña", font=("Segoe UI", 11, "bold"),
                 bg=self.BG_CARD, fg=self.FG_TITULO, anchor="w").pack(fill="x")
        self.password_entry = ttk.Entry(card, width=32, show="•", font=("Segoe UI", 11))
        self.password_entry.pack(fill="x", pady=(4, 16))

        # Mensaje de error / éxito
        self.message_label = tk.Label(
            card, text="", bg=self.BG_CARD, fg=self.ERROR_COLOR,
            font=("Segoe UI", 10, "bold"), wraplength=300, justify="center",
        )
        self.message_label.pack(fill="x", pady=(0, 12))

        # Botón ingresar
        self.login_button = tk.Button(
            card, text="Ingresar", font=("Segoe UI", 12, "bold"),
            bg=self.BTN_BG, fg=self.BTN_FG,
            activebackground="#2563eb", activeforeground=self.BTN_FG,
            bd=0, padx=20, pady=10, cursor="hand2",
            command=self._login,
        )
        self.login_button.pack(fill="x")

        # Créditos
        tk.Label(
            card, text="Semana 15 · POO · UEA",
            font=("Segoe UI", 8), bg=self.BG_CARD, fg="#475569",
        ).pack(pady=(16, 0))

    def _cargar_logo(self) -> None:
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        ruta_logo = os.path.join(assets_dir, "logo_restaurante.png")
        if os.path.exists(ruta_logo):
            try:
                img = Image.open(ruta_logo).resize((72, 72), Image.LANCZOS)
                self.logo_image = ImageTk.PhotoImage(img)
            except Exception:
                pass

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)
        self.usuario_entry.focus_set()

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def limpiar(self) -> None:
        self.usuario_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.mostrar_mensaje("")

    def mostrar_mensaje(self, mensaje: str, color: str = "") -> None:
        if not color:
            color = self.ERROR_COLOR
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
