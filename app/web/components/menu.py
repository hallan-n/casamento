from nicegui import ui

from web.utils import reset_css


def menu():
    reset_css()

    with ui.header().classes("bg-olive-1 p-4 shadow"):
        with ui.row().classes(
            "flex items-center justify-center sm:justify-between w-full mx-auto max-w-[1200px]"
        ):
            ui.image("app/web/assets/logo.svg").classes("w-12")
            with ui.element("div").classes(
                "flex gap-3 justify-between sm:w-auto w-full"
            ):
                ui.link("Início", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Administração", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Lista de presentes", "/").classes("cursor-pointer text-white no-underline")
