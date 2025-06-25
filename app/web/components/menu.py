from nicegui import ui


def menu():
    with ui.header().classes("bg-violet-400 p-4 shadow"):
        with ui.row().classes(
            "flex items-center justify sm:justify-between w-full mx-auto max-w-[1200px]"
        ):
            ui.image("app/web/assets/logo.svg").classes("w-12")
            with ui.element("div").classes(
                "flex gap-3 justify-between sm:w-auto w-full"
            ):
                ui.link("Rota 1", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Rota 2", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Rota 3", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Rota 4", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Rota 5", "/").classes("cursor-pointer text-white no-underline")
