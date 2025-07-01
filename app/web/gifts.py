from nicegui import ui
from web.components.menu import menu


@ui.page("/gifts")
async def index():
    lista = [
        {
            "id": 0,
            "thumb": "string",
            "name": "string",
            "url": "string",
            "price": 0,
            "guest_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        },
        {
            "id": 0,
            "thumb": "string",
            "name": "string",
            "url": "string",
            "price": 0,
            "guest_id": "",
        },
    ]
    menu()

    with ui.element("div").classes("flex gap-2 w-full justify-center mt-40 h-screen"):
        for item in lista:
            with ui.card().classes("max-h-[500px]"):
                ui.image(
                    "https://d1ih8jugeo2m5m.cloudfront.net/2020/11/editar-pagina-de-produtos.jpg"
                ).classes("rounded-lg w-96 h-96 object-cover")
                ui.label("Carrinho de compras").classes("text-bold text-lg mt-4")
                with ui.element("div").classes(
                    "flex w-full justify-between items-center mt-4"
                ):
                    ui.label("R$ 30,00").classes("text-2xl")
                    if not item["guest_id"]:
                        ui.button(
                            text="Dar presente",
                            icon="add_shopping_cart",
                            color=None,
                        ).classes("bg-[#6b6d4a] text-white")
                    else:
                        ui.button(
                            icon="add",
                            color=None,
                        ).classes("bg-[#6b6d4a] text-white")
