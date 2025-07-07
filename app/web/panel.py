from functools import partial

import httpx
from consts import API_URL
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
                f"{API_URL}/guest/",
                headers={"token": token},
            )
            if response.status_code == 200:
                return response.json()
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")
                return []

    async def post_guest(name: str, phone: str, description: str, is_confirmed: bool, max_companion: int, companions: list[str]):
        async with httpx.AsyncClient() as client:
            data = {
                "name": name,
                "phone": phone,
                "description": description,
                "is_confirmed": is_confirmed,
                "max_companion": max_companion
            }
            for i, companion in enumerate(companions, 1):
                data.update({f"companion_{i}": companion})

            response = await client.post(
                f"{API_URL}/guest/",
                json=data,
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def put_guest(
        id: str, name: str, phone: str, description: str, is_confirmed: bool, companions: list[str]
    ):
        async with httpx.AsyncClient() as client:
            data={
                "id": id,
                "name": name,
                "phone": phone,
                "description": description,
                "is_confirmed": is_confirmed,
                "max_companion": len(companions)
            }
            for i, companion in enumerate(companions, 1):
                data.update({f"companion_{i}": companion})

            response = await client.put(
                f"{API_URL}/guest/",
                json=data,
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
                f"{API_URL}/guest/?id={id}",
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
                f"{API_URL}/gift/",
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
                f"{API_URL}/gift/",
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
                f"{API_URL}/gift/",
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
                f"{API_URL}/gift/?id={id}",
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Presente excluido com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    menu()
    with ui.element("div").classes("w-full mt-10 mb-20"):
        with ui.element("div").classes("max-w-[1200px] mx-auto w-full h-full p-6"):
            with ui.element("div").classes("flex justify-between flex-col gap-4 w-full"):
                ui.label("Adicionar convidado").classes("text-bold text-lg")

                post_companion_inputs = []
                def add_input(e):
                    container.clear()
                    post_companion_inputs.clear()
                    input_len = int(e.args)
                    if input_len > 5:
                        input_len = 5
                    with container:
                        for i in range(input_len):
                            input_field = ui.input(label=f'Nome do acompanhante {i+1}')
                            post_companion_inputs.append(input_field) 

                with ui.element('div').classes('flex w-full'):
                    with ui.element('div').classes('w-1/2 p-2'):
                        guest_name = ui.input(label="Nome")
                        guest_phone = ui.input(label="Telefone")
                        guest_description = ui.input(label="Descrição")
                        guest_max_companion=ui.number(label='Qt. de acompanhantes', max=5).on('change', add_input)
                        guest_is_confirmed = ui.checkbox("Confirmado", value=False)               

                    with ui.element('div').classes('w-1/2 p-2'):
                        container = ui.element("div")
                ui.button(
                    text="Adicionar",
                    icon="add",
                    on_click=lambda: post_guest(
                        guest_name.value,
                        guest_phone.value,
                        guest_description.value,
                        guest_is_confirmed.value,
                        guest_max_companion.value,
                        [inp.value for inp in post_companion_inputs]
                    ),
                    color=None,
                ).classes("bg-[#6b6d4a] text-white w-full")
            ui.separator().classes('my-10')
            guests = await get_guest()

            with ui.element("div").classes("col-span-2 w-full h-full max-h-[400px]"):
                ui.label("Lista de convidados").classes("text-bold text-lg")
                with ui.column().classes("overflow-y-scroll h-full"):
                    for item in guests:
                        with ui.row().classes(
                            "items-center justify-between w-full border p-4 sm:min-w-[680px] min-h-32 flex-nowrap"
                        ):
                            with ui.label().classes("flex-col flex-nowrap gap-1"):
                                with ui.element('div').classes('flex flex-nowrap'):
                                    ui.input("ID").props("readonly").value = item["id"]
                                    update_guest_name = ui.input("Nome", value=item["name"])
                                    update_guest_phone = ui.input("Telefone", value=item["phone"])
                                    update_guest_description = ui.input("Descrição", value=item["description"])
                                    update_guest_is_confirmed = ui.checkbox("Confirmado", value=item["is_confirmed"])
                                with ui.element('div').classes('flex flex-nowrap'):
                                    update_guest_companion_1 = ui.input("Acompanhante 1", value=item["companion_1"])
                                    update_guest_companion_2 = ui.input("Acompanhante 2", value=item["companion_2"])
                                    update_guest_companion_3 = ui.input("Acompanhante 3", value=item["companion_3"])
                                    update_guest_companion_4 = ui.input("Acompanhante 4", value=item["companion_4"])
                                    update_guest_companion_5 = ui.input("Acompanhante 5", value=item["companion_5"])
                                    
                                    liupdate_guest_companion_list = [
                                        update_guest_companion_1,
                                        update_guest_companion_2,
                                        update_guest_companion_3,
                                        update_guest_companion_4,
                                        update_guest_companion_5
                                    ]
                                    async def handle_update():
                                        companion_names = [c.value for c in liupdate_guest_companion_list if c.value]
                                        await put_guest(
                                            item["id"],
                                            update_guest_name.value,
                                            update_guest_phone.value,
                                            update_guest_description.value,
                                            update_guest_is_confirmed.value,
                                            companion_names
                                        )

                            with ui.row().classes("flex flex-col flex-nowrap gap-2"):
                                ui.button(icon="check", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(handle_update)

                                ui.button(icon="delete", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None: delete_guest(i),
                                        i=item["id"],
                                    )
                                )

            
            ui.separator().classes('my-10')

            with ui.element("div").classes(
                "flex justify-between flex-col gap-4 w-full max-h-[400px]"
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

            
            
            ui.separator().classes('my-10')
            
            gifts = await get_gift()
            with ui.element("div").classes(
                "col-span-2 w-full h-full max-h-[400px]"
            ):
                ui.label("Lista de presentes").classes("text-bold text-lg")
                with ui.column().classes("overflow-y-scroll h-full"):
                    for item in gifts:
                        with ui.row().classes(
                            "items-center justify-between w-full border p-4 sm:min-w-[680px] min-h-32 flex-nowrap"
                        ):
                            with ui.label().classes("flex flex-nowrap gap-3"):
                                ui.input("ID").props("readonly").value = item["id"]
                                update_gift_name = ui.input(label="Título", value=item["name"])
                                update_gift_url = ui.input(label="Link", value=item["url"])
                                update_gift_thumb = ui.input(label="URL da imagem", value=item["thumb"])
                                update_gift_price = ui.input(label="Preço", value=item["price"])

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
