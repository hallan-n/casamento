from functools import partial

import httpx
from nicegui import ui
from web.components.menu import menu
from web.utils import is_login


@ui.page("/panel")
async def index():
    token = await ui.run_javascript('localStorage.getItem("access_token");', timeout=30)

    is_login()

    async def get_guest():
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "http://localhost:8000/guest/",
                headers={"token": token},
            )
            if response.status_code == 200:
                return response.json()
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")
                return []

    async def post_guest(name: str, phone: str, description: str, is_confirmed: bool):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8000/guest/",
                json={
                    "name": name,
                    "phone": phone,
                    "description": description,
                    "is_confirmed": is_confirmed,
                },
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def put_guest(
        id: str, name: str, phone: str, description: str, is_confirmed: bool
    ):
        async with httpx.AsyncClient() as client:
            response = await client.put(
                "http://localhost:8000/guest/",
                json={
                    "id": id,
                    "name": name,
                    "phone": phone,
                    "description": description,
                    "is_confirmed": is_confirmed,
                },
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Convidado atualizado com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def delete_guest(id: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://localhost:8000/guest/?id={id}",
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Convidado excluido com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def get_gift():
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "http://localhost:8000/gift/",
                headers={"token": token},
            )
            if response.status_code == 200:
                return response.json()
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")
                return []

    async def post_gift(name: str, url: str, thumb: str, price: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8000/gift/",
                json={
                    "name": name,
                    "url": url,
                    "thumb": thumb,
                    "price": price,
                },
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def put_gift(id: str, name: str, url: str, thumb: str, price: str):
        async with httpx.AsyncClient() as client:
            response = await client.put(
                "http://localhost:8000/gift/",
                json={
                    "id": id,
                    "name": name,
                    "url": url,
                    "thumb": thumb,
                    "price": price,
                },
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Presente atualizado com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def delete_gift(id: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://localhost:8000/gift/?id={id}",
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Presente excluido com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    menu()
    with ui.element("div").classes("w-full mt-10 mb-20"):
        with ui.element("div").classes(
            "grid grid-cols-3 gap-6 max-w-[1200px] mx-auto w-full h-full"
        ):
            with ui.element("div").classes(
                "flex justify-between flex-col gap-4 w-full max-h-[400px]"
            ):
                ui.label("Adicionar convidado").classes("text-bold text-lg")
                guest_name = ui.input(label="Nome")
                guest_phone = ui.input(label="Telefone")
                guest_description = ui.input(label="Descrição")
                guest_is_confirmed = ui.checkbox("Confirmado", value=False)
                ui.button(
                    text="Adicionar",
                    icon="add",
                    on_click=lambda: post_guest(
                        guest_name.value,
                        guest_phone.value,
                        guest_description.value,
                        guest_is_confirmed.value,
                    ),
                    color=None,
                ).classes("bg-[#6b6d4a] text-white w-full")

            guests = await get_guest()

            with ui.element("div").classes("col-span-2 w-full h-full max-h-[400px]"):
                ui.label("Lista de convidados").classes("text-bold text-lg")
                with ui.column().classes("overflow-y-scroll h-full"):
                    for item in guests:
                        with ui.row().classes(
                            "items-center justify-between w-full border p-4 sm:min-w-[680px] min-h-32 flex-nowrap"
                        ):
                            with ui.label().classes("flex flex-nowrap gap-1"):
                                ui.input("ID").props("readonly").classes(
                                    "w-24"
                                ).value = item["id"]
                                update_guest_name = ui.input(
                                    "Nome", value=item["name"]
                                ).classes("w-24")
                                update_guest_phone = ui.input(
                                    "Telefone", value=item["phone"]
                                ).classes("w-24")
                                update_guest_description = ui.input(
                                    "Descrição", value=item["description"]
                                ).classes("w-24")
                                update_guest_is_confirmed = ui.checkbox(
                                    "Confirmado", value=item["is_confirmed"]
                                )

                            with ui.row().classes("flex flex-row flex-nowrap gap-2"):
                                ui.button(icon="check", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None, n=None, p=None, d=None, c=None: put_guest(
                                            i, n.value, p.value, d.value, c.value
                                        ),
                                        i=item["id"],
                                        n=update_guest_name,
                                        p=update_guest_phone,
                                        d=update_guest_description,
                                        c=update_guest_is_confirmed,
                                    )
                                )

                                ui.button(icon="delete", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None: delete_guest(i),
                                        i=item["id"],
                                    )
                                )

            with ui.element("div").classes(
                "flex justify-between flex-col gap-4 w-full max-h-[400px] mt-20"
            ):
                ui.label("Adicionar presente").classes("text-bold text-lg")
                gift_name = ui.input(label="Título")
                gift_url = ui.input(label="Link")
                gift_thumb = ui.input(label="URL da imagem")
                gift_price = ui.input(label="Preço")

                ui.button(
                    text="Adicionar",
                    icon="add",
                    on_click=lambda: post_gift(
                        gift_name.value,
                        gift_url.value,
                        gift_thumb.value,
                        gift_price.value,
                    ),
                    color=None,
                ).classes("bg-[#6b6d4a] text-white w-full")

            gifts = await get_gift()
            with ui.element("div").classes(
                "col-span-2 w-full h-full max-h-[400px] mt-20"
            ):
                ui.label("Lista de presentes").classes("text-bold text-lg")
                with ui.column().classes("overflow-y-scroll h-full"):
                    for item in gifts:
                        with ui.row().classes(
                            "items-center justify-between w-full border p-4 sm:min-w-[680px] min-h-32 flex-nowrap"
                        ):
                            with ui.label().classes("flex flex-nowrap gap-3"):
                                ui.input("ID").props("readonly").classes(
                                    "w-24"
                                ).value = item["id"]
                                update_gift_name = ui.input(
                                    label="Título", value=item["name"]
                                ).classes("w-24")
                                update_gift_url = ui.input(
                                    label="Link", value=item["url"]
                                ).classes("w-24")
                                update_gift_thumb = ui.input(
                                    label="URL da imagem", value=item["thumb"]
                                ).classes("w-24")
                                update_gift_price = ui.input(
                                    label="Preço", value=item["price"]
                                ).classes("w-24")

                            with ui.row().classes("flex flex-row flex-nowrap gap-2"):
                                ui.button(icon="check", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None, n=None, u=None, t=None, p=None: put_gift(
                                            i, n.value, u.value, t.value, p.value
                                        ),
                                        i=item["id"],
                                        n=update_gift_name,
                                        u=update_gift_url,
                                        t=update_gift_thumb,
                                        p=update_gift_price,
                                    )
                                )

                                ui.button(icon="delete", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None: delete_gift(i),
                                        i=item["id"],
                                    )
                                )
