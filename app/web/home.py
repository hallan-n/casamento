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
                "z-[1000] flex flex-col items-center mt-28 md:mt-0 md:justify-center gap-2 text-white text-lg home-content"
            ):
                ui.image("app/web/assets/logo_full.svg")
                ui.image("app/web/assets/divider.svg")
                ui.label("Save the Date")
                ui.label("Sábado, 04 de Outubro, às 16h!").classes('text-bold')
                ui.label("Gostaríamos de convidá-lo(a)")
                ui.label("para celebrar conosco este")
                ui.label("momento especial de união.")
                with ui.element('a').classes(
                    'bg-black/20 hover:bg-black/50 flex flex-nowrap items-center gap-4 rounded-lg w-full p-4'
                ).props('href=https://maps.app.goo.gl/VH5fz9o2oMAg3LMx9 target=_blank'):
                    ui.icon('location_on')
                    ui.label("Paróquia de Santo André, Rua Santo André, 387 | Às 16h").classes("text-sm no-underline text-white")
    ui.element("div").classes("home-sm")