"""Punto de entrada GUI para la versión Tkinter de Restaurante App.

Semana 16: incorpora la gestión completa de usuarios con manejo de eventos.
Flujo: USUARIO → EVENTO → bind() / command= → CALLBACK → RestauranteServicio
       → PERSISTENCIA → RESPUESTA VISUAL.
"""

from __future__ import annotations

import os
import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class App:
    """Controlador principal que administra la única ventana y las vistas."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Restaurante App — Semana 16")
        self.root.geometry("1100x720")
        self.root.minsize(900, 620)
        self.root.configure(bg="#0f172a")

        # Establecer ícono de la ventana desde assets/
        self._establecer_icono()

        self.restaurante_servicio = RestauranteServicio()

        # crear vistas
        self.login_view = LoginView(self.root, self)
        self.main_view = MainView(self.root, self, self.restaurante_servicio)

        self.show_login()

    def _establecer_icono(self) -> None:
        """Intenta establecer el ícono de la ventana usando el logo de assets/."""
        try:
            from PIL import Image, ImageTk
            assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
            ruta_logo = os.path.join(assets_dir, "logo_restaurante.png")
            if os.path.exists(ruta_logo):
                img = Image.open(ruta_logo).resize((32, 32), Image.LANCZOS)
                self._icono = ImageTk.PhotoImage(img)
                self.root.iconphoto(True, self._icono)
        except Exception:
            pass  # Si falla la carga del ícono, la app continúa sin él

    def show_login(self) -> None:
        self.main_view.ocultar()
        self.login_view.limpiar()
        self.login_view.mostrar()

    def show_main(self) -> None:
        self.login_view.ocultar()
        self.main_view.mostrar()

    def iniciar_sesion(self, usuario: str, password: str) -> tuple[bool, str]:
        ok, mensaje = self.restaurante_servicio.validar_acceso(usuario, password)
        if ok:
            self.show_main()
            return True, mensaje
        # no hacer cambio de vista; dejar que la vista muestre el mensaje
        return False, mensaje

    def cerrar_sesion(self) -> None:
        self.restaurante_servicio.usuario_activo = ""
        self.show_login()


def main() -> None:
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
