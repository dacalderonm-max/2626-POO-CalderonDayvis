"""Punto de entrada GUI para la versión Tkinter de Restaurante App."""

from __future__ import annotations

import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class App:
    """Controlador principal que administra la única ventana y las vistas."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Restaurante App - Semana 14")
        self.root.geometry("1100x720")
        self.root.minsize(900, 620)

        self.restaurante_servicio = RestauranteServicio()

        self.login_view = LoginView(self.root, self)
        self.main_view = MainView(self.root, self, self.restaurante_servicio)

        self.show_login()

    def show_login(self) -> None:
        self.main_view.ocultar()
        self.login_view.limpiar()
        self.login_view.mostrar()

    def show_main(self) -> None:
        self.login_view.ocultar()
        self.main_view.mostrar()
        self.main_view.mostrar_productos()

    def iniciar_sesion(self, usuario: str, password: str) -> tuple[bool, str]:
        ok, mensaje = self.restaurante_servicio.validar_acceso(usuario, password)
        if ok:
            self.show_main()
            return True, mensaje
        return False, mensaje

    def cerrar_sesion(self) -> None:
        self.show_login()


def main() -> None:
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
