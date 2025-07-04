from nicegui import ui
from web.components.menu import menu
from web.utils import reset_css


@ui.page("/")
async def index():
    reset_css()
    menu()
    ui.add_head_html("""<style>body{overflow: hidden;}</style>""")

    ui.element("div").classes("home")

    with ui.element("div").classes("absolute w-full h-full mx-auto bg-olive-1 p-4"):
        with ui.element("div").classes(
            "flex justify-center lg:justify-end h-full max-w-[1200px] mx-auto"
        ):
            with ui.element("div").classes(
                "flex flex-col items-center justify-center gap-2 text-white text-2xl lg:text-3xl"
            ):
                ui.image("app/web/assets/logo_full.svg")
                ui.image("app/web/assets/divider.svg")
                ui.label("Save the Date")
                ui.label("Sábado, 04 de Outubro!")
                ui.label("Gostaríamos de convidá-lo(a)")
                ui.label("para celebrar conosco este")
                ui.label("momento especial de união.")
