from nicegui import ui
from web.components.menu import menu
from web.utils import reset_css


@ui.page("/")
async def index():
    reset_css()
    menu()
    ui.add_head_html("""<style>body{overflow: hidden;}</style>""")

    ui.element("div").classes("home-lg")

    with ui.element("div").classes("absolute w-full h-full mx-auto bg-olive-1 p-4 z-auto"):
        with ui.element("div").classes(
            "flex justify-center lg:justify-end h-full max-w-[1200px] mx-auto"
        ):
            with ui.element("div").classes(
                "flex flex-col items-center mt-28 md:mt-0 md:justify-center gap-2 text-white text-lg home-content"
            ):
                ui.image("app/web/assets/logo_full.svg")
                ui.image("app/web/assets/divider.svg")
                ui.label("Save the Date")
                ui.label("Sábado, 04 de Outubro!")
                ui.label("Gostaríamos de convidá-lo(a)")
                ui.label("para celebrar conosco este")
                ui.label("momento especial de união.")
                with ui.element('div').classes('flex flex-nowrap items-center gap-4 rounded-lg w-full p-4').style("""background-color: rgba(0, 0, 0, 0.2);"""):
                    ui.icon('location_on')
                    ui.link("Paróquia de Santo André, Rua Santo André, 387", "https://maps.app.goo.gl/VH5fz9o2oMAg3LMx9", new_tab=True).classes("text-sm no-underline text-white")
    ui.element("div").classes("home-sm")