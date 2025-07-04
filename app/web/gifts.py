from functools import partial

import httpx
from nicegui import ui
from web.components.menu import menu
from web.utils import get_current_user


@ui.page("/gifts")
async def index():
    current_user = await get_current_user()

    menu(current_user)

    def format_currency(value):
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    async def get_gift():
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:8000/gift/")
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 422:
                ui.notify("Erro: Erro ao buscar presentes", color="red")
            elif response.status_code == 404:
                ui.notify("Nenhum presente cadastrado", color="red")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def put_gift(gift_dict, guest_id):
        if not current_user:
            ui.notify(
                "Você não está logado, acesse o site pelo seu link único.", color="red"
            )
            return
        gift_dict.update({"guest_id": guest_id})

        async with httpx.AsyncClient() as client:
            response = await client.put(
                "http://localhost:8000/gift/",
                json=gift_dict,
            )
            if response.status_code == 200:
                if guest_id:
                    ui.notify("Presente cancelado com sucesso!", color="green")
                else:
                    ui.notify("Presente dado com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    with ui.element("div").classes("mx-auto mt-10 w-full max-w-[1200px] px-4"):
        ui.label("Lista de Presentes").classes(
            "text-2xl mb-2 text-center md:text-start text-bold text-gray-800"
        )
        gifts = await get_gift()

        if gifts:
            with ui.element("div").classes(
                "justify-center grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mb-10"
            ):
                for item in gifts:
                    with ui.card().classes(
                        "justify-between w-full h-[400px] max-w-[300px] mx-auto"
                    ):
                        ui.image(item.get("thumb")).classes(
                            "rounded-lg w-full h-52 object-cover"
                        )
                        ui.label(
                            f'{item.get("name")[:62] + "..." if len(item.get("name")) > 60 else item.get("name")}'
                        ).classes("text-bold text-sm mt-4")
                        with ui.element("div").classes(
                            "flex w-full justify-between items-center mt-4"
                        ):
                            ui.label(
                                f'R$ {format_currency(item.get("price"))}'
                            ).classes("text-md")

                            if not item.get("guest_id"):
                                ui.button(
                                    text="Dar presente",
                                    icon="add_shopping_cart",
                                    color=None,
                                ).classes("bg-[#6b6d4a] text-white").on_click(
                                    partial(
                                        lambda _=None, data=None, guest_id=None: put_gift(
                                            data, guest_id
                                        ),
                                        data=item,
                                        guest_id=current_user.get("id", "").replace(
                                            "-", ""
                                        ),
                                    )
                                )

                            elif item.get("guest_id").replace(
                                "-", ""
                            ) == current_user.get("id", "").replace("-", ""):
                                ui.button(
                                    text="Dado por você",
                                    icon="check_circle",
                                    color=None,
                                ).classes(
                                    "text-white bg-green-500 hover:bg-red-500"
                                ).on(
                                    "mouseover",
                                    lambda e: (
                                        e.sender.set_text("Cancelar presente"),
                                        e.sender.set_icon("close"),
                                    ),
                                ).on(
                                    "mouseout",
                                    lambda e: (
                                        e.sender.set_text("Dado por você"),
                                        e.sender.set_icon("check_circle"),
                                    ),
                                ).on_click(
                                    partial(
                                        lambda _=None, data=None, guest_id=None: put_gift(
                                            data, guest_id
                                        ),
                                        data=item,
                                        guest_id=None,
                                    )
                                )

                            elif item.get("guest_id").replace("-", "") and item.get(
                                "guest_id"
                            ).replace("-", "") != current_user.get("id", ""):
                                ui.button(
                                    text="Presente dado",
                                    icon="check_circle",
                                    color=None,
                                ).classes("bg-[#6b6d4a] text-white").props("disabled")
        else:
            ui.label("Nenhum presente encontrado").classes(
                "text-bold text-gray-500 text-lg"
            )
