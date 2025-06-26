from nicegui import app, ui
from web.components.menu import menu
from web.utils import reset_css

app.add_static_files("/assets", "app/web/assets")


@ui.page("/")
async def index():
    menu()
    reset_css(ui)

    ui.element("div").classes("home")

    with ui.element("div").classes("absolute w-full h-full mx-auto bg-olive-1"):
        with ui.element("div").classes(
            "flex justify-end h-full max-w-[1200px] mx-auto"
        ):
            with ui.element("div").classes(
                "flex flex-col items-center justify-center gap-2"
            ):
                ui.image("app/web/assets/logo_full.svg")
                ui.image("app/web/assets/divider.svg")
                ui.label("Save the Date")
                ui.label("Sábado, 04 de Outubro!")
                ui.label("Gostaríamos de convidá-lo(a)")
                ui.label("para celebrar conosco este")
                ui.label("momento especial de união.")
